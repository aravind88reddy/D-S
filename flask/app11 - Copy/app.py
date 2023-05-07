from flask import Flask, render_template,request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["POST",'GET'])
def index():
    if request.method=='POST':
        note = request.form.get("note")
        session['notes'].append(note)
   
    if ('notes' not in session) :
      session['notes'] = []
    return render_template("home.html",notes = session['notes']) 

if __name__ == '__main__':
    app.run(debug=True)