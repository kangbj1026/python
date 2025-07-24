# api/item/entity/item_entity.py
# 이 파일은 데이터베이스 테이블과 매핑되는 'Item' 엔티티(모델)를 정의합니다.
# SQLAlchemy의 ORM 기능을 사용하여 파이썬 객체와 데이터베이스 레코드 간의 매핑을 설정합니다.

# database.py에서 정의된 db 객체를 임포트합니다.
# 이 db 객체는 SQLAlchemy 인스턴스이며, 모델 정의에 사용됩니다.
from database import db

# Item 클래스는 db.Model을 상속받아 SQLAlchemy 모델임을 나타냅니다.
class Item(db.Model):
    # __tablename__ 속성은 이 모델이 매핑될 데이터베이스 테이블의 이름을 지정합니다.
    __tablename__ = 'items' 

    # id 컬럼: 정수형, 기본 키(Primary Key)로 설정됩니다.
    # primary_key=True는 이 컬럼이 테이블의 기본 키임을 의미하며, 자동으로 증가(auto-increment)합니다.
    id = db.Column(db.Integer, primary_key=True)
    # name 컬럼: 최대 80자 길이의 문자열, Null을 허용하지 않습니다.
    name = db.Column(db.String(80), nullable=False)
    # description 컬럼: 최대 200자 길이의 문자열, Null을 허용합니다.
    description = db.Column(db.String(200), nullable=True)

    # 객체를 문자열로 표현할 때 사용되는 메서드입니다.
    # 디버깅 시 유용하며, 객체의 이름(name)을 포함하여 출력합니다.
    def __repr__(self):
        return f'<Item {self.name}>'

    # Item 객체를 딕셔너리 형태로 변환하는 메서드입니다.
    # API 응답으로 JSON 데이터를 반환할 때 유용하게 사용됩니다.
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
