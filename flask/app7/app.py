from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def fun2():
    return 'this is post request'

@app.route('/')
def fun1():
    return 'this is get request'

if __name__ == '__main__':
    app.run(debug=True)