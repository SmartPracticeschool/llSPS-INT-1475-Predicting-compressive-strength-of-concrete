from flask import Flask,render_template,request
import pickle 
import numpy as np

model = pickle.load(open('compressive strength.pkl','rb'))

app =Flask (__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=['POST'])
def login():
     cement =request.form['cement']
     furnace= request.form['furnace']
     flyash= request.form['flyash']
     water= request.form['water']
     superr= request.form['super']
     coarse= request.form['coarse']
     fine= request.form['fine']
     age= request.form['age']
     
     strength = [[cement,furnace,flyash,water,superr,coarse,fine,age]]
     ypred1 = model.predict(np.array(strength))
     
     
     return render_template("index.html",showcase =ypred1)
 

if __name__=='__main__':
    app.run(debug =False)
