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
    due_date = db.Column(db.DateTime)
    
    def __repr__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.time} - {self.due_date}"
    
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        if due_date:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        else:
            due_date = None
        
        todo = ToDo(title=title,description=description ,due_date=due_date)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    all_todo = ToDo.query.all()
    
    return render_template('index.html' ,all_todo=all_todo)
# todo = ToDo(title="First Task",description="This is the first task")
    # db.session.add(todo)
    # db.session.commit()
    
@app.route('/delete/<int:id>')
def delete(id):
    todo = ToDo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        
        todo = ToDo.query.filter_by(id=id).first()
        todo.title = title
        todo.description = description
        if due_date:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
            todo.due_date = due_date
        else:
            todo.due_date = None
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    todo = ToDo.query.filter_by(id=id).first()
    return render_template('update.html',todo=todo)
    
@app.route('/add')
def add():
    all_todo = ToDo.query.all()
    print(all_todo)
    return 'Added'
    

if __name__ == '__main__':
    
    #db.create_all()
    app.run(debug=True)
