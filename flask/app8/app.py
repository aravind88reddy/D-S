from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def fun_1():
    return render_template('index.html')
@app.route('/thankyou',methods=['GET','POST'])
def fun_2():
    if request.method=='GET':
        return 'thanks for get register'
    return 'thanks for post register'
if __name__ == '__main__':
    app.run(debug=True)