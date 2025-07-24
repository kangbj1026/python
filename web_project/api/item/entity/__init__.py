# api/item/entity/__init__.py
# 이 파일은 'entity' 디렉토리가 파이썬 패키지임을 나타냅니다.
# 이 패키지 내의 item_entity.py에서 정의된 Entity 클래스들을 패키지 레벨로 노출하여
# 다른 계층(예: Repository, Service)에서 더 쉽게 임포트할 수 있도록 합니다.

# item_entity 모듈에서 Item 클래스를 임포트합니다.
# .item_entity는 현재 패키지(entity) 내의 item_entity 모듈을 의미합니다.
from .item_entity import Item

# 이 패키지에서 'from api.item.entity import *' 구문을 사용할 때 외부에 공개할 이름들을 정의합니다.
# 여기서는 Item만 공개하도록 설정합니다.
__all__ = ['Item']