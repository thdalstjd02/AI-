import streamlit as st

# 1. 페이지 기본 설정 (탭 이름, 아이콘 등)
st.set_page_config(
    page_title="나의 포트폴리오",
    page_icon="🎨",
    layout="wide"
)

# 2. 사이드바 메뉴 만들기
menu = st.sidebar.radio(
    "MENU",
    ["HOME", "자기소개", "내 작품(램프)", "방명록"]
)

# --- [1] HOME 화면 ---
if menu == "HOME":
    st.title("환영합니다! 👋")
    st.subheader("미디어콘텐츠학과 송민성의 포트폴리오입니다.")
    st.write("---")
    st.write("왼쪽 메뉴를 눌러 저의 소개와 작품들을 감상해보세요.")
    
    # 메인 이미지 (가지고 계신 사진 파일명으로 바꾸세요)
    # st.image("main_photo.jpg", use_column_width=True) 
    st.info("이곳은 저의 창작물과 아이디어를 기록하는 공간입니다.")

# --- [2] 자기소개 화면 ---
elif menu == "자기소개":
    st.title("About Me 🧑‍💻")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # 프로필 사진이 있다면 "profile.png"로 업로드 후 주석(#) 제거
        # st.image("profile.png", width=200)
        st.write("📷 (여기에 본인 사진을 넣으세요)")

    with col2:
        st.subheader("송민성 (Student)")
        st.write("""
        - **소속**: 미디어콘텐츠학과
        - **관심 분야**: 모션 그래픽, 영상 편집, 파이썬 개발
        - **사용 툴**: Adobe Premiere, After Effects, Illustrator, Blender
        """)
        st.success("안녕하세요! 영상과 코딩으로 새로운 가치를 만드는 크리에이터입니다.")

# --- [3] 내 작품 (램프 프로젝트) ---
elif menu == "내 작품(램프)":
    st.title("Project: 램프의 요정 🧞‍♂️")
    st.write("제가 파이썬으로 직접 구현한 인터랙티브 기능입니다.")
    st.write("---")

    # === [램프 기능 코드 시작] ===
    # 세션 상태 초기화
    if 'show_face' not in st.session_state:
        st.session_state['show_face'] = False

    def toggle_face():
        st.session_state['show_face'] = not st.session_state['show_face']

    # 중앙 정렬을 위해 컬럼 사용
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.session_state['show_face']:
            # 얼굴 나온 상태
            try:
                st.image("face.png", caption="짜잔! 제가 나왔습니다.", width=400)
            except:
                st.error("face.png 이미지가 없습니다! 파일을 업로드해주세요.")
            st.button("다시 숨기기", on_click=toggle_face, use_container_width=True)
        else:
            # 램프 상태
            try:
                st.image("lamp.png", caption="신비한 램프입니다.", width=400)
            except:
                st.error("lamp.png 이미지가 없습니다! 파일을 업로드해주세요.")
            st.button("램프 줄 당기기!", on_click=toggle_face, use_container_width=True)
    # === [램프 기능 코드 끝] ===

# --- [4] 방명록 화면 ---
elif menu == "방명록":
    st.title("Contact & Guestbook 📧")
    
    st.write("저에게 궁금한 점이나 남기고 싶은 말이 있다면 적어주세요!")
    
    with st.form("guestbook_form"):
        name = st.text_input("이름")
        message = st.text_area("메시지")
        
        submitted = st.form_submit_button("보내기")
        
        if submitted:
            st.write(f"✅ **{name}**님, 메시지가 전송되었습니다: {message}")
            st.caption("(실제 전송 기능은 데이터베이스 연동이 필요합니다. 지금은 체험만 가능해요!)")
