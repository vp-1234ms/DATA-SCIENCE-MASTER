from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world1():
    return "Hello, World1!"

@app.route("/hello2")
def hello_world2():
    return "Hello, World2!"

@app.route("/chintu")
def hello_world3():
    return "My Best Friend!"

@app.route("/python")
def test():
    a=5+6
    return f"This my first fun in flask {a}"

@app.route("/vaib")
def myfunc():
    data=request.args.get('x')
    return f"This is your input {data}"

if __name__=="__main__":
    app.run(host="0.0.0.0")


