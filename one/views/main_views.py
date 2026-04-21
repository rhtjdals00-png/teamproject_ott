from flask import Blueprint, redirect, render_template, url_for, session

bp=Blueprint('home',__name__,url_prefix='/')

@bp.route('/')
def index():
    if session.get('user'):   # 🔥 로그인 상태 체크
        return redirect(url_for('home.main'))
    return render_template('main/home.html')

@bp.route('/home')
def home():
    # 127.0.0.1:5000/home 접속 시에도 같은 페이지를 보여주고 싶을 경우
    return render_template('main/home.html')

@bp.route('/main')
def main():
    return render_template('main/main.html')



