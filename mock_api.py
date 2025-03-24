from fastapi import FastAPI
from pydantic import BaseModel
import random
import time

app = FastAPI()

class ImageRequest(BaseModel):
    image_path: str

@app.post("/")
def analyze_image(request: ImageRequest):
    """ モックAPI: 画像ファイルPathを受け取って擬似的なレスポンスを返す """
    image_path = request.image_path

    # 画像ファイルPathにerror文字列が含まれている場合または20%の確率でエラーを発生させる
    # time.sleep(3)
    if "error" in image_path or random.random() < 0.2:
        return {"success": False, "message": "Error:E50012", "estimated_data": {}}
    else:
        return {
            "success": True,
            "message": "success",
            "estimated_data": {
                "class": random.randint(1, 10),
                "confidence": round(random.uniform(0.5, 1.0), 4)
            }
        }