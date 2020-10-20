class LoginForm(FlaskForm):
	username = StringField ('username', validators=[InputRequired(message='A username is required!'), Length(min=5, max=10, message="Must be longer")])
	password = PasswordField('password',validators=[InputRequired('Password is required!'), AnyOf(values=['password', 'secret'])])
	recaptcha = RecaptchaField()