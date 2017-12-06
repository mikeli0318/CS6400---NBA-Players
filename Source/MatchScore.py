import MySQLdb
import numpy as np

from sklearn.metrics.pairwise import manhattan_distances

HOST = 'localhost'
PORT = '3306'
USER_NAME = 'root'
PASSWORD = 'root'
DB_NAME = 'NBA'

TABLE_PLAYER = 'Player'
TABLE_TEAM = 'Team'

def MatchScore(player_name):
    db = MySQLdb.connect(host=HOST, port=int(PORT), user=USER_NAME, passwd=PASSWORD, db=DB_NAME)
    cursor = db.cursor()
    sql = 'select distinct(TeamAbbr), avg(FGP), avg(3PP), avg(2PP), avg(FTP), avg((ORB/TRB)), avg((DRB/TRB)), \
                  avg(AST/(GAMES*5)), avg(STL/(GAMES*5)), avg(BLK/(GAMES*5)), avg(TOV/(GAMES*5)), avg(PF/(GAMES*5)) \
           from TeamStats\
           group by TeamAbbr;'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        teamStats = np.asarray(results)
        teamNames = teamStats[:,0]
        teamStats = teamStats[:, 1:].astype("float")
    except:
        print ("Unable to fetch data1")

    sql2 = "select FGP, 3PP, 2PP, FTP, (ORB/TRB), (DRB/TRB), \
            AST/Games, STL/Games, BLK/Games, TOV/Games, PF/Games\
            from Player where Name='" + player_name  + "';"
    try:
        cursor.execute(sql2)
        player = cursor.fetchone()
        playerStats = np.asarray(player).astype("float")
        playerStats = np.reshape(playerStats, (-1, teamStats.shape[1]))
    except:
        print ("Unable to fetch data2")

    pairwise_sim = manhattan_distances(playerStats, teamStats)
    ind = np.argpartition(pairwise_sim[0], -5)[-5:]
    print(pairwise_sim[0][ind])
    print(teamNames[ind])
    db.close()

def main():
    MatchScore("Derrick Rose")

if __name__ == "__main__":
    main()