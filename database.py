from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone

# SQLiteのデータベースURL設定
DATABASE_URL = "sqlite:///./ai_analysis.db"

# SQLAlchemyのエンジン作成
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# データベースのテーブル定義
class AIAnalysisLog(Base):
    __tablename__ = "ai_analysis_log"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_path = Column(String(255), nullable=False) # 画像のパス
    success = Column(Boolean, nullable=False) # 成功/失敗フラグ
    message = Column(String(255), nullable=False) # APIのメッセージ
    class_label = Column(Integer, nullable=True) # 画像の所属クラス
    confidence = Column(DECIMAL(5,4), nullable=True)
    request_timestamp = Column(DateTime, nullable=True) # リクエスト時刻
    response_timestamp = Column(DateTime, nullable=True) # 応答時刻

# テーブルが存在しなければ自動作成
def init_db():
    Base.metadata.create_all(bind=engine)

# DBセッションを取得
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()