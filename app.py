from flask import Flask, render_template, request
from covid_india import states
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        state = request.form['State']
        if state:
            data = states.getdata(state)
        return render_template("result.html",data=data, state=state)

if __name__ == '__main__':
   app.run(debug = True)