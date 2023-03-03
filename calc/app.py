# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def addPage():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    print(a)
    return str(a + b)

@app.route('/sub')
def subPage():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a - b)

@app.route('/mult')
def multPage():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a * b)

@app.route('/div')
def divPage():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(a / b)

@app.route('/math/<op>')
def mathPage(op):
    a = int(request.args['a'])
    b = int(request.args['b'])
    if op == 'add':
        return str(a + b)
    elif op == 'sub':
        return str(a - b)
    elif op == 'mult':
        return str(a * b)
    elif op == 'div':
        return str(a / b)
    else:
        return "not sure what that is.."