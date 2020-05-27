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
    return "Your name is"+name




@app.route('/')
def home():
    return "Hello World"



@app.route('/home')
def home_page():
    return "home Information"





if __name__ == "__main__":
    app.run(debug=True)
