from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def fun_1():
    return render_template('index.html')

@app.route('/about')
def fun_2():
    return render_template('about.html')

@app.route('/contact')
def fun_3():
    return render_template('contact.html')

@app.route('/register')
def fun_4():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
