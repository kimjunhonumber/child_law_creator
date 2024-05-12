import streamlit as st

# 홈 페이지의 타이틀 설정
st.title('🛠 AI인공지능 도구 모음 홈페이지')

# 애플리케이션 소개
st.markdown("""
    ## 🌟 안녕하세요!
    이 애플리케이션은 학생들의 도덕 학습을 위해 제작된 챗봇입니다. 아래는 제작된 도구들의 리스트와 기능 설명입니다.
""")

# 컬럼으로 레이아웃 구성
col1, col2 = st.columns(2)

with col1:
    # 링크가 포함된 서브헤더와 이미지
    st.markdown('### [1. 마음AI](https://childlawcreator-qfu1xsx5rw.streamlit.app/%EB%A7%88%EC%9D%8CAI)')
    st.write('이 도구를 사용하면, 제안서를 쉽고 빠르게 작성할 수 있습니다.')
    # 이미지에 하이퍼링크 추가
    st.markdown("""
        <a href="https://childlawcreator-qfu1xsx5rw.streamlit.app/%EB%A7%88%EC%9D%8CAI">
            <img src="https://lh3.googleusercontent.com/proxy/UIggDZZrawXmiJPUmYyE-kMGFVEhWTLgIJwi58SOZSuP76LydbfSzGhVHDvcg4iuxAhL_1mtM7-voTXABICKwjPZmvSDoN_lM2_qi6R_GNo3szzC-ezWjA" width="100" height="100" alt="제안서 도구 이미지">
        </a>
    """, unsafe_allow_html=True)


with col2:
    st.subheader('2. 마음AI보조도구')
    st.write('마음AI보조도구')

col3, col4 = st.columns(2)

with col3:
    st.subheader('3. 생각AI')
    st.write('도덕과 관련된 딜레마상황을 판단할수 있습니다.')
    st.write('보조도구를 이용해 보세요.')

with col4:
    st.subheader('4. 실천AI')
    st.write('실천AI')
    st.markdown('**주의:** 이미지 생성요청이 한번에 몰릴 경우 이미지생성오류가 있을 수 있습니다.')

# 추가적인 정보 제공
st.markdown("""
    ## 🚀 시작하기
    왼쪽의 탐색 바(> 클릭)를 사용하여 원하는 도구를 선택하고 사용해 보세요. 각 도구는 사용자의 입력에 따라 다양한 결과를 제공합니다.
""")

st.markdown("""
    ## 비밀번호는 선생님에게 물어보세요.
""")

