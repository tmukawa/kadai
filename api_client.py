import requests
import os
from datetime import datetime, timezone

# モックAPIのエンドポイント
MOCK_API_URL = "http://127.0.0.1:8001/"

def send_request(image_path):
    """ モックAPIに画像ファイルPathを指定してリクエストを送信 """
    
    # モックAPIへPOSTリクエストを送信
    response = requests.post(MOCK_API_URL, json={"image_path": image_path})
    
    # ステータスが200であればレスポンスを返し、それ以外はError
    if response.status_code == 200:
        return response.json(), datetime.now(timezone.utc)
    else:
        return {"success": False, "message": "API Error", "estimated_data": {}}, datetime.now(timezone.utc)