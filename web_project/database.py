# database.py
# 이 파일은 SQLAlchemy 데이터베이스 인스턴스를 초기화하고 다른 모듈에서 사용할 수 있도록 제공합니다.
# 이렇게 분리함으로써 애플리케이션의 다른 부분에서 데이터베이스 객체를 쉽게 임포트하여 사용할 수 있습니다.

from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 인스턴스를 생성합니다.
# 이 인스턴스는 Flask 애플리케이션과 연결될 때(app.py에서 db.init_app(app) 호출 시) 초기화됩니다.
db = SQLAlchemy()