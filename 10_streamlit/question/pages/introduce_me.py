import streamlit as st
from streamlit_extras.let_it_rain import *
import requests
import time
import random

st.title(':gray[나의 프로필 페이지] 🫧')
st.write(':gray[안녕하세요, 저는 skn 34기 김현지입니다.]')

st.divider()
st.header(':gray[기본 정보]')
st.subheader(':gray[이름 / 닉네임]')
n = "현지"
nk = "면지"
st.write(f'이름은 {n}')
st.write(f'별명은 {nk}')

st.divider()
st.header(':gray[취미]')
h1 = "영화 / 드라마 정주행"
h2 = "음악 감상"
st.write(f'{h1},  {h2} 등 ...')

st.divider()
st.header(':gray[오늘의 상태]')
s = "피곤 😵‍💫"
st.write(s)

st.divider()
st.header(':gray[소개 정리] 🐚')
col1, col2 = st.columns([2, 3])
with col1:
    st.write(f':gray[**이름**: {n}]')
    st.write(f':gray[**별명**: {nk}]')
with col2:
    st.write(f':gray[**취미**: {h1}, {h2}]')
    st.write(f':gray[**상태**: {s}]')

st.divider()
mood = st.select_slider('오늘의 기분', options=['😫', '☹️', '😐', '🙂', '☺️'])

today = st.text_input('한 줄 다짐-!', placeholder='문장을 적어주세요')
if today:
    st.write(f"오늘의 다짐은,  '{today}'")


st.divider()
q = st.selectbox("제가 vs code pet에 넣지 않은 동물을 골라보시겠어요 ..?", 
                 ["고양이", "강아지", "토끼", "여우"], 
                 index=None, placeholder="동물을 선택하세요")
if q is not None:
    st.write(f"선택한 동물: {q}")
    # with st.spinner('😺'):
    #     time.sleep(1)
    # with st.spinner('🐰'):
    #         time.sleep(1)
    # with st.spinner('🦊'):
            # time.sleep(1)
    #status 로 구현해야 ..
    if q == "강아지":
        st.success('정답입니다-!', icon="✅")
    else:
        st.error('답은 강아지입니다. 저는 고양이, 토끼, 여우를 추가했어요 😺🐰🦊', icon="❌")

st.write('\n\n')

choice = st.radio("당신이 선호하는 색상을 선택해주세요", ["검정", "하양", "초록", "파랑"], index=None)
st.write(f"선택된 색상: {choice}")
if choice is not None:
    st.info('제가 좋아하는 색은 연한 초록색 .. 세이지 그린입니다.', icon="ℹ️")

st.write('\n')

if 'bg_color' not in st.session_state:
    st.session_state.bg_color = None

with st.popover("🖱️ 클릭"):
    st.write("좋아하는 색 고르기 🎨")
    color = st.color_picker("좋아하는 색상을 골라보세요")
    if st.button("확정하기-!"):
        st.session_state.bg_color = color

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
        transition: background-color 0.5s ease;    # 색상이 부드럽게 바뀌는 효과
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 날씨
# st.divider()

# API_KEY = 'di2vMgW5lfdBFNZCP7oz7F%2F9GysZVRQP%2BC3oN2k7LFnOev4hX6V%2B8puiBrry4qRUf0McfIl4IA3fNwmDuiq7iw%3D%3D'

# nx = 
# yx = 


rain(
    emoji="☁️",
    font_size=45,
    falling_speed=5,
    animation_length=1,
)

st.write("점심메뉴 추천")
if st.button("추첨기"):
    with st.spinner("😺"):
        time.sleep(3)
        menu = ['한식', '중식', '일식']
        r = random.choice(menu)
    st.write(f'추천 메뉴는 {r}입니다-!')
