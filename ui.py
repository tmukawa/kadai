import streamlit as st
import requests

# APIのエンドポイント
API_URL = "http://127.0.0.1:8000/analyze/"

st.title("AI 画像分析 UI")
st.write("入力した画像のパスを分析して、画像が所属するクラスを出力します。")

# 画像パスの入力
image_path = st.text_input("画像のパスを入力してください", "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg")

# 送信ボタン
if st.button("分析を実行"):
    if not image_path:
        st.warning("画像パスを入力してください。")
    else:
        try:
            # APIにリクエストを送信
            response = requests.post(API_URL, json={"image_path": image_path})
            response.raise_for_status()
            result = response.json()

            if result.get("data", {}).get("success", False):
                st.success("分析成功！")
                estimated_data = result["data"].get("estimated_data", {})
                st.subheader("画像が所属するクラス")
                st.write(f"Class: {estimated_data.get('class', 'なし')}")
            else:
                st.error("分析失敗！")
                error_message = result.get("data", {}).get("message", "不明なエラー")
                st.error(error_message)

            st.subheader("解析結果 (JSON)")
            st.json(result)

        except requests.exceptions.RequestException as e:
            st.error("サーバーに接続できませんでした。")
            st.error(str(e))
        except ValueError:
            st.error("サーバーからのレスポンスが不正な形式です。")