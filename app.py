
from flask import Flask
import nltk
app = Flask(__name__)
@app.route("/")
def tabs_information():
    return "chrome driver not working on cloud we'll fix it."




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
    app.run()
