from flask import Flask, render_template, request, jsonify  , url_for , flash, redirect, abort 
from flask_sqlalchemy import SQLAlchemy  
from  datetime import datetime
from flask_pymongo import PyMongo
from forms import RegistrationForm, LoginForm
from datetime import datetime
from CalculationManager import CalculationManager






app = Flask(__name__ , template_folder='template', static_folder="static")
app.config['SECRET_KEY'] = '7c22cdd8fc00ed5188a0f2d98f972990'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['STRIPE_PUBLIC_KEY']= 'pk_test_51IjQ9zSC7Z8k5EKQviIiZmr42H6MepB3FAXFyrpJDC7OzRJV8Q3gu5bV8GkNnsOhLTvWdH8KRcIy4fkgyLVYoazw00xYS6pB0W'

app.config['STRIPE_SECTRET_KEY']='sk_test_51IjQ9zSC7Z8k5EKQi24kRVnOmw1NPfP38FIcZElRFFg5EEvGiCeb6XENsMyJ7VIVotAL8sJ3PAEJWT9SqMuvTFda00nDRcDfdh'

db=SQLAlchemy(app)





class Profile(db.Model):

    # sno. name email dob contactno.
    sno = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(40), unique=False, nullable=False)
    email= db.Column(db.String(150), unique=False, nullable=False)
    DOB = db.Column(db.Integer, unique=True, nullable=False)
    contactno = db.Column(db.Integer, unique=True, nullable=False)


    def __repr__(self):
        return '<Post %r>' % self.name



@app.route('/',  methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        password = request.form.get('password')
        
    return render_template('index.html')
    #return 'Hello, World!'

@app.route('/index.html', )
def index_page():
    return render_template('index.html')

  
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
        
        entry=Profile(name=name, email=email, DOB=dob, contactno=contactNumber)
        db.session.add(entry)
        

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



@app.route("/tax.html", methods=['GET'])
def redirection():
    return redirect(url_for('tax_calculator'))


@app.route("/count", methods=['GET'])
def tax_calculator():
    provided_salary = request.args.get('providedSalary')
    show_description = request.args.get('showDescription')

    if not provided_salary:
        return render_template('tax.html', result=None)

    try:
        int(provided_salary)
    except ValueError:
        abort(400)


    calculation_manager = CalculationManager(float(provided_salary))
    calculation_manager.count_tax_0()
    calculation_manager.count_tax_5()
    calculation_manager.count_tax_10()
    calculation_manager.count_tax_15()
    calculation_manager.count_tax_20()
    calculation_manager.count_tax_25()
    calculation_manager.count_tax_30()


    calculation_manager.count_salary_after_taxes()

    return render_template('tax.html',
                           result=calculation_manager.get_result(),
                           provided_salary=provided_salary,
                           calculation_manager=CalculationManager,
                           show_description=show_description)



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

@app.route('/finances.html', methods=["GET", "POST"])
def navigation_page():
    return render_template('finances.html')

@app.route('/calendar.html', methods=["GET", "POST"])
def calendar_page():
    return render_template('calendar.html')


@app.route('/dashboard.html', methods=["GET", "POST"])
def dashboard_page():
    return render_template('dashboard.html')


if  __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000)  
    
