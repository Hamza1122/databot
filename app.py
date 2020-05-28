import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#PreProcessing
def tokenize(text):
    text = text.lower()
    tokens = text.split(" ")
    updated = []
    for item in tokens:
        updated.append(item)
    return updated



#Testing
def response(question):
    test = ["Hello",question]
    tfidf_test = tfidf_vect.transform(test)
    h = 0;
    h_i = 0;
    for i in range(len(tfidf_train.A)):
        cos_lib = cosine_similarity(tfidf_test[1], tfidf_train[i])
        if cos_lib > h :
            h = cos_lib
            h_i = i
    return df['Answer'][h_i]

def greeting(text):
    for i in range(len(greetings)):
        if greetings[i].lower() == text.lower():
            return Responses[i]
    return 0


from flask import Flask
app = Flask(__name__)
@app.route("/")
def tabs_information():
    return "chrome driver not working on cloud we'll fix it."

@app.route("/data1")
def data1():
    df = pd.read_csv('Updated_Dataset.csv')
    df = df.drop(['Unnamed: 0'], axis=1)
    tfidf_vect = TfidfVectorizer(tokenizer = tokenize , stop_words = 'english')
    tfidf_train = tfidf_vect.fit_transform(df['Question'].values.astype(str))
    greetings = ["how are you?","hi","hello", "How is it going?","How are you doing?","Nice to meet You","how do you do?","What's up?"]
    Responses = ["I am Good","Hello","hi", "Good","Very well, thanks.","Thankyou","I am doing well","The sky's up but I'm fine thanks. What about you?"]
    user_response ="User: Is a bussiness plan important?"
    user_response=user_response.lower()
    if(user_response!='bye'):
      if(user_response=='thanks' or user_response=='thank you' ):
        print("ROBO: You are welcome..")
      else:
        resp = greeting(user_response)
        if(resp!=0):
          print("ROBO: "+greeting(user_response))
        else:
          print("ROBO: ",end="")
          print(response(user_response))
    else:

      print("ROBO: Bye! take care..")
    return "chrome driver not working on cloud we'll fix it"




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


@app.route('/test')
def test_quizzes():
    name1="Hello"
    return name1
    
    

@app.route('/Roster')
def roster():
    return "Roster"


@app.route('/messages')
def messages():
    return "message"



@app.route('/test_quize')
def test():
    return '''<p>
    What is the Tests & Quizzes tool?<br>
    How do I create an assessment in Tests and Quizzes?<br>
    How do I create a new assessment using markup text or cut and paste?<br>
    How do I create a new question (with the assessment builder)?<br>
    How do I create a multiple choice question?<br>
    How do I create a matching question?<br>
    How do I create a true/false question?<br>
    How do I create a short answer/essay question?<br>
    How do I create a fill in the blank question?<br>
    How do I create a numeric response question?<br>
    How do I create a calculated question?<br>
    How do I create a hot spot question?<br>
    How do I create a survey?<br>
    How do I create a student audio response question?<br>
    How do I create a file upload question?<br>
    How to I add multiple parts to an assessment?<br>
    </p>'''


@app.route('/Dropbox')
def dropbox():
    return '''<p>
    What is the Drop Box tool?<br>
    How do I upload files to multiple dropbox folders?<br>
    How do students add items to the Drop Box?<br>
    How do I download multiple files from Dropbox?<br>
    
    </p>'''

        

@app.route('/syllabus')
def syallabus():
    return '''<p>
    What is the Syllabus tool?<br>
    How do I add my syllabus as a file attachment?<br>
    How do I create a syllabus using cut and paste from a document?<br>
    How do I edit syllabus items?<br>
    How do I create a multi-part syllabus based on number of items needed?<br>
    How do I create a multi-part syllabus by dates?<br>
    How do I print the syllabus?<br>
    How do I point my syllabus to a webpage?<br>
    How do I rearrange syllabus items?<br>
    How do I pubish/unpublish a syllabus item?<br>
    How do I add a syllabus item to the calendar?<br>
    How do I change syllabus item access?<br>
    How do I delete a syllabus item?<br>
    </p>'''




@app.route('/assignment')
def assignment():
    return '''
    What is the Assignments tool?
    How do I add an assignment?
    How do I edit an existing assignment?
    How do I enable student peer review for an assignment?
    How do I enable group submissions for an assignment?
    How do I delete an assignment?
    How do students submit an assignment?
    How do I submit an assignment on behalf of a student?
    How do I grade an assignment?
    How do students complete a peer assessment assignment?
    How do I grade a peer review assignment
    How do I download assignments for grading offline?
    How do I upload graded assignment submissions and feedback?
    How do I release assignment grades?
    How do students view their assignment feedback?
    How do I change the Assignments tool permissions?
    '''

@app.route('/announcement')
def announcement():
    return '''<p>
    What is the Assignments tool?<br>
    What is the Announcements tool?<br>
    How do I add an announcement?<br>
    How do I edit an announcement?<br>
    How do I delete an announcement?<br>
    How do I merge announcements?<br>
    How do I reorder announcements?<br>
    How do I change Announcements tool permissions?<br>
    How do I view announcements?<br>
    </p>'''


if __name__ == "__main__":
    app.run()
