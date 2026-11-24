
import streamlit as st
import pandas as pd

# 1. 앱 제목
st.title("🏃 스마트 운동 케어")
st.write("호흡·맥박 측정 후 맞춤 운동 추천")

# 2. 부상 및 위험 데이터 리스트
hurt_exercise = ["근육 경련", "근육 피로", "어지럼증", "탈수", "호흡 곤란"]
risk_data = ["근육 과사용", "과도한 운동", "신체 이상", "수분 부족", "호흡 이상"]

# 3. 위험도 분석 함수
def check_risk(pulse, breath):
    score = 0

    if pulse >= 150 or breath >= 35:
        score = 3
        warning = "위험! 운동을 중단하세요."
    elif pulse >= 120 or breath >= 25:
        score = 2
        warning = "주의! 운동 강도를 낮추세요."
    else:
        score = 1
        warning = "큰 이상 신호가 없습니다."

    return score, warning

# 4. 사용자 입력
exercise = st.selectbox(
    "운동 선택",
    ["걷기", "달리기", "자전거", "줄넘기", "근력 운동"]
)

pulse = st.slider("분당 맥박수", 40, 220, 80)
breath = st.slider("분당 호흡수", 5, 60, 16)

# 5. 분석 버튼
if st.button("운동 분석하기"):

    score, warning = check_risk(pulse, breath)

    if score == 3:
        recommendation = "운동 중단 및 휴식"
        st.error(warning)

    elif score == 2:
        recommendation = "가벼운 스트레칭 및 휴식"
        st.warning(warning)

    else:
        recommendation = exercise + " 운동을 무리하지 않는 강도로 진행하세요."
        st.success(warning)

    st.metric("위험도 점수", score)
    st.write("추천 운동 방향:", recommendation)

# 6. for문으로 부상 데이터 표 만들기
table_data = []

for i in range(len(hurt_exercise)):
    table_data.append({
        "번호": i + 1,
        "부상 종류": hurt_exercise[i],
        "위험 요인": risk_data[i]
    })

# 7. DataFrame 출력
df = pd.DataFrame(table_data)

st.subheader("운동 관련 신체 이상 데이터")
st.dataframe(df, use_container_width=True)

# 8. 안내 문구
st.caption(
    "본 프로그램은 교육용 예시이며 의학적 진단용이 아닙니다."
)

