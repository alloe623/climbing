import streamlit as st
import base64
from pathlib import Path

# Apply embedded local font from ./fonts folder.
# Use KERISKEDU_R.ttf or 원하는 다른 파일명으로 변경 가능합니다.
font_path = Path(__file__).resolve().parents[1] / "fonts" / "KERISKEDU_R.ttf"
with open(font_path, "rb") as f:
    font_base64 = base64.b64encode(f.read()).decode("utf-8")

st.set_page_config(page_title="볼더링", layout="wide")

st.markdown(f"""
<style>
@font-face {{
  font-family: 'KERISKEDU';
  src: url(data:font/truetype;charset=utf-8;base64,{font_base64}) format('truetype');
  font-weight: normal;
  font-style: normal;
}}
:root, html, body, .stApp, [class*='css'] {{
  font-family: 'KERISKEDU', sans-serif !important;
}}
</style>
""", unsafe_allow_html=True)

st.title("🧗 볼더링 (Bouldering)")

st.markdown("---")

st.header("볼더링이란?")
st.write("""
볼더링은 로프 없이 낮은 높이의 암벽(보통 3~5m 높이)을 오르는 클라이밍 스포츠입니다.
안전망(매트)이 설치되어 있어 로프와 안전벨트 없이도 안전하게 즐길 수 있습니다.
개인의 능력에 맞는 난이도의 루트를 선택할 수 있어 초보자부터 전문가까지 모두 즐길 수 있습니다.
""")

st.header("볼더링의 특징")

col1, col2 = st.columns(2)

with col1:
    st.subheader("장점")
    st.write("""
    ✅ **낮은 난이도 학습곡선**: 특별한 교육 없이 시작 가능
    
    ✅ **빠른 운동 효과**: 짧은 시간 고강도 운동
    
    ✅ **사회성**: 같은 시간에 여러 사람과 함께 운동 가능
    
    ✅ **비용 효율적**: 로프/안전장비 불필요
    
    ✅ **재미**: 다양한 루트와 문제 풀이의 재미
    
    ✅ **문제 해결력**: 로직과 전술 개발
    """)

with col2:
    st.subheader("필요한 것")
    st.write("""
    🧤 **클라이밍화**: 발가락이 강한 전문 신발
    
    🎒 **맞춤형 분필**: 손의 그립 개선
    
    🧴 **분필 가방**: 분필 보관
    
    🥋 **편한 옷**: 움직임이 자유로운 의류
    
    💪 **기본 체력**: 충분한 근력과 유연성
    
    🏪 **클라이밍 짐**: 안전망이 있는 실내 시설
    """)

st.header("볼더링의 기술")

st.subheader("1. 홀드 잡기 (Hold Grip)")
st.write("""
- **Crimp Hold**: 손가락으로 홀드를 집는 방식 - 가장 기본적이고 중요
- **Jug Hold**: 손잡이처럼 큰 홀드를 쥐는 방식 - 초보자 친화적
- **Sloper Hold**: 내려경사진 홀드 - 손목과 팔 근력 필요
- **Pocket Hold**: 작은 구멍 모양의 홀드 - 손가락 강도 필요
""")

st.subheader("2. 발 기술 (Footwork)")
st.write("""
- **정밀한 발 배치**: 정확한 위치에 발을 올리는 것
- **발의 전환**: 한 발에서 다른 발로 무게 이동
- **엣지 사용**: 발의 안쪽 또는 바깥쪽 모서리 활용
- **정점 도달**: 발을 홀드 위에 올리고 일어서기
""")

st.subheader("3. 신체 움직임 (Body Movement)")
st.write("""
- **근접성**: 몸을 벽에 가깝게 유지하여 팔에 부담 감소
- **회전 (Rotation)**: 어깨를 회전시켜 도달 거리 증가
- **균형 유지**: 무게 중심 조절로 효율성 증대
- **동적 움직임 (Dynamic Movement)**: 점프나 스윙을 통한 홀드 이동
""")

st.header("볼더링 난이도 등급")

difficulty_data = {
    "등급": ["V0", "V1-V2", "V3-V4", "V5", "V6", "V7+"],
    "설명": [
        "초급자도 배울 수 있는 기본 문제",
        "기본 기술을 습득한 초보자 수준",
        "중급자: 다양한 기술 적용 필요",
        "상급자: 복잡한 시퀀스와 강도 필요",
        "전문가까지도 도전적인 문제",
        "엘리트: 월드 클래스 클라이머를 위한 문제"
    ]
}

st.table(difficulty_data)

st.header("볼더링 안전 팁")

st.warning("""
1️⃣ **준비 운동**: 항상 충분한 스트레칭으로 시작
2️⃣ **안전망 확인**: 매트의 위치와 상태 점검
3️⃣ **스팟터 활용**: 친구에게 스폿팅(낙하 시 안전 보조) 받기
4️⃣ **점진적 난이도**: 자신의 능력에 맞는 루트부터 시작
5️⃣ **부상 예방**: 무리하지 말고 충분한 휴식
6️⃣ **손가락 관리**: 특히 손가락 부상에 주의
7️⃣ **수분 섭취**: 운동 중 충분한 수분 섭취
""")

st.header("볼더링의 이점")

benefits = {
    "신체적 이점": "전신 근력, 유연성, 지구력 향상",
    "정신적 이점": "문제 해결 능력, 자신감, 집중력 증진",
    "사회적 이점": "클라이밍 커뮤니티와의 친교",
    "재활 효과": "안전한 환경에서 근력 회복"
}

for title, benefit in benefits.items():
    st.write(f"**{title}**: {benefit}")

st.info("""
💡 **팁**: 정기적인 스트레칭과 적절한 회복 시간을 가지면 부상을 예방하고 
지속적인 성장을 할 수 있습니다!
""")
