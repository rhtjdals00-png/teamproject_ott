from flask import Blueprint, redirect, render_template


bp=Blueprint('home',__name__,url_prefix='/')

@bp.route('/home')
def home():
    return render_template("main/home.html")
