import streamlit as st
import streamlit.components.v1 as components

# HTML 파일 경로
html_file_path = 'lda_positive (1).html'

# HTML 파일 읽기
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Streamlit 애플리케이션
st.title("LDA 긍정 토픽 모델링 결과")

# HTML 콘텐츠 삽입
components.html(html_content, height=1000, width=1200, scrolling=True)