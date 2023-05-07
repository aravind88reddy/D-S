from flask import Flask, render_template,session
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/user')
def fun():
    return render_template('user.html')
@app.route('/s')
def fun1():
    if not session.get('notes'):
        return redirect('user.html')
    return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=True)