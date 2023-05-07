from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def fun1():
    return render_template('index.html')

@app.route('/about')
def fun2():
    cars = ['nexon','punch','harrier','safari','hexa']
    return render_template('about_us.html',input = cars)

if __name__ == '__main__':
    app.run(debug=True)