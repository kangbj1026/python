from flask import Blueprint, render_template, request, jsonify, session
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# https://aistudio.google.com/app/apikey key 발급 url
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


ai_bp = Blueprint('ai', __name__, url_prefix='/ai')

def chat_with_gemini(user_input):
    try:
        if 'chat_history' not in session:
            session['chat_history'] = []

        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        chat = model.start_chat(history=session['chat_history'])
        response = chat.send_message(user_input)

        session['chat_history'].append({'role': 'user', 'parts': [user_input]})
        session['chat_history'].append({'role': 'model', 'parts': [response.text]})
        session.modified = True # 세션 변경 사항 저장

        return response.text
    except Exception as e:
        return f"챗봇 응답 생성 중 오류가 발생했습니다: {e}"

@ai_bp.route("/list_models")
def list_gemini_models():
	try:
		models = genai.list_models()
		model_names = []
		for m in models:
			model_names.append({
				"name": m.name,
				"supported_methods": m.supported_generation_methods
			})
		return jsonify({"available_models": model_names})
	except Exception as e:
		return jsonify({"error": str(e)}), 500

@ai_bp.route("/clear_chat", methods=["POST"])
def clear_chat():
    session.pop('chat_history', None)
    session.modified = True
    return jsonify({"status": "success", "message": "대화 기록이 초기화되었습니다."})


@ai_bp.route("/main")
def index():
	return render_template("./index.html")

@ai_bp.route("/chat", methods=["POST"])
def chat():
	data = request.get_json()
	user_input = data.get("message", "")
	response = chat_with_gemini(user_input)
	return jsonify({"response": response})
