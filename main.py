from pydantic import BaseModel
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import init_db, get_db, AIAnalysisLog
from api_client import send_request
from datetime import datetime
from zoneinfo import ZoneInfo
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # アプリケーションの起動時にDB初期化
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# 画像ファイルPathを受け取ってバリデーションチェック
class ImageRequest(BaseModel):
    image_path: str

@app.post("/analyze/")
def analyze_image(request: ImageRequest, db: Session = Depends(get_db)):
    """画像ファイルPathを受け取ってモックAPIで解析し、結果をDBに保存するAPI"""
    
    request_timestamp=datetime.now(ZoneInfo("Asia/Tokyo"))
    
    # モックAPIの呼び出し
    response, response_timestamp = send_request(request.image_path)
    
    # データベース保存用ログデータの作成
    log_entry = AIAnalysisLog(
        image_path=request.image_path,
        success=response["success"],
        message=response["message"],
        class_label=response["estimated_data"].get("class"),
        confidence=response["estimated_data"].get("confidence"),
        request_timestamp=request_timestamp,
        response_timestamp=response_timestamp.astimezone(ZoneInfo("Asia/Tokyo"))
    )
    
    # データベースに保存
    db.add(log_entry)
    db.commit()

    return {"message": "Data saved successfully", "data": response}
    