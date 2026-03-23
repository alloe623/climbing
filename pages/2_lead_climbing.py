import streamlit as st
import base64
from pathlib import Path

font_path = Path(__file__).resolve().parents[1] / "fonts" / "KERISKEDU_R.ttf"
with open(font_path, "rb") as f:
    font_base64 = base64.b64encode(f.read()).decode("utf-8")

st.markdown(f"""
<style>
@font-face {{
  font-family: 'KERISKEDU';
  src: url(data:font/truetype;charset=utf-8;base64,{font_base64}) format('truetype');
  font-weight: normal;
  font-style: normal;
}}
html, body, [class*='css'] {{
  font-family: 'KERISKEDU', sans-serif !important;
}}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="리드클라이밍", layout="wide")

st.title("🪢 리드클라이밍 (Lead Climbing)")

st.markdown("---")

st.header("리드클라이밍이란?")
st.write("""
리드클라이밍은 높은 암벽(보통 15m 이상)을 로프에 연결된 상태로 오르는 클라이밍 스포츠입니다.
클라이머는 오르면서 카라비너를 이용해 자신의 로프를 페그(금속 고정구)에 연결하여 
낙하 시 안전을 확보합니다. 기술, 체력, 심리적 강인함이 모두 필요한 종목입니다.
""")

st.header("리드클라이밍의 특징")

col1, col2 = st.columns(2)

with col1:
    st.subheader("장점")
    st.write("""
    ✅ **높은 난제들**: 다양한 높이와 난이도의 루트 도전
    
    ✅ **심리적 도전**: 높이와 위험에 대한 극복
    
    ✅ **인내력 발달**: 긴 루트 완주의 성취감
    
    ✅ **안전성**: 로프를 통한 안전 확보
    
    ✅ **팀워크**: 파트너와의 협력(빌레이어 필요)
    
    ✅ **올림픽 종목**: 국제 경기와 프로 활동 가능
    """)

with col2:
    st.subheader("필요한 것")
    st.write("""
    🧤 **클라이밍화**: 발가락이 강한 전문 신발
    
    🪢 **로프**: 움직임에 따라 움직이는 역동적 로프
    
    🔗 **카라비너**: 로프를 페그에 연결하는 장비
    
    ⛏️ **안전벨트**: 몸에 장착하는 안전 장비
    
    👥 **빌레이어**: 로프를 관리하는 파트너 필요
    
    🏪 **실내/실외 클라이밍 시설**: 적절한 환경
    """)

st.header("리드클라이밍의 장비")

st.subheader("1. 개인 보호구 (Personal Protective Equipment)")
st.write("""
- **안전벨트 (Harness)**: 몸에 착용하는 안전 장비
- **클라이밍화 (Climbing Shoes)**: 발의 그립 향상
- **분필 (Chalk)**: 손의 습기 제거
- **헬멧 (Helmet)**: 낙석이나 충돌로부터 보호
""")

st.subheader("2. 로프 시스템 (Rope System)")
st.write("""
- **동적 로프 (Dynamic Rope)**: 충격을 흡수하는 로프 (직경 9.2-10mm)
- **카라비너 (Carabiner)**: 금속 연결고리 (Locking/Non-locking)
- **페그/확보점 (Anchor/Bolts)**: 암벽에 고정된 금속 고리
- **로프 백 (Rope Bag)**: 로프 보관 및 운반
""")

st.subheader("3. 빌레이 장비 (Belay Device)")
st.write("""
- **오토블로커 (ATC, Gri-Gri)**: 로프를 관리하는 장치
- **빌레이 글로브**: 손 보호
- **로프 관리 기술**: 파트너의 안전을 보장하는 기술
""")

st.header("리드클라이밍 기술")

st.subheader("1. 클립 기술 (Clipping)")
st.write("""
- **로프 방향 주의**: 로프가 올바른 방향으로 페그 통과
- **빠른 클립**: 효율적이고 안전한 클리핑 동작
- **Z-클립 방지**: 로프 엉킴 방지
- **안정적 자세**: 클리핑 시 안정적 홀드 유지
""")

st.subheader("2. 체력 관리 (Endurance Management)")
st.write("""
- **페이싱**: 루트 전반에 걸친 에너지 분배
- **레스 (Resting)**: 홀드에서 휴식하는 기술
- **근육 회복**: 운동 중 호흡 조절
- **정신 집중**: 피로 상황에서의 집중력 유지
""")

st.subheader("3. 빌레이 기술 (Belay Technique)")
st.write("""
- **로프 관리 (Rope Management)**: 클라이머의 로프 속도 조절
- **안전기**: 클라이머가 추락할 때 즉시 로프 멈추기
- **명령어 사용**: 파트너와의 명확한 커뮤니케이션
- **주의 집중**: 항상 클라이머 감시
""")

st.header("리드클라이밍 안전 절차")

st.warning("""
🔴 **리드클라이밍 안전 체크리스트**:

1️⃣ **장비 점검**: 모든 장비(로프, 벨트, 카라비너) 확인
2️⃣ **기술 숙달**: 공인된 교육을 받고 자격 확보
3️⃣ **파트너 확인**: 숙련된 빌레이어와 함께 시작
4️⃣ **보이킹 (Voicing)**: "안녕하세요?" "준비됐나?" "등반중!" 등 표준 명령어 사용
5️⃣ **루트 확인**: 클라이밍 전 루트 살펴보기
6️⃣ **낙하 연습**: 안전한 환경에서 낙하 기술 연습
7️⃣ **정기 적검**: 장비를 정기적으로 검사 및 유지보수
""")

st.header("리드클라이밍 난이도 등급")

difficulty_data = {
    "등급": ["5.5", "5.6", "5.7", "5.8", "5.9", "5.10", "5.11", "5.12"],
    "설명": [
        "초보자: 기본 기술 학습 단계",
        "초보자: 낮은 높이에서의 안정감",
        "초중급: 기본 기술 숙달",
        "중급: 몸의 사용법 이해 필요",
        "중급: 기술과 체력 결합",
        "상급: 고난도 기술 요구",
        "상급: 체력과 정신력 극한",
        "엘리트: 세계적 수준의 클라이머 대상"
    ]
}

st.table(difficulty_data)

st.header("리드클라이밍의 훈련")

st.subheader("체력 훈련 프로그램")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("""
    **근력 훈련**
    - 핑거보드 운동
    - 풀-업
    - 손목 강화
    """)

with col2:
    st.write("""
    **지구력 훈련**
    - 긴 루트 연습
    - 체계적 반복
    - 회복 기간 관리
    """)

with col3:
    st.write("""
    **정신 훈련**
    - 긍정적 자기 대화
    - 불안 관리
    - 목표 설정
    """)

st.header("리드클라이밍과 올림픽")

st.info("""
🏅 **올림픽 스포츠 클라이밍**:

리드클라이밍은 2021년 도쿄 올림픽부터 정식 종목으로 편성되었습니다.
- 스피드클라이밍, 볼더링과 함께 복합 경기
- 세계 최고 수준의 클라이머들이 참가
- 국제 대회(월드컵, 세계선수권)에 참가 기회

**클라이밍을 경력으로 발전시킬 수 있습니다!**
""")

st.header("시작 가이드")

st.write("""
1. **교육 받기**: 공인된 클라이밍 스쿨에서 기본 기술 학습
2. **스터디 찾기**: 경험 많은 클라이머와 함께 시작
3. **점진적 도전**: 자신의 수준에 맞는 루트부터 시작
4. **커뮤니티 참여**: 클라이밍 커뮤니티에 참여하여 성장
5. **정기적 훈련**: 일관된 훈련으로 실력 향상
""")
