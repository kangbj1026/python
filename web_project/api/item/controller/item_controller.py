# api/item/controller/item_controller.py
# 이 파일은 아이템 관련 REST API 엔드포인트를 정의하고 HTTP 요청을 처리합니다.
# 클라이언트의 요청을 받아 Service 계층으로 전달하고, Service 계층의 처리 결과를 클라이언트에게 응답합니다.

# Flask의 Blueprint, request, jsonify 모듈을 임포트합니다.
# Blueprint: 관련된 라우트와 뷰 함수를 그룹화하여 애플리케이션을 모듈화합니다.
# request: 클라이언트로부터의 HTTP 요청 데이터를 다룹니다.
# jsonify: 파이썬 딕셔너리나 리스트를 JSON 형식의 응답으로 변환합니다.
from flask import Blueprint, request, jsonify

# 사용자 정의 데코레이터인 handle_response를 임포트합니다.
# 이 데코레이터는 API 응답을 표준화하고 예외 처리를 담당합니다.
from utils.decorators import handle_response

# 아이템 비즈니스 로직을 담당하는 ItemService를 임포트합니다.
# ..service는 현재 모듈(controller)의 부모 디렉토리(item) 아래의 service 패키지를 의미합니다.
from ..service import ItemService
# 데이터 전송 객체(DTO)를 임포트합니다.
# ..dto는 현재 모듈(controller)의 부모 디렉토리(item) 아래의 dto 패키지를 의미합니다.
from ..dto import ItemCreateDTO, ItemUpdateDTO

# 'items'라는 이름의 Blueprint를 생성합니다.
# url_prefix='/api/items'는 이 Blueprint에 정의된 모든 라우트의 URL이 '/api/items'로 시작함을 의미합니다.
item_bp = Blueprint('items', __name__, url_prefix='/api/items')

# ItemService 인스턴스를 생성합니다.
# Controller는 Service 계층의 메서드를 호출하여 비즈니스 로직을 수행합니다.
item_service = ItemService()

# 모든 아이템을 가져오는 API 엔드포인트입니다.
# GET 요청을 처리하며, handle_response 데코레이터를 통해 응답이 처리됩니다.
@item_bp.route('/', methods=['GET'])
@handle_response(message="Items retrieved successfully", status_code=200)
def get_items():
    # ItemService를 통해 모든 아이템 데이터를 조회하고 반환합니다.
    return item_service.get_all_items()

# 특정 아이템을 가져오는 API 엔드포인트입니다.
# GET 요청을 처리하며, URL에서 item_id를 파라미터로 받습니다.
@item_bp.route('/<int:item_id>', methods=['GET'])
@handle_response(message="Item retrieved successfully", status_code=200)
def get_item(item_id):
    # ItemService를 통해 특정 ID의 아이템을 조회합니다.
    item = item_service.get_item_by_id(item_id)
    # 아이템이 존재하면 해당 아이템 데이터를 반환합니다.
    if item:
        return item
    # 아이템을 찾을 수 없으면 ValueError를 발생시켜 데코레이터에서 오류 응답을 처리하도록 합니다.
    raise ValueError("Item not found")

# 새로운 아이템을 생성하는 API 엔드포인트입니다.
# POST 요청을 처리하며, 요청 본문(JSON)에서 아이템 정보를 받습니다.
# cmd - curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"새로운 아이템\", \"description\": \"이것은 새로 생성할 아이템입니다.\"}" http://127.0.0.1:5000/api/items/
@item_bp.route('/', methods=['POST'])
@handle_response(message="Item created successfully", status_code=201)
def create_item():
    # 요청 본문이 JSON 형식이 아니거나 'name' 필드가 없으면 ValueError를 발생시킵니다.
    if not request.json or 'name' not in request.json:
        raise ValueError("Name is required")
    
    # 요청 JSON 데이터를 ItemCreateDTO 객체로 변환합니다.
    item_dto = ItemCreateDTO(
        name=request.json['name'],
        description=request.json.get('description', "") # description은 선택 사항
    )
    # ItemService를 통해 새로운 아이템을 생성하고 그 결과를 반환합니다.
    new_item = item_service.create_item(item_dto)
    return new_item

# 특정 아이템을 업데이트하는 API 엔드포인트입니다.
# PUT 요청을 처리하며, URL에서 item_id를 파라미터로 받고 요청 본문(JSON)에서 업데이트 정보를 받습니다.
@item_bp.route('/<int:item_id>', methods=['PUT'])
@handle_response(message="Item updated successfully", status_code=200)
def update_item(item_id):
    # 요청 본문이 JSON 형식이 아니면 ValueError를 발생시킵니다.
    if not request.json:
        raise ValueError("Request body must be JSON")

    # 요청 JSON 데이터를 ItemUpdateDTO 객체로 변환합니다.
    item_dto = ItemUpdateDTO(
        name=request.json.get('name'), # name은 선택 사항
        description=request.json.get('description') # description은 선택 사항
    )
    # ItemService를 통해 아이템을 업데이트하고 그 결과를 반환합니다.
    updated_item = item_service.update_item(item_id, item_dto)
    # 업데이트된 아이템이 존재하면 반환합니다.
    if updated_item:
        return updated_item
    # 아이템을 찾을 수 없으면 ValueError를 발생시킵니다.
    raise ValueError("Item not found")

# 특정 아이템을 삭제하는 API 엔드포인트입니다.
# DELETE 요청을 처리하며, URL에서 item_id를 파라미터로 받습니다.
@item_bp.route('/<int:item_id>', methods=['DELETE'])
@handle_response(message="Item deleted successfully", status_code=200)
def delete_item(item_id):
    # ItemService를 통해 아이템을 삭제합니다.
    if item_service.delete_item(item_id):
        # 삭제 성공 시 HTTP 200 OK와 함께 내용 없이 반환합니다.
        return None
    # 아이템을 찾을 수 없으면 ValueError를 발생시킵니다.
    raise ValueError("Item not found")