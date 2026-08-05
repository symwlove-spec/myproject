import streamlit as st
import pandas as pd
import database as db

st.set_page_config(page_title="머신러닝 형성평가", page_icon="📝", layout="wide")

# DB 테이블 초기화
db.init_db()

st.title("📝 머신러닝 개념 형성평가")
st.caption("10문항의 5지 선다형 평가를 통해 학습 내용을 점검해보세요. (다회 응시 가능)")

# 로그인 체크
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ 형성평가에 응시하려면 먼저 로그인해주세요.")
    st.info("메인 페이지(`app.py`)에서 회원가입 및 로그인을 진행할 수 있습니다.")
    st.stop()

userid = st.session_state["userid"]
st.success(f"👤 현재 응시자: **{userid}**님")

# 형성평가 10문항 데이터 정의
questions = [
    {
        "id": 1,
        "question": "다음 중 머신러닝(Machine Learning)의 기본 정의로 가장 적절한 것은?",
        "options": [
            "① 사람이 작성한 모든 정교한 규칙 조건문을 그대로 실행하는 프로그램",
            "② 컴퓨터가 데이터를 학습하여 스스로 패턴과 규칙을 찾아내는 기술",
            "③ 데이터베이스에서 SQL을 이용해 데이터를 빠르게 검색하는 기술",
            "④ 컴퓨터 하드웨어의 처리 속도를 물리적으로 향상시키는 방법",
            "⑤ 웹 페이지의 레이아웃을 자동으로 정렬해주는 알고리즘"
        ],
        "answer": 2,
        "hint": "전통적 프로그래밍은 '규칙'을 사람이 입력하지만, 머신러닝은 데이터로부터 '규칙'을 찾아냅니다."
    },
    {
        "id": 2,
        "question": "전통적 프로그래밍과 머신러닝의 구조적 차이점에 대한 설명으로 옳은 것은?",
        "options": [
            "① 전통적 프로그래밍: 데이터 + 결과 ➔ 규칙 생성",
            "② 전통적 프로그래밍: 정답이 없으면 작동할 수 없음",
            "③ 머신러닝: 데이터 + 규칙 ➔ 결과 도출",
            "④ 머신러닝: 데이터 + 결과 ➔ 규칙(모델) 생성",
            "⑤ 두 방식 모두 정답(Label)을 반드시 사전에 요구함"
        ],
        "answer": 4,
        "hint": "머신러닝은 데이터와 결과를 바탕으로 패턴(규칙)을 스스로 도출합니다."
    },
    {
        "id": 3,
        "question": "데이터에 정답(Label)이 포함되어 있을 때 활용하는 머신러닝 학습 방식은?",
        "options": [
            "① 비지도학습(Unsupervised Learning)",
            "② 지도학습(Supervised Learning)",
            "③ 강화학습(Reinforcement Learning)",
            "④ 자기지도학습(Self-supervised Learning)",
            "⑤ 군집화(Clustering)"
        ],
        "answer": 2,
        "hint": "선생님이 정답을 알려주며 가르치는 방식과 비슷합니다."
    },
    {
        "id": 4,
        "question": "다음 중 지도학습(Supervised Learning)의 주요 문제 유형으로 짝지어진 것은?",
        "options": [
            "① 군집화(Clustering), 차원 축소",
            "② 분류(Classification), 회귀(Regression)",
            "③ 이상 탐지(Anomaly Detection), 보상 최적화",
            "④ 연관 규칙 분석, 군집화",
            "⑤ 에이전트 정책 수립, 회귀"
        ],
        "answer": 2,
        "hint": "이메일 스팸 분류(범주형) 및 주가 예측(연속형 값) 등이 대표적입니다."
    },
    {
        "id": 5,
        "question": "정답(Label)이 없는 데이터 내부의 숨겨진 구조나 패턴을 탐색하는 학습 방식은?",
        "options": [
            "① 지도학습",
            "② 비지도학습",
            "③ 강화학습",
            "④ 전이학습",
            "⑤ 앙상블 학습"
        ],
        "answer": 2,
        "hint": "라벨이 없는 데이터들을 유사한 것끼리 묶거나 구조를 파악합니다."
    },
    {
        "id": 6,
        "question": "에이전트가 환경과 상호작용하며 '보상(Reward)'을 최대화하는 방향으로 학습하는 방식은?",
        "options": [
            "① 지도학습",
            "② 비지도학습",
            "③ 강화학습",
            "④ 회귀분석",
            "⑤ 분류분석"
        ],
        "answer": 3,
        "hint": "알파고나 자율주행, 로봇 제어 등에 주로 활용됩니다."
    },
    {
        "id": 7,
        "question": "고객 구매 데이터를 바탕으로 유사한 특성을 가진 고객 그룹을 묶는 '군집화(Clustering)'는 어떤 학습에 해당하는가?",
        "options": [
            "① 지도학습",
            "② 비지도학습",
            "③ 강화학습",
            "④ 지도/강화 혼합학습",
            "⑤ 생성적 대립 학습"
        ],
        "answer": 2,
        "hint": "미리 정해진 고객 등급 정답이 없이 데이터 간 유사도로 그룹화합니다."
    },
    {
        "id": 8,
        "question": "머신러닝 프로세스의 일반적인 4단계 순서로 올바른 것은?",
        "options": [
            "① 모델 평가 ➔ 데이터 수집 및 전처리 ➔ 예측 및 활용 ➔ 모델 선택 및 학습",
            "② 데이터 수집 및 전처리 ➔ 모델 선택 및 학습 ➔ 모델 평가 ➔ 예측 및 활용",
            "③ 모델 선택 및 학습 ➔ 데이터 수집 및 전처리 ➔ 모델 평가 ➔ 예측 및 활용",
            "④ 데이터 수집 및 전처리 ➔ 예측 및 활용 ➔ 모델 평가 ➔ 모델 선택 및 학습",
            "⑤ 모델 평가 ➔ 모델 선택 및 학습 ➔ 데이터 수집 및 전처리 ➔ 예측 및 활용"
        ],
        "answer": 2,
        "hint": "데이터 수집 ➔ 학습 ➔ 검증 ➔ 실전 활용 순서입니다."
    },
    {
        "id": 9,
        "question": "다음 중 연속적인 숫자 값(예: 아파트 가격, 내일의 기온)을 예측하는 머신러닝 문제는?",
        "options": [
            "① 분류 (Classification)",
            "② 회귀 (Regression)",
            "③ 군집화 (Clustering)",
            "④ 차원 축소 (Dimensionality Reduction)",
            "⑤ 이상 탐지 (Anomaly Detection)"
        ],
        "answer": 2,
        "hint": "범주가 아닌 연속적인 수치를 예측할 때 사용합니다."
    },
    {
        "id": 10,
        "question": "학습된 머신러닝 모델의 성능을 제대로 평가하기 위한 올바른 방법은?",
        "options": [
            "① 학습에 사용했던 데이터 그대로 평가한다.",
            "② 학습에 사용하지 않은 별도의 테스트(검증) 데이터를 활용하여 평가한다.",
            "③ 정답(Label)을 모두 제거하고 눈으로 확인한다.",
            "④ 파라미터 조절 없이 한 번의 학습으로 항상 완벽하다고 가정한다.",
            "⑤ 데이터 전처리 과정을 생략해야만 정확하게 평가된다."
        ],
        "answer": 2,
        "hint": "과적합(Overfitting)을 방지하고 일반화 성능을 보려면 평가용 데이터를 분리해야 합니다."
    }
]

# 폼 생성
with st.form("quiz_form"):
    user_responses = []
    
    for idx, q in enumerate(questions):
        st.markdown(f"#### Q{q['id']}. {q['question']}")
        
        # 힌트 및 정답 확장 영역
        col_hint, col_ans = st.columns(2)
        with col_hint:
            with st.expander(f"💡 Q{q['id']} 힌트 보기"):
                st.info(q["hint"])
        with col_ans:
            with st.expander(f"🔒 Q{q['id']} 정답 숨김/보기"):
                st.success(f"정답: {q['options'][q['answer'] - 1]}")
                
        # 5지 선다 선택 라디오 버튼
        choice = st.radio(
            f"Q{q['id']} 답변을 선택하세요:",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: q["options"][x-1],
            key=f"q_{q['id']}",
            index=None
        )
        user_responses.append(choice)
        st.divider()

    submit_button = st.form_submit_button("📤 형성평가 제출하기", use_container_width=True)

# 제출 처리
if submit_button:
    if None in user_responses:
        st.error("⚠️ 미응답 문항이 있습니다. 모든 문항에 답변을 선택한 후 제출해주세요.")
    else:
        score = 0
        user_answers = []
        for i, resp in enumerate(user_responses):
            user_answers.append(resp)
            if resp == questions[i]["answer"]:
                score += 10
                
        # DB 저장
        db.save_quiz_result(userid, user_answers, score)
        
        st.balloons()
        st.success(f"🎉 평가 제출 완료! **{userid}**님의 최종 점수: **{score}점 / 100점**")

st.divider()

# 응시 이력 확인
st.subheader("📊 나의 형성평가 응시 이력")
history_rows = db.get_user_history(userid)

if history_rows:
    history_data = []
    for row in history_rows:
        row_dict = dict(row)
        history_data.append({
            "응시 일시": row_dict["created_at"],
            "점수": f"{row_dict['score']}점",
            "Q1": row_dict["m1"], "Q2": row_dict["m2"], "Q3": row_dict["m3"],
            "Q4": row_dict["m4"], "Q5": row_dict["m5"], "Q6": row_dict["m6"],
            "Q7": row_dict["m7"], "Q8": row_dict["m8"], "Q9": row_dict["m9"], "Q10": row_dict["m10"]
        })
    df_history = pd.DataFrame(history_data)
    st.dataframe(df_history, use_container_width=True)
else:
    st.info("아직 응시한 이력이 없습니다.")