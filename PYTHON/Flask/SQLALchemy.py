from flask import Flask, render_template, request, redirect, url_for, request, session, flash,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY']='random string'
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    pin = db.Column(db.String(10))
    
    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin
        
@app.route('/')
def home():
    return render_template("show.html")

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please enter all the fields', 'error')
        else:
            user = users(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('home'))
    return render_template("new.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
