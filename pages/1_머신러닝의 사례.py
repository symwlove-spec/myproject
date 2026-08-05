import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 기본 설정
st.set_page_config(
    page_title="머신러닝의 사례",
    page_icon="💡",
    layout="wide"
)

# 헤더 영역
st.title("💡 머신러닝 문제 해결 사례")
st.caption("실제 개발된 머신러닝 문제 해결 사례 웹 페이지를 시뮬레이션 화면으로 확인합니다.")

# HTML 파일 경로 설정 (프로젝트 루트에 위치한 aaaa.html 파일)
html_file_path = "비버의 축용요소 끼워맞춤(E20250242 황선영_최종).html"

# 파일 존재 여부 확인 후 렌더링
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    st.markdown("---")
    
    # 상하 및 좌우 스크롤을 가능하게 만드는 CSS wrapper
    # 기본 크기: 너비 1024px, 높이 768px (콘텐츠가 클 경우 스크롤 생성)
    custom_css = """
    <style>
        .iframe-wrapper {
            width: 1024px;
            height: 768px;
            overflow: auto; /* 상하/좌우 스크롤바 자동 생성 */
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #ffffff;
        }
        /* 내부 콘텐츠가 1024px보다 작더라도 틀을 유지하도록 설정 */
        .iframe-content {
            width: 100%;
            min-width: 1024px;
            height: 100%;
        }
    </style>
    """

    # HTML 커스텀 래퍼와 사용자 html 파일 결합
    wrapped_html = f"""
    {custom_css}
    <div class="iframe-wrapper">
        <div class="iframe-content">
            {html_content}
        </div>
    </div>
    """

    # Streamlit components.html 사용하여 렌더링
    # 1024x768 크기 및 외곽 여백 처리
    components.html(
        wrapped_html,
        width=1050,  # 스크롤바 여유 공간을 위해 너비 약간 확장
        height=790,  # 스크롤바 여유 공간을 위해 높이 약간 확장
        scrolling=True
    )

else:
    st.warning(f"⚠️ `{html_file_path}` 파일을 찾을 수 없습니다.")
    st.info("""
    **안내:**
    프로젝트 최상위(Root) 폴더에 `aaaa.html` 파일을 배치해 주세요.
    
    ```text
    📁 my_streamlit_project/
    ├── 📄 app.py
    ├── 📄 database.py
    ├── 📄 aaaa.html  <-- 여기에 위치해야 합니다.
    └── 📁 pages/
        ├── 📄 0_머신러닝의_개념.py
        ├── 📄 2_머신러닝의_사례.py
        └── 📄 3_형성평가.py
    ```
    """)
