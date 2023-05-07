from flask import Flask, render_template,request
import re
import pandas
app = Flask(__name__)

 
@app.route('/',methods=['POST','GET'])
def fun():
    if request.method=='POST':
        target = request.form.get('in_1')
        regex = request.form.get('in_2')
        lst = re.findall(regex,target)
        lst1 = len(lst)
        return render_template('home.html',lst=lst,lst1=lst1)
    return render_template('home.html')    

if __name__ == '__main__':
    app.run(debug=True)



