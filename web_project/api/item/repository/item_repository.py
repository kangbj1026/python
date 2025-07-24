# api/item/repository/item_repository.py
# 이 파일은 데이터베이스와의 직접적인 상호작용을 담당하는 ItemRepository 클래스를 정의합니다.
# 데이터의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 등 CRUD 작업을 처리합니다.
# SQLAlchemy의 ORM 기능을 사용하여 파이썬 객체로 데이터베이스 작업을 수행합니다.

# database.py에서 정의된 db 객체를 임포트합니다.
# db 객체는 SQLAlchemy 세션 및 쿼리 기능을 제공합니다.
from database import db
# ..entity는 현재 모듈(repository)의 부모 디렉토리(item) 아래의 entity 패키지를 의미합니다.
# Item 엔티티를 임포트하여 데이터베이스 모델로 사용합니다.
from ..entity import Item

# ItemRepository 클래스
# 데이터베이스의 'items' 테이블에 대한 CRUD 작업을 수행합니다.
class ItemRepository:
    # 모든 아이템을 데이터베이스에서 조회하여 반환합니다.
    # Item.query.all()은 'items' 테이블의 모든 레코드를 Item 객체 리스트로 반환합니다.
    def get_all(self) -> list[Item]:
        return Item.query.all()

    # 특정 ID를 가진 아이템을 데이터베이스에서 조회하여 반환합니다.
    # Item.query.get(item_id)는 기본 키(id)를 사용하여 레코드를 조회합니다.
    def get_by_id(self, item_id: int) -> Item | None:
        return Item.query.get(item_id)

    # 새로운 아이템을 데이터베이스에 생성합니다.
    # db.session.add(): 새로운 Item 객체를 세션에 추가합니다.
    # db.session.commit(): 세션에 추가된 변경사항(새로운 아이템)을 데이터베이스에 영구적으로 저장합니다.
    def create(self, name: str, description: str) -> Item:
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    # 특정 ID를 가진 아이템의 정보를 업데이트합니다.
    # name과 description이 None이 아니면 해당 필드를 업데이트합니다.
    # db.session.commit(): 변경된 내용을 데이터베이스에 저장합니다.
    def update(self, item_id: int, name: str, description: str) -> Item | None:
        item = self.get_by_id(item_id)
        if item:
            if name is not None:
                item.name = name
            if description is not None:
                item.description = description
            db.session.commit()
            return item
        return None

    # 특정 ID를 가진 아이템을 데이터베이스에서 삭제합니다.
    # db.session.delete(): 세션에서 해당 Item 객체를 삭제 대상으로 표시합니다.
    # db.session.commit(): 삭제 변경사항을 데이터베이스에 적용합니다.
    def delete(self, item_id: int) -> bool:
        item = self.get_by_id(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
