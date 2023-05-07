from flask import Flask, render_template, request,redirect
import random
import string
import os
import pyperclip
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
path = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class All_urls(db.Model):
    __tablename__='urls'
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.Text)
    short_url = db.Column(db.Text)

    def __init__(self, short_url,original_url):
        self.short_url = short_url
        self.original_url = original_url     
    def __repr__(self):
        return 'ORIGINAL URL-{} SHORT URL-{}'.format(self.original_url, self.short_url)



@app.route('/')
def home_get():
    return render_template('home.html')
    

@app.route('/', methods=['POST','GET'])
def home_post():
    if request.method=='POST':    
        short_url = random.choice(string.ascii_letters)+ str(random.randint(1,999))
        original_url = request.form.get('in_1')
        c = pyperclip.copy(short_url)
        all_urls = All_urls(short_url,original_url)
        db.session.add(all_urls)
        db.session.commit()
    return render_template('home.html',short_url = short_url,c=c,o=original_url) 


@app.route('/history')
def history_get():
    urls = All_urls.query.all()
    return render_template('history.html',urls = urls)


@app.route('/a/<short>')
def fun(short):
    a = All_urls.query.filter_by(short_url = short)
    for i in a:
        return redirect(i.original_url)

if __name__ == "__main__":
    app.run(debug=True)
