import streamlit as st

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title('천안공고 기계학습방에 온걸 환영해')
import streamlit as st

# 소제목 출력
st.subheader('기계과 AIDT')

# 화면을 4:1 비율로 분할
col1, col2 = st.columns([4, 1])

# 왼쪽 넓은 영역 (비율 4)
with col1:
    with st.expander('1차시_ 끼워맞춤 동영상'):
        st.title('동영상 시청......')

# 오른쪽 좁은 영역 (비율 1)
with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')
        st.write('This is a term....')