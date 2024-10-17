from flask import Flask, render_template, request, make_response, session, redirect, url_for
import os
from flask_mail import Mail, Message   
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, validators, ValidationError
from wtforms import IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name Of Student", [DataRequired("Please enter your name.")])
    
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])

    address = TextAreaField("Address")
    
    email = StringField("Email", [DataRequired("Please enter your email address."),
                                  Email("Please enter a valid email address.")])

    age = IntegerField("Age")
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])  
    submit = SubmitField("Send")
