# api/item/dto/__init__.py
# 이 파일은 'dto' 디렉토리가 파이썬 패키지임을 나타냅니다.
# 이 패키지 내의 item_dto.py에서 정의된 DTO 클래스들을 패키지 레벨로 노출하여
# 상위 패키지(api.item)나 다른 계층에서 더 쉽게 임포트할 수 있도록 합니다.

# item_dto 모듈에서 ItemCreateDTO와 ItemUpdateDTO 클래스를 임포트합니다.
# .item_dto는 현재 패키지(dto) 내의 item_dto 모듈을 의미합니다.
from .item_dto import ItemCreateDTO, ItemUpdateDTO

# 이 패키지에서 'from api.item.dto import *' 구문을 사용할 때 외부에 공개할 이름들을 정의합니다.
# 여기서는 ItemCreateDTO와 ItemUpdateDTO만 공개하도록 설정합니다.
__all__ = ['ItemCreateDTO', 'ItemUpdateDTO']