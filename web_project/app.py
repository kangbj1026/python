"""
* 역할: 이 파일은 Flask 웹 애플리케이션의 메인 코드를 포함합니다.
* 상세 설명:
* from flask import Flask: Flask 프레임워크에서 Flask 클래스를 가져옵니다. 이 클래스를 사용하여 웹 애플리케이션 인스턴스를
    생성합니다.
* app = Flask(__name__): Flask 애플리케이션 인스턴스를 생성합니다. __name__은 현재 모듈의 이름을 나타내며, Flask가 리소스(템플릿,
    정적 파일 등)를 찾을 때 사용됩니다.
* @app.route('/'): 이 데코레이터는 바로 아래의 함수를 특정 URL 경로('/'는 웹사이트의 루트 경로)에 연결합니다. 즉, 사용자가
    웹사이트의 메인 페이지에 접속하면 이 함수가 실행됩니다.
* def hello_world(): return 'Hello, World! This is a basic Flask app.': hello_world 함수는 사용자가 루트 경로에 접속했을 때
    실행되며, "Hello, World! This is a basic Flask app."라는 문자열을 웹 브라우저에 반환합니다.
* @app.route('/about'): /about 경로에 연결되는 데코레이터입니다.
* def about(): return 'This is the about page.': about 함수는 사용자가 /about 경로에 접속했을 때 실행되며, "This is the about
    page."라는 문자열을 반환합니다.
* if __name__ == '__main__': app.run(debug=True): 이 부분은 app.py 파일이 직접 실행될 때 (다른 모듈에서 임포트되지 않고) Flask 개발
    서버를 시작하도록 합니다.
"""
from flask import Flask, request, jsonify
from item_controller import item_bp # item_controller에서 Blueprint 임포트
from basics_controller import basics_bp # basics_controller에서 Blueprint 임포트
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 한글 깨짐 방지
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True # JSON 응답을 예쁘게 출력

# 로깅 설정
# 로거 생성
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) # INFO 레벨 이상의 로그만 기록

# 파일 핸들러 (access.log)
# RotatingFileHandler는 로그 파일이 특정 크기에 도달하면 자동으로 새 파일로 교체합니다.
file_handler = RotatingFileHandler('access.log', maxBytes=1024 * 1024 * 5, backupCount=5, encoding='utf-8') # 5MB, 5개 파일
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# 콘솔 핸들러
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a basic Flask app.'

@app.route('/about')
def about():
    return 'This is the about page.'

# 모든 요청 전에 실행되는 함수
@app.before_request
def log_request_info():
    logger.info(f'Request: {request.method} {request.url} from {request.remote_addr}')
    if request.is_json:
        logger.info(f'Request JSON: {request.json}')
    elif request.form:
        logger.info(f'Request Form: {request.form}')

# item_bp Blueprint를 애플리케이션에 등록
app.register_blueprint(item_bp)

# basics_bp Blueprint를 애플리케이션에 등록
app.register_blueprint(basics_bp)

if __name__ == '__main__':
    app.run(debug=True)
