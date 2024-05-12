import streamlit as st
from PIL import Image


# 홈 페이지의 타이틀 설정
st.title('🛠 도덕 도구 모음')

# 애플리케이션 소개
st.markdown("""
    ## 🌟 안녕하세요!
    이 애플리케이션은 학생 자치활동에 필요한 여러 가지 유용한 도구들로 구성되어 있습니다. 아래는 제작된 도구들의 리스트와 기능 설명입니다.
""")

# 컬럼으로 레이아웃 구성
col1 st.columns(1)

with col1:
    st.subheader('1. 생각 톡톡 AI')
    st.write('이 도구를 사용하면, 여러분이 배워야 할 도덕적 덕목에 대해서 잘 알 수 있습니다.')
    st.write('이렇게 질문하세요. 예) 정의로운 삶은 뜻은?')
    
    # 이미지 삽입
    image_path = 'https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/xSO/image/LlSElL_exe7lc0mLeGSxBr4EZjg.png'  # 로컬 파일 경로 또는 URL
    st.image(image_path, caption='도덕 교육 이미지')  # 이미지에 설명 추가
    
    link_url = 'https://www.naver.com/'  # 이미지를 클릭했을 때 이동할 링크
    st.markdown(f'<a href="{link_url}" target="_blank"><img src="{image_path}" alt="도덕 교육 이미지" style="width:100%;"></a>', unsafe_allow_html=True)


col2 = st.columns(1)

with col2:
    st.subheader('2.마음톡톡 AI')
    st.write('도덕적 딜레마상황에 대해서 생각해 보고 어떤 선택기 옮은 것인지 생각해 볼 수 있습니다.'
    image_path = 'https://postfiles.pstatic.net/MjAyNDA1MTNfMjQz/MDAxNzE1NTM5ODc2OTY3.8AWJDUJhCOJe2ycZlMbIUy2tm38ZKIhOywDeYMHcMDMg.Robn_xaq42P3a3iLkvXvS_EaUP_tFJr2OMEawP1hA7gg.JPEG/DALL%C2%B7E_2024-05-13_03.50.30_-_A_colorful_illustration_showing_a_group_of_dive.jpg?type=w773'
    st.image(image_path, caption='도덕 교육 이미지')  # 이미지에 설명 추가 


col2 = st.columns(1)

with col2:
    st.subheader('3.실천톡톡 AI')
    st.write('텍스트 설명을 바탕으로 이미지를 생성합니다.')
    st.markdown('**주의:** 이미지 생성요청이 한번에 몰릴 경우 이미지생성오류가 있을 수 있습니다.')
    image_path = 'https://postfiles.pstatic.net/MjAyNDA1MTNfMjQz/MDAxNzE1NTM5ODc2OTY3.8AWJDUJhCOJe2ycZlMbIUy2tm38ZKIhOywDeYMHcMDMg.Robn_xaq42P3a3iLkvXvS_EaUP_tFJr2OMEawP1hA7gg.JPEG/DALL%C2%B7E_2024-05-13_03.50.30_-_A_colorful_illustration_showing_a_group_of_dive.jpg?type=w773'
    st.image(image_path, caption='도덕 교육 이미지')  # 이미지에 설명 추가 

# 추가적인 정보 제공
st.markdown("""
    ## 🚀 시작하기
    왼쪽의 탐색 바(> 클릭)를 사용하여 원하는 도구를 선택하고 사용해 보세요. 각 도구는 사용자의 입력에 따라 다양한 결과를 제공합니다.
""")

