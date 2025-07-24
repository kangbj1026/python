from functools import wraps
from flask import jsonify

# API 응답을 표준화하고 예외를 처리하는 데코레이터입니다.
# 이 데코레이터는 뷰 함수가 반환하는 데이터를 JSON 형식으로 변환하고,
# 성공/실패 메시지, 상태 코드 등을 포함한 일관된 응답 형식을 제공합니다.
# 또한, 뷰 함수 실행 중 발생하는 예외를 잡아서 오류 응답을 생성합니다.
def handle_response(message="Success", status_code=200, success=True):
	# 실제 데코레이터 함수를 정의합니다.
	def decorator(f):
		# 원본 함수의 메타데이터(이름, 문서 등)를 유지하기 위해 @wraps 데코레이터를 사용합니다.
		@wraps(f)
		# 데코레이터가 적용될 뷰 함수를 감싸는 래퍼 함수입니다.
		# *args와 **kwargs는 원본 함수가 받을 수 있는 모든 인자를 유연하게 처리합니다.
		def decorated_function(*args, **kwargs):
			try:
				# 원본 뷰 함수를 실행하고 그 결과를 data 변수에 저장합니다.
				data = f(*args, **kwargs)
				# 성공적인 API 응답을 위한 페이로드(데이터 구조)를 생성합니다.
				response_payload = {
					"success": success,      # 요청 성공 여부 (True/False)
					"message": message,      # 응답 메시지
					"statusCode": status_code, # HTTP 상태 코드
					"result": data           # 뷰 함수가 반환한 실제 데이터
				}
				# 페이로드를 JSON 형식으로 변환하여 Flask 응답 객체를 생성합니다.
				response = jsonify(response_payload)
				# 응답 헤더에 Content-Type을 설정하여 클라이언트에게 JSON임을 알리고 한글 깨짐을 방지합니다.
				response.headers['Content-Type'] = 'application/json; charset=utf-8'
				# 생성된 응답 객체와 HTTP 상태 코드를 반환합니다.
				return response, status_code
			except Exception as e:
				# 뷰 함수 실행 중 예외가 발생하면 이곳에서 처리합니다.
				error_message = str(e) # 예외 메시지를 문자열로 변환합니다.
				error_status_code = 500 # 기본 오류 상태 코드를 500으로 설정합니다.
				# 오류 API 응답을 위한 페이로드를 생성합니다.
				response_payload = {
					"success": False,        # 요청 실패
					"message": error_message,  # 오류 메시지
					"statusCode": error_status_code, # 오류 HTTP 상태 코드
					"result": None           # 오류 발생 시 데이터는 없음
				}
				# 오류 페이로드를 JSON 형식으로 변환하여 Flask 응답 객체를 생성합니다.
				response = jsonify(response_payload)
				# 응답 헤더에 Content-Type을 설정합니다.
				response.headers['Content-Type'] = 'application/json; charset=utf-8'
				# 생성된 오류 응답 객체와 오류 HTTP 상태 코드를 반환합니다.
				return response, error_status_code
		# 래퍼 함수를 반환합니다.
		return decorated_function
	# 데코레이터 함수를 반환합니다.
	return decorator