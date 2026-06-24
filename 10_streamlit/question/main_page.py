import streamlit as st

st.title('오늘은 수요일')
st.header('오늘은 streamlit 배우는 날 🔥🔥🔥')
st.subheader('streamlit으로 나만의 데모 페이지 만들기-!!')

site = st.text_input('오늘 내가 만들어보고 싶은 사이트는?!')
st.write(f'{site}')

butt = st.button(f'{site} 접속하기')
if butt:
    st.write(f'{site} 접속 중!!!!! 🚀🚀🚀')

