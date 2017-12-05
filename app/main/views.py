from flask import render_template
#bluprint main
from . import main

@main.route('/')
def index():
    return render_template('index.html')