from flask import Flask, request, render_template

web = Flask(__name__)


@web.route('/', methods=['GET', 'POST'])
def Home():
    return render_template('home.html')


@web.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@web.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == '123456':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='username and password is error', username=username)


if __name__ == '__main__':
    web.run()
