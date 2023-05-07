from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def fun_1():
    return render_template('index.html')
 
@app.route('/thankyou',methods=['GET','POST'])
def fun_2():
    if request.method=='POST':
        email = request.form.get('in_1')
        age = request.form.get('in_2')
        return render_template('thankyou.html',e = email,a = int(age))
    
    return 'please register'

if __name__ == '__main__':
    app.run(debug=True)