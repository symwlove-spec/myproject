import streamlit as st
import database as db

# 페이지 기본 설정
st.set_page_config(
    page_title="기계과 AIDT - 메인",
    page_icon="🏠",
    layout="wide"
)

# DB 초기화 (myproject.db 생성 및 테이블 준비)
db.init_db()

# Session State 초기화
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "userid" not in st.session_state:
    st.session_state["userid"] = ""

# ---------------------------------------------------------
# Sidebar: 로그인 및 회원가입 시스템
# ---------------------------------------------------------
st.sidebar.title("🔐 사용자 인증 시스템")

if st.session_state["logged_in"]:
    st.sidebar.success(f"**{st.session_state['userid']}**님 환영합니다!")
    if st.sidebar.button("로그아웃", use_container_width=True):
        st.session_state["logged_in"] = False
        st.session_state["userid"] = ""
        st.rerun()
else:
    auth_mode = st.sidebar.radio("서비스 선택", ["로그인", "회원가입"])
    
    if auth_mode == "로그인":
        st.sidebar.subheader("🔑 로그인")
        login_id = st.sidebar.text_input("아이디(ID)", key="login_id")
        login_pw = st.sidebar.text_input("비밀번호", type="password", key="login_pw")
        
        if st.sidebar.button("로그인", use_container_width=True):
            if db.login_user(login_id, login_pw):
                st.session_state["logged_in"] = True
                st.session_state["userid"] = login_id
                st.sidebar.success("로그인 성공!")
                st.rerun()
            else:
                st.sidebar.error("아이디 또는 비밀번호가 올바르지 않습니다.")
                
    elif auth_mode == "회원가입":
        st.sidebar.subheader("📝 회원가입")
        new_id = st.sidebar.text_input("신규 아이디(ID)", key="new_id")
        new_pw = st.sidebar.text_input("비밀번호", type="password", key="new_pw")
        new_pw_chk = st.sidebar.text_input("비밀번호 확인", type="password", key="new_pw_chk")
        
        if st.sidebar.button("회원가입 완료", use_container_width=True):
            if not new_id or not new_pw:
                st.sidebar.warning("아이디와 비밀번호를 모두 입력해주세요.")
            elif new_pw != new_pw_chk:
                st.sidebar.error("비밀번호가 일치하지 않습니다.")
            else:
                success, msg = db.register_user(new_id, new_pw)
                if success:
                    st.sidebar.success(msg)
                else:
                    st.sidebar.error(msg)

st.sidebar.divider()
st.sidebar.info("💡 형성평가는 로그인 후 응시하실 수 있습니다.")

# ---------------------------------------------------------
# Main Contents (기존 코드 유지 및 확장)
# ---------------------------------------------------------
st.title('This is my first webapp!!')
st.subheader('기계과 AIDT')

# 1차시
col1, col2 = st.columns((4, 1))
with col1:
    with st.expander('1차시_ 동영상'):
        st.title('동영상 시청......')
        url = 'https://www.youtube.com/watch?v=jPs3n9Vou9c&t=219s'
        st.video(url)
with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')
        imgpath = 'https://i.ytimg.com/vi/MP8R6kBykzE/hqdefault.jpg'
        st.image(imgpath)
        st.write('This is a term....')

# 2차시
col11, col12 = st.columns((4, 1))
with col11:
    with st.expander('2차시_ 동영상'):
        st.title('동영상 시청......')
        imgpath1 = './img/이미지.jpg'
        try:
            st.image(imgpath1)
        except:
            st.info("이미지를 찾을 수 없습니다. (경로: ./img/이미지.jpg)")

with col12:
    with st.expander('Tips...'):
        st.subheader('Tips...')
        imgpath = 'https://i.ytimg.com/vi/MP8R6kBykzE/hqdefault.jpg'
        st.image(imgpath)
        st.write('This is a term....')

# 3차시
colll1, colll2 = st.columns((4, 1))
with colll1:
    with st.expander('3차시_ 동영상'):
        st.title('머신러닝의 개념')
        st.markdown("""
        ### 📌 머신러닝(Machine Learning)이란?
        * **정의**: 사람이 직접 규칙을 프로그래밍하지 않고, **데이터를 학습하여 스스로 패턴과 규칙을 찾아내는** 인공지능 기술
        * **핵심 원리**: `입력 데이터` + `정답/결과` ➔ **[머신러닝]** ➔ `규칙(모델) 생성`

        ---

        ### 💡 핵심 특성 및 필요성
        * **자동화된 특징 추출**: 복잡한 패턴이나 대용량 데이터에서 유용한 정보 추출
        * **유연성 및 확장성**: 새로운 데이터가 입력되면 지속적으로 성능 개선
        * **기존 방식과의 차이**:
          * *전통적 프로그래밍*: 데이터 + 규칙 ➔ 결과
          * *머신러닝*: 데이터 + 결과 ➔ 규칙

        ---

        ### ⚙️ 학습 프로세스 4단계
        1. **데이터 수집 및 전처리**: 결측치 처리 및 데이터 정제
        2. **모델선택 및 학습**: 문제 유형에 맞는 알고리즘 적용
        3. **모델 평가**: 예측 정확도 및 성능 검증
        4. **예측 및 활용**: 실전 데이터 투입 후 결과 도출
        """)

with colll2:
    with st.expander('Tips...'):
        st.subheader('Tips...')
        st.markdown("""
        **🔍 머신러닝 주요 분류**

        * **지도학습 (Supervised)**
          * 정답(Label) 포함
          * 분류(Class), 회귀(Value)
        
        * **비지도학습 (Unsupervised)**
          * 정답 없음
          * 군집화(Clustering), 차원축소
        
        * **강화학습 (Reinforcement)**
          * 보상(Reward) 기반 학습
          * 시행착오를 통한 최적화
        
        ---
        💡 *Tip: 데이터의 정답 유무에 따라 학습 방식을 선택하세요!*
        """)