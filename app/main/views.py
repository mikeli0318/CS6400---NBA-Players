from flask import render_template, request
#bluprint main
from . import main, Similarity, teamUtil
import MySQLdb

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@main.route('/simPlayer', methods=['GET', 'POST'])
def getSimPlayer():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    playerName = splitted[0]
    for i in range(1, len(splitted) - 1):
        playerName = playerName + " " + splitted[i]

    players = Similarity.FindTopKSimilar(playerName)
    return render_template('simPlayers.html', result = players)

@main.route('/simTeam', methods=['GET', 'POST'])
def getSimTeam():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    playerName = splitted[0]
    for i in range(1, len(splitted) - 1):
        playerName = playerName + " " + splitted[i]

    players = Similarity.getSimilarTeams(playerName)
    return render_template('simTeam.html', result = players)

@main.route('/teamPerform', methods=['GET', 'POST'])
def getTeamPerform():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    teamName = splitted[0]
    for i in range(1, len(splitted) - 1):
        teamName = teamName + " " + splitted[i]

    players = teamUtil.getTeamPerformance(teamName)
    return render_template('teamPerform.html', result = players)