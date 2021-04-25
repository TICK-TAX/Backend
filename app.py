from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy  
from  datetime import datetime
import sqlite3
import datetime 
import stripe
import os

app = Flask(__name__ , template_folder='template', static_folder="C:\\Project\\static")








@app.route('/',  methods=["GET", "POST"])
def home_page():

    print("hello world")
    return render_template('index.html')
    #return 'Hello, World!'







@app.route('/',  methods=["GET", "POST"])
def index_page():
    if request.method == "GET":
        print("hello")
    else: 
        print("bye")
    return render_template('index.html')


@app.route('/home.html', methods=["GET", "POST"])
def homepage():
    return render_template('home.html')



@app.route('/profile.html', methods=["GET", "POST"])
def profile_page():
    if request.method == 'POST':
        name = request.form['Full Name']
        print(name)
    return render_template('profile.html')

@app.route('/profile2.html', methods=["GET", "POST"])
def profile2_page():
    return render_template('profile2.html')

@app.route('/profile3.html', methods=["GET", "POST"])
def profile3_page():
    return render_template('profile3.html')



@app.route('/finances.html', methods=["GET", "POST"])
def finances_page():
    return render_template('finances.html')

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

@app.route('/calander.html', methods=["GET", "POST"])
def calendar_page():
    return render_template('calander.html')


@app.route('/dashboard.html', methods=["GET", "POST"])
def dashboard_page():
    return render_template('dashboard.html')


if  __name__ == "__main__":
    app.run(debug=True, port=8000)  
