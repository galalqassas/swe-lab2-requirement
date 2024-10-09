from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/display', methods=["POST"])
def display():
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template('display.html', email=email, password=password)


if __name__ == '__main__':
    app.run()
