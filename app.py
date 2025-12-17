from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 포트폴리오 데이터 (여기서 내용을 수정하세요)
    data = {
        "profile": {
            "name": "홍길동",
            "title": "Python Backend Developer",
            "email": "hello@example.com",
            "github": "github.com/yourid",
            "blog": "blog.example.com"
        },
        "about": {
            "intro": "안녕하세요. 효율적인 코드를 사랑하는 개발자입니다.",
            "desc": "Python과 웹 기술을 활용하여 사용자에게 가치를 전달하는 서비스를 만듭니다. 새로운 기술을 배우고 적용하는 것을 즐깁니다.",
            "skills": ["Python", "Flask", "Django", "SQL", "Git"]
        },
        "career": [
            {"period": "2024.01 - 현재", "company": "프리랜서 개발자", "role": "웹 서비스 외주 개발"},
            {"period": "2022.03 - 2023.12", "company": "OOO 테크", "role": "백엔드 개발팀 인턴"}
        ],
        "works": [
            {"title": "포트폴리오 사이트", "desc": "Flask로 제작한 개인 웹사이트", "tag": "Web"},
            {"title": "데이터 분석 툴", "desc": "주식 데이터 자동 수집 및 분석", "tag": "Data"},
            {"title": "사내 메신저 봇", "desc": "업무 자동화 슬랙 봇 개발", "tag": "Automation"},
            {"title": "미니 게임", "desc": "Pygame을 활용한 슈팅 게임", "tag": "Game"}
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
