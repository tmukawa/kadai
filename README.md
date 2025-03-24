## プロジェクト概要
本プロジェクトは、以下の構成要素で成り立っています。
- 指定された画像パスを受け取り、ランダムにClassを返すモックAPIを実装
- モックAPIのレスポンスをデータベースに保存
- 上記の画像パスの入力と結果を出力する簡易UIを実装

## ファイル構成
```
./project_root
│── database.py      # データベース定義
│── main.py          # APIサーバー（FastAPI）
│── mock_api.py      # モック画像分析API（FastAPI）
│── ui.py            # 簡易UI（Streamlit）
│── requirements.txt # 依存パッケージ一覧
└── ai_analysis.db   # SQLiteデータベース（APIサーバ起動時に自動生成）
```

## 環境情報
| 言語・フレームワーク | バージョン |
| -------------------- | ---------- |
| Python                | 3.13.1       |
| SQLite                | 3.43.2     |
| FastAPI           | 0.115.11     |
| Streamlit              | 1.43.2   |

※ その他の依存パッケージは'requirements.txt' を参照

## セットアップ
### 1. 必要なパッケージのインストール
```
pip install -r requirements.txt
```
### 2. APIサーバーの起動
データベースは API サーバー起動時に自動生成されるため、特別な初期化処理は不要です。
```
uvicorn main:app --reload
```
### 3. モックAPIの起動
```
uvicorn mock_api:app --host 127.0.0.1 --port 8001 --reload
```
### 4. 簡易UIの起動
```
streamlit run ui.py
```

## 動作確認
### curlを使う場合
API に対して curl コマンドを用いてリクエストを送信し、動作を確認できます。
リクエスト例:
```
curl -X 'POST' 'http://127.0.0.1:8000/analyze/' -H 'Content-Type: application/json' -d '{"image_path": "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"}'
```
成功時のレスポンス例:
```
{"message":"Data saved successfully","data":{"success":true,"message":"success","estimated_data":{"class":9,"confidence":0.9968}}}
```
失敗時のレスポンス例:
```
{"message":"Data saved successfully","data":{"success":false,"message":"Error:E50012","estimated_data":{}}}
```

### 簡易UIを使う場合
以下のコマンドを用いてUIを起動します。
```
streamlit run ui.py
```

画像パスをフィールドに入力し、[分析を実行]をクリックします
<img width="819" alt="Image" src="https://github.com/user-attachments/assets/67e3fa75-4915-4bb6-a615-6405552d3133" />
