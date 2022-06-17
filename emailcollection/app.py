#########################
#                       #
#       Imports         #
#                       #
#########################
# importing flask, redirect for try/except, render template, url for and request for the POST
# importing SQL for the database
# importing datetime for the date_created column, not necessarily needed


from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#########################
#                       #
#   Variables/Classes   #
#                       #
#########################

# naming app for the init
# naming the database

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)

# setting db class/model - specifying the columns needed, the data type, and if they can be null. 
# can now refer to data as Person.name etc
class Person(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String (150),nullable=False)
    number = db.Column(db.String (1000), nullable=False)
    course = db.Column(db.Integer, nullable = False)
    market = db.Column(db.String (100), nullable=True)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<Asset %r>' % self.id

#########################
#                       #
#        Routes         #
#                       #
#########################

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        person_name = request.form['name']
        person_email = request.form['email']
        person_number = request.form['number']
        person_course = request.form['course']
        marketing_allowed=request.form.get('market')

        new_item= Person(name=person_name,email=person_email,number=person_number,course=person_course, market=marketing_allowed)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('thanks'))
        except:
            return 'There was an issue with adding the item'
    else:
        person = Person.query.all()
        return render_template('index.html',person=person)

@app.route('/view')
def viewing():
    person = Person.query.all()
    return render_template('view.html',person=person)

@app.route('/thanks')
def thanks():
    person = Person.query.all()
    last=person[-1]
    return render_template('thanks.html',name=last)

#########################
#                       #
#     Initialsing       #
#                       #
#########################

if __name__=="__main__":
    app.run(debug=True)