from flask import Flask, request, jsonify, render_template, redirect, url_for, session,request 
from flask_sqlalchemy import SQLAlchemy
import hashlib
import os
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class ToDo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(500),nullable=False)
    description=db.Column(db.String(100))
    time = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.time}"
    
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        todo = ToDo(title=title,description=description)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    all_todo = ToDo.query.all()
    
    return render_template('index.html' ,all_todo=all_todo)
# todo = ToDo(title="First Task",description="This is the first task")
    # db.session.add(todo)
    # db.session.commit()
@app.route('/add')
def add():
    all_todo = ToDo.query.all()
    print(all_todo)
    return 'Added'
    

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)