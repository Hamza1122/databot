import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
 
classifier = KNeighborsClassifier(n_neighbors=1, algorithm = 'brute')


app = Flask(__name__)
#PreProcessing


def tokenize(text):
    text = text.lower()
    #tokens = nltk.word_tokenize(text)
    tokens=text.split(" ")
    updated = []
    for item in tokens:
        updated.append(item)
    return updated

def response(question):
    test = ["Hello",question]
    cv=CountVectorizer()
    word_count_vector=cv.fit_transform(test)
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_vect=tfidf_transformer.fit(word_count_vector)
    tfidf_test = tfidf_vect.transform(test)
    y_pred = classifier.predict(tfidf_test[1])
    return df['Answer'][y_pred[0]]


@app.route('/predict')
def result():
    
    filename = 'knn_bot.pkl'
    classifier = pickle.load(open(filename,'rb'))
    filename1 = 'tfidf.pkl'
   # tfidf_vect = pickle.load(open(filename1,'rb'))
    df = pd.read_csv('Updated_Dataset.csv')
    df = df.drop(['Unnamed: 0'], axis=1)
    user_response = "What is a leveraged buyout?"
    bot_response = response(user_response)
    return "Hello Worl2"


@app.route('/')
def home():
    return "Hello World"



@app.route('/home')
def home_page():
    return "home Information"





if __name__ == "__main__":
    app.run(debug=True)
