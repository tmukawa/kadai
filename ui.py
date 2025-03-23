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
    if image_path:
        # APIにリクエストを送信
        response = requests.post(API_URL, json={"image_path": image_path})

        # 結果を表示
        if response.status_code == 200:
            result = response.json()
            
            # レスポンスのdataからsuccessフィールドをチェック
            if result.get("data", {}).get("success", False):  
                st.success("分析成功！")
                
                # class_labelの値を取得して表示
                estimated_data = result.get("data", {}).get("estimated_data", {})
                class_label = estimated_data.get("class", "なし")
                st.subheader("画像が所属するクラス")
                st.write(f"Class: {class_label}")

            else:
                st.error("分析失敗！")
                error_message = result.get("data", {}).get("message", result.get("message", "不明なエラー"))
                st.write(f"エラーメッセージ: {error_message}")

            # JSON全体を表示
            st.subheader("解析結果 (JSON)")
            st.json(result)

        else:
            st.error("サーバーエラーが発生しました。")
    else:
        st.warning("画像パスを入力してください。")