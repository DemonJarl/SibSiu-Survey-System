from flask import render_template, flash, redirect, url_for, request
from app import db, app
#from app.models import 
#from app.forms import 

#тут происходит обработка страниц

@app.route('/')
def index():
        return render_template('404.html')
