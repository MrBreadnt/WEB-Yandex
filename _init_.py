from flask import Flask, request, url_for, render_template
import json
import hashlib

password = 'pa$$w0rd'
h = hashlib.md5(password.encode())
print(h.hexdigest())

app = Flask(__name__)
app.config['SECRET_KEY'] = "YGHBJdfDG^Dd7g7gh{}P{OU*&*shb"


@app.route('/')
@app.route('/index')
def index():
    return "<a href='/game'>Игра<a>"


@app.route('/game', methods=['POST', 'GET'])
def game():
    if request.method == 'GET':
        return render_template("game.html")
    elif request.method == 'POST':
        print(request.json["letter"])
        return request.json["letter"]


@app.route('/gettest/<name>', methods=['GET'])
def gettest(name):
    if request.method == 'GET':
        return open(url_for('static', filename=f"4545JYGghfjdgfjmfkaerhg/{name}.json"), "rb").read()


@app.route('/static/4545JYGghfjdgfjmfkaerhg/', methods=['GET'])
def st():
    if request.method == 'GET':
        return "0"


if __name__ == '__main__':
    app.run(host="192.168.0.7")
