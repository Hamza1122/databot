import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import string
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1, algorithm = 'brute')


app = Flask(__name__)

#PreProcessing
def tokenize(text):
    text = text.lower()
    #tokens = nltk.word_tokenize(text)
    tokens=text.split(" ")
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
    return df['Answer'][y_pred[0]]





@app.route('/')
def home():
    return "Hello World"



@app.route('/home')
def home_page():
    return "home Information"





if __name__ == "__main__":
    app.run(debug=True)
