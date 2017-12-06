from flask import render_template, request
#bluprint main
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@main.route('/simPlayer', methods=['GET', 'POST'])
def hhh():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    playerName = splitted[0]
    for i in range(1, len(splitted) - 1):
        playerName = playerName + " " + splitted[i]

    players = 1#
    return render_template('simPlayers.html', result = players)

@main.route('/simTeam', methods=['GET', 'POST'])
def hhh():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    playerName = splitted[0]
    for i in range(1, len(splitted) - 1):
        playerName = playerName + " " + splitted[i]

    players = ['A', 'B', 'C', 'D', playerName]
    return render_template('simTeam.html', result = players)

@main.route('/teamPerform', methods=['GET', 'POST'])
def hhh():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    playerName = splitted[0]
    for i in range(1, len(splitted) - 1):
        playerName = playerName + " " + splitted[i]

    players = ['A', 'B', 'C', 'D', playerName]
    return render_template('teamPerform.html', result = players)