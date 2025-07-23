from flask import jsonify

def api_response(data=None, message="Success", status_code=200, success=True):
    """
    표준화된 API 응답 형식을 생성합니다.

    :param data: API 결과 데이터 (result 필드에 포함될 내용)
    :param message: 응답 메시지
    :param status_code: HTTP 상태 코드
    :param success: 요청 성공 여부 (True/False)
    :return: Flask jsonify 응답
    """
    response_payload = {
        "success": success,
        "message": message,
        "statusCode": status_code,
        "result": data
    }
    response = jsonify(response_payload)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, status_code

def api_error_response(message="An error occurred", status_code=500, data=None):
    """
    표준화된 API 오류 응답 형식을 생성합니다.

    :param message: 오류 메시지
    :param status_code: HTTP 상태 코드 (기본값 500 Internal Server Error)
    :param data: 오류와 관련된 추가 데이터 (선택 사항)
    :return: Flask jsonify 응답
    """
    return api_response(data=data, message=message, status_code=status_code, success=False)
