from flask import Blueprint, redirect, url_for, render_template

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/test')
def test():
    return render_template('mypage/test.html')

@bp.route('/terms')
def term():
    return render_template('mypage/term.html')