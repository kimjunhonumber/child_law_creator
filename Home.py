import streamlit as st
from PIL import Image

# 홈 페이지의 타이틀 설정
st.title('🛠 도덕 AI')
# 애플리케이션 소개
st.markdown("""
## 🌟 안녕하세요!
이 앱은 미덕과 관련한 학습을 하기 위해서 제작되어 있습니다. 
""")
# 컬럼으로 레이아웃 구성
col1, col2 =st.columns(2)
with col1:
    st.subheader('1. 마음AI)
    st.write('이 도구를 사용하면, 마음에 대해 알 수 있습니다.')
    Image_path = 'https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/xSO/image/LlSElL_exe7lc0mLeGSxBr4EZjg.png'  # 로컬 파일 경로 또는 URL
    st.image(image_path, caption='도덕 교육 이미지')  # 이미지에 설명 추가
with col2:
    st.subheader()
    st.write()
col3, col4 =st.columns(2)
with col3:
    st.subheader('2. 생각AI')
    st.write('도덕적 생각을 하는 AI봇입니다.')
    st.write('도덕적 생각을 하는 AI봇입니다.')
    image_path = 'https://postfiles.pstatic.net/MjAyNDA1MTNfMjQz/MDAxNzE1NTM5ODc2OTY3.8AWJDUJhCOJe2ycZlMbIUy2tm38ZKIhOywDeYMHcMDMg.Robn_xaq42P3a3iLkvXvS_EaUP_tFJr2OMEawP1hA7gg.JPEG/DALL%C2%B7E_2024-05-13_03.50.30_-_A_colorful_illustration_showing_a_group_of_dive.jpg?type=w773'
    st.image(image_path, caption='도덕 교육 이미지')  # 이미지에 설명 추가 

with col4:
    st.subheader('3. 실천AI')
    st.write('실천을 하는 AI봇입니다.')
    st.markdown('')
# 추가적인 정보 제공
st.markdown("""
## 🚀 시작하기
왼쪽의 탐색 바(> 클릭)를 사용하여 원하는 도구를 선택하고 사용해 보세요. 각 도구는 사용자의 입력에 따라 다양한 결과를 제공합니다.
""")


