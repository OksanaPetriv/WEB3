from flask import Flask, render_template
from app import app

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

class LoginForm(FlaskForm):
	username = StringField ('username', validators=[InputRequired(message='A username is required!'), Length(min=5, max=10, message="Must be longer")])
	password = PasswordField('password',validators=[InputRequired('Password is required!'), AnyOf(values=['password', 'secret'])])
	recaptcha = RecaptchaField()


@app.route('/form', methods=['GET', 'POST'])
def form():
	form=LoginForm()

	if form.validate_on_submit():
		return '<h1> The username is {}. The password is {}.'.format(form.username.data, form.password.data)
	return render_template('form.html', form=form)

