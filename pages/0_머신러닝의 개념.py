#streamlit webapp의 pages 경로 밑에 서브 페이즈로 다음을 생성해주세요.
#머싱러닝의 개념에 대해 학습할 콘텐츠 생성
# 간단하게 머신러닝의 개념을 실습할 있는 시뮬레이터 포함(mock data를 생성해서 (분류데이터)직접 실습하도록 함 )
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 페이지 기본 설정
st.set_page_config(
    page_title="머신러닝의 개념",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------------
# Header & Intro Section
# ---------------------------------------------------------
st.title("🤖 머신러닝(Machine Learning)의 개념")
st.caption("기계가 데이터를 통해 학습하고 패턴을 찾아내는 핵심 원리를 알아봅니다.")

st.markdown("""
머신러닝은 명시적으로 프로그래밍을 하지 않고도, **컴퓨터가 데이터로부터 학습하여 스스로 예측이나 결정을 내리게 하는 기술**입니다.
""")

# ---------------------------------------------------------
# Section 1: ML Concept Explanation
# ---------------------------------------------------------
st.subheader("📌 머신러닝의 3가지 주요 유형")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎯 지도학습 (Supervised)
    * **정답(Label)이 있는 데이터**를 학습
    * 입력 데이터와 정답 간의 관계를 파악
    * **주요 문제:** 분류(Classification), 회귀(Regression)
    * *예시: 스팸 메일 분류, 주가 예측*
    """)

with col2:
    st.markdown("""
    ### 🔍 비지도학습 (Unsupervised)
    * **정답(Label)이 없는 데이터**를 학습
    * 데이터 내부의 숨겨진 구조나 패턴 탐색
    * **주요 문제:** 군집화(Clustering), 차원 축소
    * *예시: 고객 군집 분석, 이상 탐지*
    """)

with col3:
    st.markdown("""
    ### 🎮 강화학습 (Reinforcement)
    * 에이전트가 **환경과의 상호작용**을 통해 학습
    * 보상(Reward)을 최대화하는 방향으로 정책 수립
    * **주요 문제:** 의사결정 연속체
    * *예시: 자율주행, 알파고, 로봇 제어*
    """)

st.divider()

# ---------------------------------------------------------
# Section 2: Interactive ML Simulator (Classification)
# ---------------------------------------------------------
st.subheader("🧪 머신러닝 분류(Classification) 실습 시뮬레이터")
st.markdown("가상의 Mock Data를 생성하고, 머신러닝 모델을 직접 학습시켜 경계선(Decision Boundary)을 확인해보세요.")

# 사이드바/설정 영역
with st.sidebar:
    st.header("⚙️ 시뮬레이터 설정")
    
    st.subheader("1. Mock Data 생성")
    dataset_type = st.selectbox(
        "데이터 모양 선택",
        ["분리형 (Blobs)", "초승달형 (Moons)", "동심원 (Circles)"]
    )
    n_samples = st.slider("샘플 수 (Data Points)", 100, 500, 200, step=50)
    noise = st.slider("노이즈 (Noise Level)", 0.0, 0.5, 0.15, step=0.05)
    
    st.subheader("2. 머신러닝 알고리즘 선택")
    model_type = st.selectbox(
        "분류 모델 선택",
        ["K-최근접 이웃 (KNN)", "의사결정나무 (Decision Tree)"]
    )
    
    if model_type == "K-최근접 이웃 (KNN)":
        k_val = st.slider("이웃 수 (K)", 1, 15, 3)
    else:
        max_depth = st.slider("트리 최대 깊이 (Max Depth)", 1, 10, 3)

# Data Generation
if dataset_type == "분리형 (Blobs)":
    X, y = make_blobs(n_samples=n_samples, centers=2, cluster_std=1.0 + noise*2, random_state=42)
elif dataset_type == "초승달형 (Moons)":
    X, y = make_moons(n_samples=n_samples, noise=noise, random_state=42)
else:
    X, y = make_circles(n_samples=n_samples, noise=noise, factor=0.5, random_state=42)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
if model_type == "K-최근접 이웃 (KNN)":
    model = KNeighborsClassifier(n_neighbors=k_val)
else:
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

model.fit(X_train, y_train)
train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

# Create Decision Boundary Grid
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Layout for Visualization and Metrics
col_chart, col_metric = st.columns([3, 1])

with col_chart:
    # Plotly Visualization
    fig = go.Figure()

    # Decision Boundary Contour
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, 100),
        y=np.linspace(y_min, y_max, 100),
        z=Z,
        showscale=False,
        opacity=0.3,
        colorscale=['#636EFA', '#EF553B']
    ))

    # Scatter points
    df_plot = pd.DataFrame(X_train, columns=["Feature 1", "Feature 2"])
    df_plot["Class"] = y_train.astype(str)

    fig.add_trace(go.Scatter(
        x=df_plot[df_plot["Class"] == '0']["Feature 1"],
        y=df_plot[df_plot["Class"] == '0']["Feature 2"],
        mode='markers',
        name='클래스 0',
        marker=dict(color='#636EFA', size=8, line=dict(width=1, color='DarkSlateGrey'))
    ))

    fig.add_trace(go.Scatter(
        x=df_plot[df_plot["Class"] == '1']["Feature 1"],
        y=df_plot[df_plot["Class"] == '1']["Feature 2"],
        mode='markers',
        name='클래스 1',
        marker=dict(color='#EF553B', size=8, line=dict(width=1, color='DarkSlateGrey'))
    ))

    fig.update_layout(
        title=f"결정 경계면 (Decision Boundary) - {model_type}",
        xaxis_title="특성 1 (Feature 1)",
        yaxis_title="특성 2 (Feature 2)",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

with col_metric:
    st.markdown("### 📊 모델 성능")
    st.metric(label="학습 데이터 정확도", value=f"{train_acc * 100:.1f}%")
    st.metric(label="테스트 데이터 정확도", value=f"{test_acc * 100:.1f}%")
    
    st.info("""
    **💡 관전 포인트**
    * **노이즈**를 높이면 데이터 혼잡도가 증가합니다.
    * **모델 파라미터**를 조정하면서 결정 경계면이 복잡해지거나 단순해지는 양상을 관찰해보세요.
    """)

# ---------------------------------------------------------
# Section 3: Summary / Steps
# ---------------------------------------------------------
st.divider()
st.subheader("💡 머신러닝 프로세스 한눈에 보기")

st.markdown("""
1. **데이터 수집 및 전처리:** 센서 데이터, 텍스트, 이미지 등 수집 및 정제
2. **특성 공학 (Feature Engineering):** 모델이 학습하기 좋은 형태로 변환 (예: Feature 1, Feature 2)
3. **모델 선택 및 학습:** 알고리즘(KNN, Decision Tree 등)을 선택하고 데이터 패턴 학습
4. **평가 및 검증:** 테스트 데이터를 활용해 과적합(Overfitting) 여부 및 성능 확인
5. **배포 및 활용:** 시뮬레이터와 같이 실시간 예측 시스템 구축
""")