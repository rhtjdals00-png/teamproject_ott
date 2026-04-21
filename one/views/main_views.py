from flask import Blueprint, redirect, render_template, url_for, session
from ..models import Video, Plan

bp=Blueprint('home',__name__,url_prefix='/')

@bp.route('/')
def index():
    if session.get('user'):
        return redirect(url_for('home.main'))

    video_list = Video.query.order_by(Video.video_unique_id.desc()).all()
    plan_list = Plan.query.order_by(Plan.price.asc()).all()

    return render_template(
        'main/home.html',
        video_list=video_list,
        plans=plan_list
    )

@bp.route('/home')
def home():
    # 127.0.0.1:5000/home 접속 시에도 같은 페이지를 보여주고 싶을 경우
    return render_template('main/home.html')

@bp.route('/main')
def main():
    return render_template('main/main.html')



