from flask import render_template, request
#bluprint main
from . import main, Similarity, teamUtil, wikiUtil, MatchScore

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

    teamsTmp = MatchScore.MatchScore(playerName)
    if len(teamsTmp) == 0:
        return render_template('WrongInput.html')
    teams = []
    urls = []
    for team in teamsTmp:
        teamName = teamUtil.map[team]
        teams.append(teamName)
        urls.append(wikiUtil.getWikiUrl(teamName))
    return render_template('simTeam.html', result = teams, playerName = playerName, urls = urls)

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