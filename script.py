#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    #return "Hello World"

#prediction function
def ValuePredictor(to_predict_dict):
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict_dict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_dict = request.form.to_dict()
        to_predict_dict['age'] = int(to_predict_dict['age'])
        to_predict_dict['yearsatcompany'] = int(to_predict_dict['yearsatcompany'])
        to_predict_dict['yearsofexperience'] = int(to_predict_dict['yearsofexperience'])
        result = ValuePredictor(to_predict_dict)
        result = int(result)

        return render_template("result.html",prediction=result)

if __name__ == "__main__":
	app.run(debug=True)