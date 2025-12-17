from flask import Flask, render_template

app = Flask(__name__)

# 메인 페이지 라우팅
@app.route('/')
def home():
    # 실제 데이터는 여기서 관리하여 HTML로 보낼 수 있습니다.
    user_info = {
        "name": "홍길동",
        "title": "Python Developer & Creator",
        "email": "email@example.com",
        "github": "github.com/username"
    }
    return render_template('index.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)
