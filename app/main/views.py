from flask import render_template, request
#bluprint main
from . import main, Similarity, teamUtil, wikiUtil

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
    if len(players) == 0:
        return render_template('WrongInput.html')
    urls = []
    for player in players:
        urls.append(wikiUtil.getWikiUrl(player))
    return render_template('simPlayers.html', result = players, urls = urls)

@main.route('/simTeam', methods=['GET', 'POST'])
def getSimTeam():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    playerName = splitted[0]
    for i in range(1, len(splitted) - 1):
        playerName = playerName + " " + splitted[i]

    teams = Similarity.getSimilarTeams(playerName)
    if len(teams) == 0:
        return render_template('WrongInput.html')
    urls = []
    for team in teams:
        urls.append(wikiUtil.getWikiUrl(team))
    return render_template('simTeam.html', result = teams, playerName = playerName)

@main.route('/teamPerform', methods=['GET', 'POST'])
def getTeamPerform():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    teamName = splitted[0]
    for i in range(1, len(splitted) - 1):
        teamName = teamName + " " + splitted[i]

    players = teamUtil.getTeamPerformance(teamName)

    #check empty
    return render_template('teamPerform.html', result = players)