<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   st.title("비버의 비밀 기어 장치 조립 - CT 3단계 문제해결 모듈")

    <!-- Pretendard 웹폰트 -->
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css" />
    
    <style>
        :root {
            --primary: #4F46E5;
            --primary-hover: #4338CA;
            --secondary: #0EA5E9;
            --accent: #F59E0B;
            --success: #10B981;
            --danger: #EF4444;
            --bg-main: #F8FAFC;
            --card-bg: #FFFFFF;
            --text-main: #0F172A;
            --text-sub: #475569;
            --border-color: #E2E8F0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: "Pretendard", -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
        }

        body {
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.6;
            padding: 20px 16px;
            display: flex;
            justify-content: center;
            min-height: 100vh;
        }

        .container {
            max-width: 1240px;
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .header-dashboard {
            background: linear-gradient(135deg, #4F46E5 0%, #0EA5E9 100%);
            color: white;
            padding: 24px;
            border-radius: 20px;
            box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.25);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }

        .header-title h1 {
            font-size: 22px;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header-title p {
            font-size: 14px;
            opacity: 0.95;
            margin-top: 4px;
        }

        .scoreboard {
            display: flex;
            align-items: center;
            gap: 16px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            padding: 10px 20px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.25);
        }

        .score-item {
            text-align: center;
        }

        .score-item .label {
            font-size: 12px;
            font-weight: 600;
            opacity: 0.85;
            display: block;
        }

        .score-item .value {
            font-size: 22px;
            font-weight: 800;
            color: #FFFFFF;
        }

        .divider {
            width: 1px;
            height: 32px;
            background: rgba(255, 255, 255, 0.3);
        }

        .btn-reset-game {
            background-color: #FFFFFF;
            color: var(--primary);
            border: none;
            padding: 10px 16px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .btn-reset-game:hover {
            background-color: #F1F5F9;
            transform: translateY(-1px);
        }

        .main-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
        }

        @media (min-width: 850px) {
            .main-grid {
                grid-template-columns: 0.9fr 1.1fr;
            }
        }

        .card {
            background: var(--card-bg);
            border-radius: 18px;
            padding: 22px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .card-title {
            font-size: 17px;
            font-weight: 800;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .step-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 800;
            margin-bottom: 4px;
            width: fit-content;
        }

        .badge-step1 { background-color: #E0E7FF; color: var(--primary); }
        .badge-step2 { background-color: #FEF3C7; color: #92400E; }
        .badge-step3 { background-color: #D1FAE5; color: #065F46; }

        .table-wrapper {
            overflow-x: auto;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: center;
            font-size: 13.5px;
        }

        th, td {
            padding: 10px 12px;
            border-bottom: 1px solid var(--border-color);
        }

        th {
            background-color: #F1F5F9;
            color: var(--text-sub);
            font-weight: 700;
        }

        .tag {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
        }
        .tag-loose { background: #FEF3C7; color: #92400E; }
        .tag-tight { background: #FEE2E2; color: #991B1B; }
        .tag-trans { background: #E0E7FF; color: #3730A3; }

        .custom-select {
            display: inline-block;
            padding: 6px 10px;
            font-size: 13.5px;
            font-weight: 700;
            color: var(--primary);
            background-color: #FFFFFF;
            border: 2px solid var(--primary);
            border-radius: 8px;
            cursor: pointer;
            outline: none;
            transition: all 0.2s;
            margin: 2px 0;
            max-width: 100%;
        }

        .abs-row {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 8px;
            background: #FFFFFF;
            padding: 12px 14px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        }

        .abs-row-tag {
            font-size: 12px;
            font-weight: 800;
            color: var(--primary);
            background-color: #EEF2FF;
            padding: 3px 8px;
            border-radius: 6px;
            white-space: nowrap;
        }

        .step-box {
            background-color: #FAFAFA;
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .quiz-card {
            background-color: #EEF2FF;
            border: 2px dashed var(--primary);
            border-radius: 14px;
            padding: 18px;
        }

        .quiz-sentence {
            font-size: 14.5px;
            line-height: 2.2;
            word-break: keep-all;
        }

        .info-box {
            display: none;
            padding: 12px 14px;
            border-radius: 10px;
            font-size: 13.5px;
            line-height: 1.5;
            animation: fadeIn 0.3s ease;
        }

        .feedback-correct {
            background-color: #ECFDF5;
            border: 1px solid #A7F3D0;
            color: #065F46;
        }

        .feedback-wrong {
            background-color: #FEF2F2;
            border: 1px solid #FCA5A5;
            color: #991B1B;
        }

        .hint-box {
            background-color: #FFFBEB;
            border: 1px solid #FCD34D;
            color: #78350F;
        }

        .btn-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .btn {
            flex: 1;
            min-width: 120px;
            padding: 11px 16px;
            border: none;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
        }
        .btn-primary:hover { background-color: var(--primary-hover); transform: translateY(-1px); }

        .btn-secondary {
            background-color: #FEF3C7;
            color: #92400E;
        }
        .btn-secondary:hover { background-color: #FDE68A; }

        .stepper-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #F1F5F9;
            padding: 6px;
            border-radius: 12px;
            margin-bottom: 6px;
            gap: 6px;
        }

        .step-tab {
            flex: 1;
            text-align: center;
            padding: 10px 8px;
            font-size: 13px;
            font-weight: 700;
            border-radius: 8px;
            color: var(--text-sub);
            background: transparent;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .step-tab.active {
            background: #FFFFFF;
            color: var(--primary);
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        }

        .step-tab.completed {
            color: var(--success);
        }

        .step-tab.locked {
            opacity: 0.5;
            cursor: not-allowed;
            background: rgba(0,0,0,0.03);
        }

        /* 춤추는 바비 축하 모달 스타일 */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(6px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }

        .modal-card {
            background: #FFFFFF;
            border-radius: 24px;
            padding: 32px 28px;
            max-width: 440px;
            width: 90%;
            text-align: center;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.1);
            transform: scale(0.8) translateY(20px);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
        }

        .modal-overlay.active .modal-card {
            transform: scale(1) translateY(0);
        }

        /* 바비 춤 애니메이션 */
        .bobby-character {
            width: 160px;
            height: 160px;
            animation: bobbyBounce 0.6s infinite alternate ease-in-out;
        }

        .bobby-tail {
            transform-origin: 20px 110px;
            animation: bobbyTail 0.3s infinite alternate ease-in-out;
        }

        .bobby-arm-left {
            transform-origin: 50px 85px;
            animation: bobbyArmLeft 0.5s infinite alternate ease-in-out;
        }

        .bobby-arm-right {
            transform-origin: 110px 85px;
            animation: bobbyArmRight 0.5s infinite alternate ease-in-out;
        }

        @keyframes bobbyBounce {
            0% { transform: translateY(0) rotate(-3deg); }
            100% { transform: translateY(-16px) rotate(3deg); }
        }

        @keyframes bobbyTail {
            0% { transform: rotate(-15deg); }
            100% { transform: rotate(20deg); }
        }

        @keyframes bobbyArmLeft {
            0% { transform: rotate(-20deg); }
            100% { transform: rotate(40deg); }
        }

        @keyframes bobbyArmRight {
            0% { transform: rotate(20deg); }
            100% { transform: rotate(-40deg); }
        }

        .modal-title {
            font-size: 22px;
            font-weight: 800;
            color: var(--text-main);
        }

        .modal-desc {
            font-size: 14.5px;
            color: var(--text-sub);
            line-height: 1.5;
        }

        .step-content {
            display: none;
        }

        .step-content.active {
            display: flex;
            flex-direction: column;
            gap: 16px;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        #canvas {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 999;
        }
    </style>
</head>
<body>

<canvas id="canvas"></canvas>

<div class="container">
    <header class="header-dashboard">
        <div class="header-title">
            <h1>🦫 비버의 동력전달장치 - CT 3단계 컴퓨팅 사고력 학습</h1>
            <p>1열의 데이터를 참조하여 [1. 추상화] → [2. 패턴 분석] → [3. 알고리즘 적용] 순서로 해결하세요!</p>
        </div>

        <div style="display: flex; align-items: center; gap: 12px;">
            <div class="scoreboard">
                <div class="score-item">
                    <span class="label">현재 점수</span>
                    <span class="value" id="scoreVal">0점</span>
                </div>
                <div class="divider"></div>
                <div class="score-item">
                    <span class="label">총 시도 횟수</span>
                    <span class="value" id="attemptVal">0회</span>
                </div>
            </div>
            <button class="btn-reset-game" onclick="resetGame()">🔄 게임 다시하기</button>
        </div>
    </header>

    <div class="main-grid">
        
        <!-- ========================================== -->
        <!-- 1열 (좌측): 문제 시나리오 및 기준 데이터 표 (고정 참고 자료) -->
        <!-- ========================================== -->
        <aside class="card">
            <div>
                <span class="step-badge badge-step1">📖 문제 시나리오 및 기준 데이터</span>
                <div class="card-title">⚙️ 비버 공장의 선배 작업자 조립 데이터</div>
            </div>

            <p style="font-size: 13.5px; color: var(--text-sub);">
                비버 마크의 공장에서는 베어링 구멍과 동력축을 결합하는 작업을 합니다. 
                아래 표는 5명의 선배 작업자가 가공한 부품 치수와 끼워맞춤 결과입니다.
            </p>

            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
                            <th>작업자</th>
                            <th>구멍 지름 (H)</th>
                            <th>축 지름 범위 (S<sub>min</sub> ~ S<sub>max</sub>)</th>
                            <th>조립 결과</th>
                        </tr>
                    </thead>
                    <tbody id="refTableBody">
                        <!-- JS에서 무작위 데이터 자동 생성 -->
                    </tbody>
                </table>
            </div>

            <div style="background-color: #F8FAFC; border-radius: 12px; padding: 12px; border: 1px solid var(--border-color); font-size: 12.5px; color: var(--text-sub);">
                <strong>💡 기호 설명:</strong><br>
                • <code>H</code> : 베어링 구멍 내경 지름<br>
                • <code>S<sub>min</sub></code>, <code>S<sub>max</sub></code> : 축 외경 가공 최솟값 및 최댓값<br>
                • <strong>헐거운 끼워맞춤</strong>: 축이 구멍보다 작아 원활히 회전함.<br>
                • <strong>억지 끼워맞춤</strong>: 축이 구멍보다 크거나 같아 강력히 고정됨.<br>
                • <strong>중간 끼워맞춤</strong>: 제작 오차에 따라 틈새/죔새가 모두 발생 가능.
            </div>
        </aside>

        <!-- ========================================== -->
        <!-- 2열 (우측): 컴퓨팅 사고력(CT) 3단계 문제 해결 Wizard -->
        <!-- ========================================== -->
        <main class="card" style="display: flex; flex-direction: column; gap: 16px;">
            
            <!-- 단계별 진행 네비게이션 탭 -->
            <div class="stepper-nav">
                <button id="tabStep1" class="step-tab active" onclick="goToStep(1)">1. 추상화</button>
                <button id="tabStep2" class="step-tab" onclick="goToStep(2)">2. 패턴 분석</button>
                <button id="tabStep3" class="step-tab" onclick="goToStep(3)">3. 알고리즘 적용</button>
            </div>

            <!-- STEP 1. 추상화 (Abstraction) - 작업자 1명 데이터 실습 -->
            <div id="stepContainer1" class="step-content active">
                <div>
                    <span class="step-badge badge-step1">STEP 1. 데이터 추상화 (Abstraction)</span>
                    <div class="card-title">🔍 데이터에서 핵심 속성(작업자-구멍-축-결과) 추상화하기</div>
                </div>
                <p style="font-size: 13.5px; color: var(--text-sub);">
                    좌측 기준 데이터 표를 관찰하고, <strong>작업자 1명</strong>을 선택하여 해당 작업자의 [구멍 지름], [축 지름 범위], [끼워맞춤 결과] 속성을 직접 매칭해보세요.
                </p>

                <div class="step-box">
                    <div id="absRowsContainer" style="display: flex; flex-direction: column; gap: 10px;">
                        <!-- JS에서 작업자 1명 선택 행 생성 -->
                    </div>

                    <div id="step1Feedback" class="info-box"></div>

                    <div class="btn-group" style="margin-top: 8px;">
                        <button class="btn btn-primary" onclick="checkAndNextStep1()">
                            Step 1 검증 및 다음 단계로 ➡️
                        </button>
                    </div>
                </div>
            </div>

            <!-- STEP 2. 패턴 분석 (Pattern Analysis) -->
            <div id="stepContainer2" class="step-content">
                <div>
                    <span class="step-badge badge-step2">STEP 2. 패턴 분석 (Pattern Analysis)</span>
                    <div class="card-title">🧩 조립 시 발생하는 물리적 현상 패턴 분류하기</div>
                </div>
                <p style="font-size: 13.5px; color: var(--text-sub);">
                    추상화된 치수 조건에 따라 실제로 조립할 때 발생하는 틈새/죔새 현상 패턴을 매칭하세요.
                </p>

                <div class="step-box">
                    <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13.5px;">
                        <div>
                            <strong>패턴 A:</strong> <code>S<sub>max</sub> &lt; H</code> (헐거운 끼워맞춤) 일 때 발생 현상 → 
                            <select id="patRule1" class="custom-select">
                                <option value="">-- 현상 선택 --</option>
                                <option value="항상 틈새">항상 틈새</option>
                                <option value="항상 죔새">항상 죔새</option>
                                <option value="틈새 또는 죔새">틈새 또는 죔새</option>
                            </select>
                        </div>

                        <div>
                            <strong>패턴 B:</strong> <code>S<sub>min</sub> &gt; H</code> (억지 끼워맞춤) 일 때 발생 현상 → 
                            <select id="patRule2" class="custom-select">
                                <option value="">-- 현상 선택 --</option>
                                <option value="항상 틈새">항상 틈새</option>
                                <option value="항상 죔새">항상 죔새</option>
                                <option value="틈새 또는 죔새">틈새 또는 죔새</option>
                            </select>
                        </div>

                        <div>
                            <strong>패턴 C:</strong> <code>S<sub>min</sub> &le; H &le; S<sub>max</sub></code> (중간 끼워맞춤) 일 때 발생 현상 → 
                            <select id="patRule3" class="custom-select">
                                <option value="">-- 현상 선택 --</option>
                                <option value="항상 틈새">항상 틈새</option>
                                <option value="항상 죔새">항상 죔새</option>
                                <option value="틈새 또는 죔새">틈새 또는 죔새</option>
                            </select>
                        </div>
                    </div>

                    <div id="step2Feedback" class="info-box"></div>

                    <div class="btn-group" style="margin-top: 8px;">
                        <button class="btn btn-secondary" onclick="goToStep(1)">⬅️ 이전 (Step 1)</button>
                        <button class="btn btn-primary" onclick="checkAndNextStep2()">Step 2 검증 및 다음 단계로 ➡️</button>
                    </div>
                </div>
            </div>

            <!-- STEP 3. 알고리즘 적용 (Algorithm Application) -->
            <div id="stepContainer3" class="step-content">
                <div>
                    <span class="step-badge badge-step3">STEP 3. 알고리즘 적용 (Algorithm Application)</span>
                    <div class="card-title">⚙️ 실전 문제! 새로 지급된 부품 판별하기</div>
                </div>
                <p style="font-size: 13.5px; color: var(--text-sub);">
                    Step 1과 Step 2에서 완성한 규칙 알고리즘을 바탕으로 새로 지급된 베어링과 축의 끼워맞춤을 완성하고 제출하세요!
                </p>

                <div class="quiz-card">
                    <!-- 무작위 문제 치수 표 -->
                    <div class="table-wrapper" style="margin-bottom: 14px;">
                        <table>
                            <thead>
                                <tr>
                                    <th>새 베어링 구멍 지름 (H)</th>
                                    <th>새 가공 축 지름 (S<sub>min</sub> ~ S<sub>max</sub>)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong id="targetHole" style="font-size: 16px; color: var(--primary);">Ø50</strong></td>
                                    <td><strong id="targetShaft" style="font-size: 16px; color: var(--primary);">Ø50.01 ~ Ø50.02</strong></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- 빈칸 완성 문장 -->
                    <div class="quiz-sentence">
                        바비는 지급된 부품의 치수를 비교하여
                        <select id="blank1" class="custom-select">
                            <option value="">-- 발생 현상 선택 --</option>
                            <option value="항상 틈새">항상 틈새</option>
                            <option value="항상 죔새">항상 죔새</option>
                            <option value="틈새 또는 죔새">틈새 또는 죔새</option>
                        </select>
                        가 발생하는 것을 확인했고, 알고리즘에 따라
                        <select id="blank2" class="custom-select">
                            <option value="">-- 최종 끼워맞춤 선택 --</option>
                            <option value="헐거운 끼워맞춤">헐거운 끼워맞춤</option>
                            <option value="억지 끼워맞춤">억지 끼워맞춤</option>
                            <option value="중간 끼워맞춤">중간 끼워맞춤</option>
                        </select>
                        이 됨을 도출해냈다.
                    </div>
                </div>

                <!-- 정오 피드백 박스 -->
                <div id="feedback" class="info-box"></div>

                <!-- 힌트 박스 -->
                <div id="hintBox" class="info-box hint-box">
                    💡 <strong>알고리즘 적용 힌트:</strong><br>
                    1. 구멍 지름 H와 축의 최소 S<sub>min</sub>, 최대 S<sub>max</sub> 치수를 확인하세요.<br>
                    2. S<sub>max</sub> &lt; H, S<sub>min</sub> &gt; H, S<sub>min</sub> &le; H &le; S<sub>max</sub> 중 어느 조건식에 해당하는지 대입해보세요!
                </div>

                <!-- 제출 및 힌트 버튼 그룹 -->
                <div class="btn-group">
                    <button class="btn btn-secondary" onclick="goToStep(2)">⬅️ 이전 (Step 2)</button>
                    <button class="btn btn-primary" onclick="submitAnswer()">🎯 정답 제출 (채점 & 보드 셔플)</button>
                    <button class="btn btn-secondary" style="flex:0.5; min-width:80px;" onclick="toggleHint()">💡 힌트</button>
                </div>
            </div>

        </main>
    </div>
</div>

<!-- 춤추는 비버 바비 축하 모달 -->
<div id="danceModal" class="modal-overlay">
    <div class="modal-card">
        <!-- SVG Animated Beaver "Bobby" -->
        <svg class="bobby-character" viewBox="0 0 160 160" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Tail -->
            <path class="bobby-tail" d="M 30 110 C 10 120, 0 100, 10 85 C 20 70, 40 90, 45 105 Z" fill="#6B4226" stroke="#4A2E1B" stroke-width="3"/>
            <!-- Body -->
            <ellipse cx="80" cy="105" rx="42" ry="38" fill="#8B5A2B"/>
            <ellipse cx="80" cy="108" rx="26" ry="24" fill="#D2B48C"/>
            <!-- Feet -->
            <ellipse cx="58" cy="142" rx="14" ry="7" fill="#6B4226"/>
            <ellipse cx="102" cy="142" rx="14" ry="7" fill="#6B4226"/>
            <!-- Head -->
            <circle cx="80" cy="65" r="32" fill="#8B5A2B"/>
            <!-- Ears -->
            <circle cx="54" cy="42" r="9" fill="#6B4226"/>
            <circle cx="106" cy="42" r="9" fill="#6B4226"/>
            <!-- Snout & Teeth -->
            <ellipse cx="80" cy="72" rx="16" ry="11" fill="#D2B48C"/>
            <rect x="74" y="78" width="5" height="9" rx="1" fill="#FFFFFF" stroke="#CCCCCC" stroke-width="0.5"/>
            <rect x="81" y="78" width="5" height="9" rx="1" fill="#FFFFFF" stroke="#CCCCCC" stroke-width="0.5"/>
            <ellipse cx="80" cy="68" rx="5" ry="3.5" fill="#332211"/>
            <!-- Eyes (Sparkling) -->
            <circle cx="68" cy="58" r="4.5" fill="#111111"/>
            <circle cx="70" cy="56" r="1.5" fill="#FFFFFF"/>
            <circle cx="92" cy="58" r="4.5" fill="#111111"/>
            <circle cx="94" cy="56" r="1.5" fill="#FFFFFF"/>
            <!-- Cheeks -->
            <circle cx="60" cy="70" r="5" fill="#FFB6C1" opacity="0.7"/>
            <circle cx="100" cy="70" r="5" fill="#FFB6C1" opacity="0.7"/>
            <!-- Left Arm -->
            <path class="bobby-arm-left" d="M 45 92 Q 25 75 35 60" stroke="#8B5A2B" stroke-width="10" stroke-linecap="round"/>
            <!-- Right Arm -->
            <path class="bobby-arm-right" d="M 115 92 Q 135 75 125 60" stroke="#8B5A2B" stroke-width="10" stroke-linecap="round"/>
            <!-- Party Hat -->
            <polygon points="80,18 66,42 94,42" fill="#F59E0B"/>
            <circle cx="80" cy="16" r="4" fill="#EF4444"/>
        </svg>

        <div class="modal-title">🎉 바비의 축하 댄스! 🎉</div>
        <div class="modal-desc">
            대단해요! <strong>추상화 → 패턴 분석 → 알고리즘 적용</strong>까지 CT 3단계를 모두 성공적으로 완수했습니다! 🦫✨
        </div>
        
        <button class="btn btn-primary" style="width: 100%; padding: 14px; font-size: 15px;" onclick="closeModalAndNextQuestion()">
            🚀 다음 문제 도전하기
        </button>
    </div>
</div>

<script>
    let score = 0;
    let attempts = 0;
    let currentStep = 1;
    let unlockedStep = 1; // 사용자가 잠금 해제한 최고 단계
    let currentProblem = {};
    let currentWorkersData = [];

    window.onload = () => {
        generateNewQuestion();
    };

    function goToStep(stepNum) {
        // 학생이 정답을 맞추지 않은 단계로 무단 이동 방지
        if (stepNum > unlockedStep) {
            showToastMessage(`🔒 이전 단계를 올바르게 해결해야 Step ${stepNum}으로 넘어갈 수 있습니다!`);
            return;
        }

        currentStep = stepNum;

        for (let i = 1; i <= 3; i++) {
            const tab = document.getElementById(`tabStep${i}`);
            const container = document.getElementById(`stepContainer${i}`);

            if (i === stepNum) {
                tab.classList.add('active');
                container.classList.add('active');
            } else {
                tab.classList.remove('active');
                container.classList.remove('active');
            }
        }
    }

    function updateTabLocks() {
        for (let i = 1; i <= 3; i++) {
            const tab = document.getElementById(`tabStep${i}`);
            if (i <= unlockedStep) {
                tab.classList.remove('locked');
            } else {
                tab.classList.add('locked');
            }
        }
    }

    function showToastMessage(msg) {
        // alert 대신 UI 내 친화적인 피드백 알림
        const activeFeedback = document.getElementById(`step${currentStep}Feedback`) || document.getElementById('feedback');
        if (activeFeedback) {
            activeFeedback.className = 'info-box feedback-wrong';
            activeFeedback.innerHTML = msg;
            activeFeedback.style.display = 'block';
        }
    }

    function generateNewQuestion() {
        unlockedStep = 1; // 문제 새로 생성 시 Step 1로 잠금 리셋
        updateTabLocks();

        // 1. 기준 데이터 먼저 생성 (선배 작업자 5명의 데이터)
        renderReferenceTable();

        // 2. 1열 기준 데이터 표에 사용된 구멍 지름 목록 추출
        const usedHoles = currentWorkersData.map(w => parseInt(w.holeStr.replace('Ø', '')));

        // 3. 기준 데이터 표의 수치와 절대 중복되지 않는 새로운 구멍 지름 후보 선정 (Ø45 ~ Ø80)
        const candidateHoles = [45, 50, 55, 60, 65, 70, 75, 80].filter(h => !usedHoles.includes(h));
        const targetHole = candidateHoles[Math.floor(Math.random() * candidateHoles.length)];

        const types = ['loose', 'tight', 'transition'];
        const targetType = types[Math.floor(Math.random() * types.length)];

        let sMin, sMax, ans1, ans2;

        if (targetType === 'loose') {
            sMin = (targetHole - 0.05 + Math.random() * 0.01).toFixed(2);
            sMax = (targetHole - 0.02 - Math.random() * 0.01).toFixed(2);
            ans1 = "항상 틈새";
            ans2 = "헐거운 끼워맞춤";
        } else if (targetType === 'tight') {
            sMin = (targetHole + 0.01 + Math.random() * 0.01).toFixed(2);
            sMax = (targetHole + 0.04 + Math.random() * 0.01).toFixed(2);
            ans1 = "항상 죔새";
            ans2 = "억지 끼워맞춤";
        } else {
            sMin = (targetHole - 0.02 + Math.random() * 0.005).toFixed(2);
            sMax = (targetHole + 0.02 + Math.random() * 0.005).toFixed(2);
            ans1 = "틈새 또는 죔새";
            ans2 = "중간 끼워맞춤";
        }

        currentProblem = {
            hole: targetHole,
            sMin: sMin,
            sMax: sMax,
            ans1: ans1,
            ans2: ans2
        };

        renderStep1UI();

        document.getElementById('targetHole').innerText = `Ø${currentProblem.hole}`;
        document.getElementById('targetShaft').innerText = `Ø${currentProblem.sMin} ~ Ø${currentProblem.sMax}`;
        
        // 문제 및 상태 초기화
        document.getElementById('blank1').value = "";
        document.getElementById('blank2').value = "";
        document.getElementById('patRule1').value = "";
        document.getElementById('patRule2').value = "";
        document.getElementById('patRule3').value = "";

        document.getElementById('feedback').style.display = "none";
        document.getElementById('hintBox').style.display = "none";
        document.getElementById('step1Feedback').style.display = "none";
        document.getElementById('step2Feedback').style.display = "none";

        // 탭 상태 리셋
        for (let i = 1; i <= 3; i++) {
            document.getElementById(`tabStep${i}`).classList.remove('completed');
        }

        // Step 1로 전환
        goToStep(1);
    }

    function renderReferenceTable() {
        const names = ['선민', '수호', '명규', '태윤', '한난', '민준', '서연', '도윤', '지우', '하준'];
        const shuffledNames = names.sort(() => 0.5 - Math.random()).slice(0, 5);

        // 다양한 구멍 지름(Ø20 ~ Ø40)으로 구성된 기준 데이터 행 생성
        const rowTypes = [
            { type: 'loose', hole: 20 },
            { type: 'tight', hole: 25 },
            { type: 'transition', hole: 30 },
            { type: 'transition', hole: 35 },
            { type: 'loose', hole: 40 }
        ].sort(() => 0.5 - Math.random());

        let tableHtml = '';
        currentWorkersData = [];

        rowTypes.forEach((row, i) => {
            let h = row.hole;
            let min, max, nameStr, tagClass;

            if (row.type === 'loose') {
                min = (h - 0.05).toFixed(2);
                max = (h - 0.02).toFixed(2);
                nameStr = "헐거운 끼워맞춤";
                tagClass = "tag-loose";
            } else if (row.type === 'tight') {
                min = (h + 0.02).toFixed(2);
                max = (h + 0.05).toFixed(2);
                nameStr = "억지 끼워맞춤";
                tagClass = "tag-tight";
            } else {
                min = (h - 0.01).toFixed(2);
                max = (h + 0.01).toFixed(2);
                nameStr = "중간 끼워맞춤";
                tagClass = "tag-trans";
            }

            const workerName = shuffledNames[i];
            const holeStr = `Ø${h}`;
            const shaftStr = `Ø${min} ~ Ø${max}`;

            currentWorkersData.push({
                name: workerName,
                holeStr: holeStr,
                shaftStr: shaftStr,
                fitting: nameStr
            });

            tableHtml += `
                <tr>
                    <td><strong>${workerName}</strong></td>
                    <td>${holeStr}</td>
                    <td>${shaftStr}</td>
                    <td><span class="tag ${tagClass}">${nameStr}</span></td>
                </tr>
            `;
        });

        document.getElementById('refTableBody').innerHTML = tableHtml;
    }

    function renderStep1UI() {
        const container = document.getElementById('absRowsContainer');
        container.innerHTML = '';

        const workerNames = currentWorkersData.map(w => w.name);
        const uniqueHoles = [...new Set(currentWorkersData.map(w => w.holeStr))];
        const allShafts = [...new Set(currentWorkersData.map(w => w.shaftStr))].sort(() => 0.5 - Math.random());
        const fittings = ['헐거운 끼워맞춤', '억지 끼워맞춤', '중간 끼워맞춤'];

        const rowDiv = document.createElement('div');
        rowDiv.className = 'abs-row';

        rowDiv.innerHTML = `
            <span class="abs-row-tag">데이터 추상화</span>
            
            <select id="absWorker_0" class="custom-select">
                <option value="">-- 작업자 선택 --</option>
                ${workerNames.map(n => `<option value="${n}">${n}</option>`).join('')}
            </select>

            <select id="absHole_0" class="custom-select">
                <option value="">-- 구멍 지름 --</option>
                ${uniqueHoles.map(h => `<option value="${h}">${h}</option>`).join('')}
            </select>

            <select id="absShaft_0" class="custom-select">
                <option value="">-- 축 지름 범위 --</option>
                ${allShafts.map(s => `<option value="${s}">${s}</option>`).join('')}
            </select>

            <select id="absFitting_0" class="custom-select">
                <option value="">-- 끼워맞춤 --</option>
                ${fittings.map(f => `<option value="${f}">${f}</option>`).join('')}
            </select>
        `;

        container.appendChild(rowDiv);
    }

    function checkAndNextStep1() {
        const fb = document.getElementById('step1Feedback');
        const worker = document.getElementById('absWorker_0').value;
        const hole = document.getElementById('absHole_0').value;
        const shaft = document.getElementById('absShaft_0').value;
        const fitting = document.getElementById('absFitting_0').value;

        if (!worker || !hole || !shaft || !fitting) {
            fb.className = 'info-box feedback-wrong';
            fb.innerHTML = '⚠️ 모든 항목(작업자, 구멍 지름, 축 지름 범위, 끼워맞춤)을 정확히 선택해야 다음 단계로 갈 수 있습니다!';
            fb.style.display = 'block';
            return;
        }

        const match = currentWorkersData.find(w => 
            w.name === worker && w.holeStr === hole && w.shaftStr === shaft && w.fitting === fitting
        );

        if (match) {
            fb.className = 'info-box feedback-correct';
            fb.innerHTML = '🎉 <strong>데이터 추상화 완벽 성공!</strong> Step 2 잠금이 해제되었습니다.';
            fb.style.display = 'block';
            
            // Step 2 잠금 해제
            unlockedStep = Math.max(unlockedStep, 2);
            updateTabLocks();

            setTimeout(() => {
                document.getElementById('tabStep1').classList.add('completed');
                goToStep(2);
            }, 800);
        } else {
            fb.className = 'info-box feedback-wrong';
            fb.innerHTML = '❌ 선택하신 데이터 매칭이 기준 데이터 표와 일치하지 않습니다. 다시 확인해 보세요!';
            fb.style.display = 'block';
        }
    }

    function checkAndNextStep2() {
        const p1 = document.getElementById('patRule1').value;
        const p2 = document.getElementById('patRule2').value;
        const p3 = document.getElementById('patRule3').value;
        const fb = document.getElementById('step2Feedback');

        if (!p1 || !p2 || !p3) {
            fb.className = 'info-box feedback-wrong';
            fb.innerHTML = '⚠️ 발생 현상 3개를 모두 바르게 선택해야 Step 3으로 이동할 수 있습니다.';
            fb.style.display = 'block';
            return;
        }

        if (p1 === '항상 틈새' && p2 === '항상 죔새' && p3 === '틈새 또는 죔새') {
            fb.className = 'info-box feedback-correct';
            fb.innerHTML = '🎉 <strong>패턴 분석 완료!</strong> 마지막 알고리즘 적용(Step 3) 잠금이 해제되었습니다.';
            fb.style.display = 'block';

            // Step 3 잠금 해제
            unlockedStep = Math.max(unlockedStep, 3);
            updateTabLocks();

            setTimeout(() => {
                document.getElementById('tabStep2').classList.add('completed');
                goToStep(3);
            }, 800);
        } else {
            fb.className = 'info-box feedback-wrong';
            fb.innerHTML = '❌ 일부 패턴 매칭이 잘못되었습니다. 구멍과 축 치수 조건을 다시 확인하고 맞춘 뒤 넘어가세요.';
            fb.style.display = 'block';
        }
    }

    function submitAnswer() {
        const userAns1 = document.getElementById('blank1').value;
        const userAns2 = document.getElementById('blank2').value;
        const feedback = document.getElementById('feedback');

        if (!userAns1 || !userAns2) {
            feedback.className = 'info-box feedback-wrong';
            feedback.innerHTML = '⚠️ 빈칸 두 개를 모두 완료한 후 정답을 제출해 주세요!';
            feedback.style.display = 'block';
            return;
        }

        attempts++;
        document.getElementById('attemptVal').innerText = `${attempts}회`;

        const isCorrect = (userAns1 === currentProblem.ans1 && userAns2 === currentProblem.ans2);

        if (isCorrect) {
            score += 1;
            document.getElementById('scoreVal').innerText = `${score}점`;
            document.getElementById('tabStep3').classList.add('completed');
            
            feedback.className = 'info-box feedback-correct';
            feedback.innerHTML = `🎉 <strong>정답입니다! (+1점 획득)</strong> 모든 스텝을 완수했습니다!`;
            feedback.style.display = 'block';

            triggerConfetti();
            
            // 바비 댄스 모달 오픈
            setTimeout(() => {
                document.getElementById('danceModal').classList.add('active');
            }, 600);
        } else {
            score = Math.max(0, score - 1);
            document.getElementById('scoreVal').innerText = `${score}점`;

            feedback.className = 'info-box feedback-wrong';
            feedback.innerHTML = `❌ <strong>틀렸습니다!</strong><br>다시 생각해보고 정답을 맞춰야 다음 문제로 진행할 수 있습니다. (힌트를 참고해보세요!)`;
            feedback.style.display = 'block';
        }
    }

    function closeModalAndNextQuestion() {
        document.getElementById('danceModal').classList.remove('active');
        generateNewQuestion();
    }

    function toggleHint() {
        const hintBox = document.getElementById('hintBox');
        hintBox.style.display = (hintBox.style.display === 'block') ? 'none' : 'block';
    }

    function resetGame() {
        score = 0;
        attempts = 0;
        document.getElementById('scoreVal').innerText = '0점';
        document.getElementById('attemptVal').innerText = '0회';
        generateNewQuestion();
    }

    function triggerConfetti() {
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particles = [];
        const colors = ['#4F46E5', '#0EA5E9', '#10B981', '#F59E0B', '#EC4899'];

        for (let i = 0; i < 90; i++) {
            particles.push({
                x: canvas.width / 2,
                y: canvas.height / 2,
                vx: (Math.random() - 0.5) * 16,
                vy: (Math.random() - 0.5) * 16 - 3,
                size: Math.random() * 8 + 4,
                color: colors[Math.floor(Math.random() * colors.length)],
                alpha: 1
            });
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            let active = false;

            particles.forEach(p => {
                p.x += p.vx;
                p.y += p.vy;
                p.vy += 0.25;
                p.alpha -= 0.015;

                if (p.alpha > 0) {
                    active = true;
                    ctx.save();
                    ctx.globalAlpha = p.alpha;
                    ctx.fillStyle = p.color;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.restore();
                }
            });

            if (active) requestAnimationFrame(animate);
        }
        animate();
    }
</script>
</body>
</html>