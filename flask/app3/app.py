from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<var>')
def fun(var):
    return render_template('user.html', a = var)

if __name__ == '__main__':
    app.run(debug=True)