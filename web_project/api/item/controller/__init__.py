# api/item/controller/__init__.py
# 이 파일은 'controller' 디렉토리가 파이썬 패키지임을 나타냅니다.
# 이 패키지 내의 item_controller.py에서 정의된 item_bp를 패키지 레벨로 노출하여
# 상위 패키지(api.item)에서 더 쉽게 임포트할 수 있도록 합니다.

# item_controller 모듈에서 item_bp Blueprint를 임포트합니다.
# .item_controller는 현재 패키지(controller) 내의 item_controller 모듈을 의미합니다.
from .item_controller import item_bp

# 이 패키지에서 'from api.item.controller import *' 구문을 사용할 때 외부에 공개할 이름들을 정의합니다.
# 여기서는 item_bp만 공개하도록 설정합니다.
__all__ = ['item_bp']