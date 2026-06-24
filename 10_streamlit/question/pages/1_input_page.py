import streamlit as st

st.title('사용자 입력 받는 페이지')

col1, col2 = st.columns(2)
with col1:
    name = st.text_input('닉네임 입력')

    age = st.number_input('나이 입력', min_value=13, max_value=100)

    nat = st.selectbox('국적을 선택하세요', ['한국', '중국', '일본', '미국', '외계'])

    hob = st.radio('취미를 선택하세요', ['맛집 탐방', '영화 감상', '음악 감상', '뜨개질'])

    agr = st.checkbox('개인정보 제공 동의')

with col2:
    butt1 = st.button('✅ 입력 완료')
    if butt1:
        st.write(f'이름이 뭐야? {name}')
        st.write(f'몇 살이야? {age}')
        st.write(f'어디서 왔어? {nat}')
        st.write(f'취미가 뭐야? {hob}')
        st.write(f'개인정보 제공에 동의해? {agr}')