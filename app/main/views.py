from flask import render_template
#bluprint main
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('experiment_main.html')

@main.route('/similarPlayer', methods=['GET', 'POST'])
def hhh():
    names = ['A', 'B', 'C', 'D']
    return render_template('experiment_simPlayers.html', result = names)

