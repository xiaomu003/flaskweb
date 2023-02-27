from flask import Blueprint, render_template, session, url_for, request
from werkzeug.utils import redirect

login = Blueprint('login', __name__)


@login.route('/login', methods=['POST', 'GET'])
def logins():
    if request.method == 'POST':
        username = request.form['username']  # 获取姓名文本框的输入值
        password = request.form['password']  # 获取密码框的输入值
        print(username, password)
        if username == '123' and password == '123':
            session['username'] = username  # 使用session存储方式，session默认为数组，给定key和value即可
            return redirect(url_for('index'))  # 重定向跳转到首页
        else:
            return 'the username or user password does not match!'
    return render_template("login.html")


@login.route('/spop', methods=['POSTR', 'GET'])
def spop():
    if request.method == 'GET':
        if session.get('username', None):
            session.pop('username')
    return redirect(url_for('index'))


