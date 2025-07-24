# api/item/service/item_service.py
# 이 파일은 아이템 관련 비즈니스 로직을 담당하는 ItemService 클래스를 정의합니다.
# Controller와 Repository 사이에서 중개자 역할을 하며, 여러 Repository 작업을 조합하거나
# 추가적인 비즈니스 규칙을 적용하는 등의 역할을 수행합니다.

# ..repository는 현재 모듈(service)의 부모 디렉토리(item) 아래의 repository 패키지를 의미합니다.
# ItemRepository를 임포트하여 데이터베이스 CRUD 작업을 수행합니다.
from ..repository import ItemRepository
# ..dto는 현재 모듈(service)의 부모 디렉토리(item) 아래의 dto 패키지를 의미합니다.
# ItemCreateDTO와 ItemUpdateDTO를 임포트하여 데이터 전송 객체로 사용합니다.
from ..dto import ItemCreateDTO, ItemUpdateDTO
# ..entity는 현재 모듈(service)의 부모 디렉토리(item) 아래의 entity 패키지를 의미합니다.
# Item 엔티티를 임포트하여 데이터 모델로 사용합니다.
from ..entity import Item

# ItemService 클래스
# 아이템 관련 비즈니스 로직을 처리합니다.
class ItemService:
    # ItemService 인스턴스 초기화 시 ItemRepository 인스턴스를 생성합니다.
    # Service는 Repository를 사용하여 데이터베이스와 상호작용합니다.
    def __init__(self):
        self.item_repository = ItemRepository()

    # 모든 아이템을 조회하는 비즈니스 로직입니다.
    # Repository에서 Item 객체 리스트를 받아와 각 객체를 딕셔너리 형태로 변환하여 반환합니다.
    def get_all_items(self) -> list[dict]:
        items = self.item_repository.get_all()
        return [item.to_dict() for item in items]

    # 특정 ID를 가진 아이템을 조회하는 비즈니스 로직입니다.
    # Repository에서 Item 객체를 받아와 딕셔너리 형태로 변환하여 반환합니다.
    def get_item_by_id(self, item_id: int) -> dict | None:
        item = self.item_repository.get_by_id(item_id)
        if item:
            return item.to_dict()
        return None

    # 새로운 아이템을 생성하는 비즈니스 로직입니다.
    # ItemCreateDTO를 입력받아 Repository를 통해 아이템을 생성하고, 생성된 아이템을 딕셔너리 형태로 반환합니다.
    def create_item(self, item_dto: ItemCreateDTO) -> dict:
        new_item = self.item_repository.create(item_dto.name, item_dto.description)
        return new_item.to_dict()

    # 특정 아이템의 정보를 업데이트하는 비즈니스 로직입니다.
    # ItemUpdateDTO를 입력받아 Repository를 통해 아이템을 업데이트하고, 업데이트된 아이템을 딕셔너리 형태로 반환합니다.
    def update_item(self, item_id: int, item_dto: ItemUpdateDTO) -> dict | None:
        updated_item = self.item_repository.update(item_id, item_dto.name, item_dto.description)
        if updated_item:
            return updated_item.to_dict()
        return None

    # 특정 아이템을 삭제하는 비즈니스 로직입니다.
    # Repository를 통해 아이템을 삭제하고, 성공 여부를 반환합니다.
    def delete_item(self, item_id: int) -> bool:
        return self.item_repository.delete(item_id)