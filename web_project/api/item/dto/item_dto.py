# api/item/dto/item_dto.py
# 이 파일은 데이터 전송 객체(DTO: Data Transfer Object)를 정의합니다.
# DTO는 계층 간 데이터 전송을 위해 사용되며, 주로 API 요청/응답의 데이터 구조를 명확히 합니다.
# dataclasses 모듈을 사용하여 간결하게 DTO 클래스를 정의합니다.

from dataclasses import dataclass

# ItemCreateDTO 클래스
# 새로운 아이템을 생성할 때 클라이언트로부터 받는 데이터를 정의합니다.
@dataclass
class ItemCreateDTO:
    # 아이템의 이름 (필수 필드)
    name: str
    # 아이템의 설명 (선택 필드, 기본값은 빈 문자열)
    description: str = ""

# ItemUpdateDTO 클래스
# 기존 아이템을 업데이트할 때 클라이언트로부터 받는 데이터를 정의합니다.
# 모든 필드는 선택 사항이며, 제공되지 않은 필드는 업데이트되지 않습니다.
@dataclass
class ItemUpdateDTO:
    # 아이템의 이름 (선택 필드, 기본값은 None)
    name: str = None
    # 아이템의 설명 (선택 필드, 기본값은 None)
    description: str = None