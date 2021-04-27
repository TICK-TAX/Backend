from flask import Flask, render_template, request, jsonify  , url_for , flash, redirect
from flask_sqlalchemy import SQLAlchemy  
from  datetime import datetime
from flask_pymongo import PyMongo
from forms import RegistrationForm, LoginForm
from datetime import datetime






app = Flask(__name__ , template_folder='template', static_folder="static")
app.config['SECRET_KEY'] = '7c22cdd8fc00ed5188a0f2d98f972990'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ticktax'
db=SQLAlchemy(app)

class Profile(db.Model):

    # sno. name email dob contactno.
    sno = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(40), unique=False, nullable=False)
    email= db.Column(db.String(150), unique=False, nullable=False)
    dob = db.Column(db.Integer, unique=True, nullable=False)
    contactno = db.Column(db.Integer, unique=True, nullable=False)





@app.route('/',  methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        password = request.form.get('password')

    return render_template('index.html')
    #return 'Hello, World!'


  
@app.route('/home.html', methods=["GET", "POST"])
def homepage():
    return render_template('home.html')



@app.route('/profile.html', methods=['GET', 'POST'])
def page():  
    if  request.method == 'POST':
        name = request.form["fullname"]
        email = request.form["email"]
        dob = request.form["DOB"]
        contactNumber= request.form["ContactNumber"]
        # Gender = request.form["Gender"]
        print(name + " " + email + " " + dob)
    return render_template('profile.html')

@app.route('/profile2.html', methods=["GET", "POST"])
def profile2_page():
    if request.method == "POST":
        HouseNo = request.form.get("house/flat No.")
        StreetNo = request.form.get("treet/sector/area")
        City = request.form.get("City")
        State = request.form.get("State")
    return render_template('profile2.html')

@app.route('/profile3.html', methods=["GET", "POST"])
def profile3_page():
    if request.method == "POST":
        source = request.form.get("Source of income")
        other = request.form.get('Asset')
    return render_template('profile3.html')



@app.route('/calculator.html', methods=["GET", "POST"])
def calculator_page():
    if request.method== "POST":
        income= request.form.get("income from salary")
        incomeasset= request.form.get("income from other sources")
    
    
    return render_template('calculator.html')


@app.route('/calculator3.html', methods=["GET", "POST"])
def calculator3_page():

#     if request.method == "POST":
     return render_template("calculator3.html")


@app.route('/calculator2.html', methods=["GET", "POST"])
def calculator2_page():



    return render_template('calculator2.html')


@app.route('/payments.html', methods=["GET", "POST"])
def payements_page():
    return render_template('payments.html')



@app.route('/payments2.html', methods=["GET", "POST"])
def payments2_page():
    return render_template('payments2.html')


@app.route('/payments3.html', methods=["GET", "POST"])
def payemnts3_page():
    return render_template('payments3.html')

@app.route('/documents.html', methods=["GET", "POST"])
def documents_page():
    return render_template('documents.html')

@app.route('/navigation.html', methods=["GET", "POST"])
def navigation_page():
    return render_template('navigation.html')

@app.route('/calendar.html', methods=["GET", "POST"])
def calendar_page():
    return render_template('calendar.html')


@app.route('/dashboard.html', methods=["GET", "POST"])
def dashboard_page():
    return render_template('dashboard.html')


if  __name__ == "__main__":
    app.run(debug=True, port=8000)  
    
