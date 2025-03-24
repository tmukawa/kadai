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
.
