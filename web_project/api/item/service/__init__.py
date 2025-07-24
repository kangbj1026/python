# api/item/service/__init__.py
# 이 파일은 'service' 디렉토리가 파이썬 패키지임을 나타냅니다.
# 이 패키지 내의 item_service.py에서 정의된 ItemService 클래스를 패키지 레벨로 노출하여
# 상위 패키지(api.item)나 Controller 계층에서 더 쉽게 임포트할 수 있도록 합니다.

# item_service 모듈에서 ItemService 클래스를 임포트합니다.
# .item_service는 현재 패키지(service) 내의 item_service 모듈을 의미합니다.
from .item_service import ItemService

# 이 패키지에서 'from api.item.service import *' 구문을 사용할 때 외부에 공개할 이름들을 정의합니다.
# 여기서는 ItemService만 공개하도록 설정합니다.
__all__ = ['ItemService']