import streamlit as st
from openai import OpenAI
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama


# 파일 업로드를 위한 Streamlit 인터페이스
st.title("객체 인식 프로그램")
st.write("사진이나 PDF 파일을 업로드하세요.")

# OpenAI API 키 입력
api_key = st.text_input("OpenAI API 키를 입력하세요:", type="password")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("파일 선택", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    # 파일 타입에 따라 처리
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        st.image(uploaded_file, caption="업로드된 이미지", use_container_width=True)
        # 이미지 처리 로직 추가
        st.write("이미지 처리 중...")
        # 객체 인식 코드 추가
    elif uploaded_file.type == "application/pdf":
        st.write("PDF 파일 업로드됨.")
        # PDF 처리 로직 추가
        st.write("PDF 처리 중...")
        # 객체 인식 코드 추가

# 챗봇 인터페이스
st.write("챗봇과 대화해보세요.")
user_input = st.text_input("메시지를 입력하세요:")

if st.button("전송"):
    if user_input and api_key:
        # OpenAI API를 사용하여 응답 생성
        chat_openai = ChatOpenAI(model="gpt-4o-mini", openai_api_key=api_key)
        response = chat_openai.chat(messages=[{"role": "user", "content": user_input}])
        st.write("챗봇 응답:", response['content'])
    elif not api_key:
        st.warning("API 키를 입력해 주세요.")
