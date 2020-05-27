import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import string
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1, algorithm = 'brute')


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#PreProcessing
def tokenize(text):
    text = text.lower()
    #tokens = nltk.word_tokenize(text)
    words=text.split()
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in words]
    print(tokens)
    updated = []
    for item in tokens:
        updated.append(lemma(item))
    return updated

@app.route('/predict/<name>')
def result(name):



    filename = 'knn_bot.pkl'
    classifier = pickle.load(open(filename, 'rb'))
    filename1 = 'tfidf.pkl'
    tfidf_vect = pickle.load(open(filename1,'rb'))
    df = pd.read_csv('Updated_Dataset.csv')
    df = df.drop(['Unnamed: 0'], axis=1)
    user_response = name#"What is a leveraged buyout?"

    test = ["Hello",user_response]
    tfidf_test = tfidf_vect.transform(test)
    y_pred = classifier.predict(tfidf_test[1])
    return name





@app.route('/')
def home():
    return "Hello World"

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
