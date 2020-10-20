#!/usr/bin/python
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY']='Thisisasecret!'
app.config['RECAPTCHA_PUBLIC_KEY']='6LcaltkZAAAAAMVhrZRp-4un99FyxKlzyyfa7YfR'
app.config['RECAPTCHA_PRIVATE_KEY']='6LcaltkZAAAAAKJaGzZHSRbohu22y2bnu9Ti7ANv'
app.config['TESTING']= True

from app import views