from flask import render_template, request
# bluprint main
from . import main, Similarity, teamUtil, wikiUtil, MatchScore, TeamStanding


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
    return render_template('simPlayers.html', result=players, urls=urls)


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
    return render_template('simTeam.html', result=teams, playerName=playerName, urls=urls)


@main.route('/teamPerform', methods=['GET', 'POST'])
def getTeamPerform():
    name = str(request.args.get('name'))
    splitted = name.split("SPLITTER")
    teamName = splitted[0]
    for i in range(1, len(splitted) - 1):
        teamName = teamName + " " + splitted[i]
    performance = TeamStanding.TeamStanding(teamName)
    if len(performance) == 0:
        return render_template('WrongInput.html')
    season = [performance[1][0], performance[2][0]]
    comment = []
    if int(performance[1][3]) > int(performance[0][3]):
        comment.append("Ascending")
    else:
        comment.append("Descending")
    if int(performance[2][3]) > int(performance[1][3]):
        comment.append("Ascending")
    else:
        comment.append("Descending")

    return render_template('teamPerform.html', result=performance, teamName=teamName, season=season, comment=comment)
