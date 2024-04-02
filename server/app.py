#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>' 


@app.route('/print/<string:parameter>') 
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    result = [f'{str(i)}\n' for i in range(parameter)] 
    return ''.join(result)


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):

    valid_operations = {"+": '+' , "-": '-', "*": '*', "div": '/' , "%": '%'}

    if operation in valid_operations.keys():
        return str(eval(f'{num1} {valid_operations.get(operation)} {num2}'))
    else:
        return 'Invalid operation'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
