from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@127.0.0.1/thegyanmate'
db = SQLAlchemy(app)


class Contacts(db.Model):
    """
    date, email, mesg, name, sno, ph_no
    """
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)
    mesg = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    ph_no = db.Column(db.String(13), nullable=False)




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        """Add Entry to the db"""
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        mesg = request.form.get('mesg')

        entry = Contacts(name = name, email = email, ph_no = phone, mesg = mesg, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True)
