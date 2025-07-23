# Flask 프레임워크에서 Blueprint, request, jsonify 모듈을 임포트합니다.
# Blueprint는 모듈화된 애플리케이션을 구성하는 데 사용됩니다.
# request는 클라이언트로부터의 HTTP 요청 데이터를 다루는 데 사용됩니다.
# jsonify는 파이썬 딕셔너리나 리스트를 JSON 형식의 응답으로 변환하는 데 사용됩니다.
from flask import Blueprint, request, jsonify

# response_utils.py 파일에서 정의된 api_response와 api_error_response 함수를 임포트합니다.
# 이 함수들은 API 응답을 표준화된 형식(success, message, statusCode, result)으로 생성하는 역할을 합니다.
from response_utils import api_response, api_error_response

# Blueprint 객체를 생성합니다.
# 'items'는 이 Blueprint의 이름입니다.
# __name__은 현재 모듈의 이름을 Flask에 알려줍니다.
# url_prefix='/api/items'는 이 Blueprint에 정의된 모든 라우트의 URL 앞에 '/api/items'가 붙도록 설정합니다.
# 예를 들어, @item_bp.route('/')는 실제로는 /api/items/ 경로가 됩니다.
item_bp = Blueprint('items', __name__, url_prefix='/api/items')

# 임시 데이터 저장소 (리스트 형태)
# 실제 웹 애플리케이션에서는 이 데이터를 데이터베이스(예: SQLite, PostgreSQL, MySQL)에 저장합니다.
# 서버가 재시작되면 이 리스트의 내용은 초기화됩니다.
items = [
    {"id": 1, "name": "Item A", "description": "Description for Item A"},
    {"id": 2, "name": "Item B", "description": "Description for Item B"}
]
# 새로운 아이템에 할당될 다음 ID를 추적하는 변수입니다.
next_id = 3

# 모든 아이템을 가져오는 API 엔드포인트입니다.
# @item_bp.route('/', methods=['GET'])는 HTTP GET 요청이 /api/items/ 경로로 들어올 때 이 함수를 실행하도록 매핑합니다.
@item_bp.route('/', methods=['GET'])
def get_items():
    # api_response 함수를 사용하여 모든 아이템(items)을 JSON 형식으로 반환합니다.
    # message는 성공 메시지, status_code는 HTTP 200 OK를 나타냅니다.
    return api_response(data=items, message="Items retrieved successfully", status_code=200)

# 특정 아이템을 가져오는 API 엔드포인트입니다.
# @item_bp.route('/<int:item_id>', methods=['GET'])는 HTTP GET 요청이 /api/items/<item_id> 경로로 들어올 때 이 함수를 실행합니다.
# <int:item_id>는 URL 경로에서 정수형 item_id 값을 추출하여 함수의 인자로 전달합니다.
@item_bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # items 리스트에서 item_id와 일치하는 아이템을 찾습니다.
    # next()와 제너레이터 표현식을 사용하여 첫 번째 일치하는 아이템을 찾고, 없으면 None을 반환합니다.
    item = next((item for item in items if item['id'] == item_id), None)
    # 아이템이 존재하면
    if item:
        # 해당 아이템을 성공 응답으로 반환합니다.
        return api_response(data=item, message="Item retrieved successfully", status_code=200)
    # 아이템이 존재하지 않으면
    # api_error_response 함수를 사용하여 아이템을 찾을 수 없다는 오류 응답을 반환합니다.
    # status_code는 HTTP 404 Not Found를 나타냅니다.
    return api_error_response(message="Item not found", status_code=404)

# 새로운 아이템을 생성하는 API 엔드포인트입니다.
# @item_bp.route('/', methods=['POST'])는 HTTP POST 요청이 /api/items/ 경로로 들어올 때 이 함수를 실행합니다.
@item_bp.route('/', methods=['POST'])
def create_item():
    # 전역 변수인 next_id를 함수 내에서 수정하기 위해 global 키워드를 사용합니다.
    global next_id
    # 요청 본문이 JSON 형식이 아니거나, 'name' 필드가 없으면 오류 응답을 반환합니다.
    if not request.json or not 'name' in request.json:
        return api_error_response(message="Name is required", status_code=400)
    
    # 새로운 아이템 딕셔너리를 생성합니다.
    # id는 next_id를 사용하고, name은 요청 JSON에서 가져옵니다.
    # description은 요청 JSON에서 가져오거나, 없으면 빈 문자열을 기본값으로 사용합니다.
    new_item = {
        "id": next_id,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    # 생성된 새 아이템을 items 리스트에 추가합니다.
    items.append(new_item)
    # 다음 아이템을 위해 next_id를 1 증가시킵니다.
    next_id += 1
    # 생성된 아이템 정보를 성공 응답으로 반환합니다.
    # status_code는 HTTP 201 Created를 나타냅니다.
    return api_response(data=new_item, message="Item created successfully", status_code=201)

# 특정 아이템을 업데이트하는 API 엔드포인트입니다.
# @item_bp.route('/<int:item_id>', methods=['PUT'])는 HTTP PUT 요청이 /api/items/<item_id> 경로로 들어올 때 이 함수를 실행합니다.
@item_bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # items 리스트에서 item_id와 일치하는 아이템을 찾습니다.
    item = next((item for item in items if item['id'] == item_id), None)
    # 아이템이 존재하지 않으면 오류 응답을 반환합니다.
    if not item:
        return api_error_response(message="Item not found", status_code=404)
    
    # 요청 본문이 JSON 형식이 아니면 오류 응답을 반환합니다.
    if not request.json:
        return api_error_response(message="Request body must be JSON", status_code=400)
    
    # 아이템의 name과 description을 요청 JSON의 값으로 업데이트합니다.
    # 요청 JSON에 해당 필드가 없으면 기존 값을 유지합니다.
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    # 업데이트된 아이템 정보를 성공 응답으로 반환합니다.
    return api_response(data=item, message="Item updated successfully", status_code=200)

# 특정 아이템을 삭제하는 API 엔드포인트입니다.
# @item_bp.route('/<int:item_id>', methods=['DELETE'])는 HTTP DELETE 요청이 /api/items/<item_id> 경로로 들어올 때 이 함수를 실행합니다.
@item_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # 전역 변수인 items 리스트를 함수 내에서 수정하기 위해 global 키워드를 사용합니다.
    global items
    # 삭제 전 items 리스트의 길이를 저장합니다.
    initial_len = len(items)
    # item_id와 일치하지 않는 아이템들로 새로운 리스트를 생성하여 items를 업데이트합니다.
    # 이는 사실상 일치하는 아이템을 리스트에서 제거하는 효과를 가집니다.
    items = [item for item in items if item['id'] != item_id]
    # 삭제 후 리스트의 길이가 줄어들었으면 (즉, 아이템이 삭제되었으면)
    if len(items) < initial_len:
        # 성공 응답을 반환합니다.
        return api_response(data=None, message="Item deleted successfully", status_code=200)
    # 아이템이 삭제되지 않았으면 (즉, 해당 ID의 아이템을 찾지 못했으면)
    # api_error_response 함수를 사용하여 아이템을 찾을 수 없다는 오류 응답을 반환합니다.
    # status_code는 HTTP 404 Not Found를 나타냅니다.
    return api_error_response(message="Item not found", status_code=404)
