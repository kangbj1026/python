# api/item/__init__.py
# 이 파일은 'item' 디렉토리가 파이썬 패키지임을 나타냅니다.
# 또한, 이 패키지의 주요 Blueprint인 item_bp를 패키지 레벨에서 바로 임포트할 수 있도록 합니다.
# 이렇게 하면 'from api.item.controller.item_controller import item_bp' 대신
# 'from api.item import item_bp'와 같이 더 간결하게 임포트할 수 있습니다.

# item_controller 모듈에서 item_bp Blueprint를 임포트합니다.
# .controller는 현재 패키지(item) 내의 controller 서브패키지를 의미합니다.
from .controller import item_bp

# 이 패키지에서 'from api.item import *' 구문을 사용할 때 외부에 공개할 이름들을 정의합니다.
# 여기서는 item_bp만 공개하도록 설정하여 패키지의 API를 명확하게 합니다.
__all__ = ['item_bp']
