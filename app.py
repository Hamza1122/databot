from flask import Flask
import pickle
import nltk
from pattern.en import lemma, lexeme
import pandas as pd
import string
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1, algorithm = 'brute')

app = Flask(__name__)

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


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


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
   # return ' name is ' + name
    
if __name__ == '__main__':
    app.run()
