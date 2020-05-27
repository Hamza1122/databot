import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))



@app.route('/home')
def home_page():
    return "home Information"


@app.route('/course_registraion')
def course_registration():
    return "Registraion Information"



@app.route('/Attendance')
def attendance():
    return "Attendance Information"


@app.route('/marks')
def marks():
    return "marks Information"


@app.route('/transcript')
def transcript():
    return "Transcript Information"

@app.route('/fee_challan')
def fee_challan():
    return "Challan Information"


@app.route('/fee_details')
def fee_details():
    return "Transcript Information"


@app.route('/course_feedback')
def course_feedback():
    return "Course feedback Information"


@app.route('/tentative_')
def tentative_studyplan():
    return "Tentatie Study Plan"





if __name__ == "__main__":
    app.run(debug=True)
