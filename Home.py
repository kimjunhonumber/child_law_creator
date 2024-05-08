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
col1, col2 = st.columns(2)

with col1:
    st.subheader('1. 생각 톡톡 AI')
    st.write('이 도구를 사용하면, 여러분이 배워야 할 도덕적 덕목에 대해서 잘 알 수 있습니다.')
    st.write('이렇게 질문하세요. 예) 정의로운 삶은 뜻은?')
    
    # 이미지 삽입
    image_path = 'https://t1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/xSO/image/LlSElL_exe7lc0mLeGSxBr4EZjg.png'  # 로컬 파일 경로 또는 URL
    st.image(image_path, caption='도덕 교육 이미지')  # 이미지에 설명 추가
    
    link_url = 'https://www.naver.com/'  # 이미지를 클릭했을 때 이동할 링크
    st.markdown(f'<a href="{link_url}" target="_blank"><img src="{image_path}" alt="도덕 교육 이미지" style="width:100%;"></a>', unsafe_allow_html=True)




with col2:
    st.subheader('2. 발표문 생성 보조도구')
    st.write('발표 준비에 도움이 필요하신가요? 이 도구가 도와드립니다.')

col3, col4 = st.columns(2)

with col3:
    st.subheader('3. 안건 제안 보조 챗봇 & 보조도구')
    st.write('보조챗봇을 통해 법률안과 제안서에 대한 이해를 높일 수 있습니다. 챗봇과의 대화를 통해 아이디어를 만들어보세요.')
    st.write('보조도구를 통해 법률안을 만들 수 있습니다.')

with col4:
    st.subheader('4. 이미지 생성 보조도구')
    st.write('텍스트 설명을 바탕으로 이미지를 생성합니다.')
    st.markdown('**주의:** 이미지 생성요청이 한번에 몰릴 경우 이미지생성오류가 있을 수 있습니다.')

# 추가적인 정보 제공
st.markdown("""
    ## 🚀 시작하기
    왼쪽의 탐색 바(> 클릭)를 사용하여 원하는 도구를 선택하고 사용해 보세요. 각 도구는 사용자의 입력에 따라 다양한 결과를 제공합니다.
""")

st.markdown("""
    ## 비밀번호는 선생님에게 물어보세요.
""")
