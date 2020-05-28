import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
classifier = KNeighborsClassifier(n_neighbors=1, algorithm = 'brute')


app = Flask(__name__)
#PreProcessing


def tokenize(text):
    text = text.lower()
    tokens=text.split(" ")
    updated = []
    for item in tokens:
        updated.append(item)
    return updated



@app.route('/predict')
def result():
    
    filename = 'knn_bot.pkl'
    model_pickle = pickle.load(open(filename,'rb'))
    filename1 = 'tfidf.pkl'
   # tfidf_vect = pickle.load(open(filename1,'rb'))
    df = pd.read_csv('Updated_Dataset.csv')
    df = df.drop(['Unnamed: 0'], axis=1)
    user_response = "What is a leveraged buyout?"
    test = ["Hello",user_response]
    tfidf_vect = TfidfVectorizer(tokenizer = tokenize , stop_words = 'english')
    tfidf_test = tfidf_vect.fit_transform(test.values.astype(str))
    y_pred = model_pickle.predict(tfidf_test[1])
    #return df['Answer'][y_pred[0]]
    return "Hello Worl2"


@app.route('/')
def home():
    return "Hello World"



@app.route('/home')
def home_page():
    return "home Information"





if __name__ == "__main__":
    app.run(debug=True)
