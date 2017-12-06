import MySQLdb
import numpy as np
#from DBConnectionConfig import *

from sklearn.metrics.pairwise import cosine_similarity

#hard code
HOST = 'localhost'
PORT = '3306'
USER_NAME = 'root'
PASSWORD = 'root'
DB_NAME = 'NBA'

TABLE_PLAYER = 'Player'
TABLE_TEAM = 'Team'
#hard code ends

def FindTopKSimilar(player_name):
    db = MySQLdb.connect(host=HOST, port=int(PORT), user=USER_NAME, passwd=PASSWORD, db=DB_NAME)
    cursor = db.cursor()
    sql = 'select distinct(Name), avg(age), sum(Games), sum(GS), sum(MP), sum(FG), sum(FGA), avg(FGP) IS NOT NULL, \
		          sum(3P), sum(3PA), avg(3PP) IS NOT NULL, sum(2P), sum(2PA), avg(2PP) IS NOT NULL, avg(EPGP) IS NOT NULL, \
                  sum(FT), sum(FTA), sum(FTP) IS NOT NULL, sum(ORB), sum(DRB), sum(TRB), sum(AST), sum(STL), \
                  sum(BLK), sum(TOV), sum(PF), sum(PTS) \
            from Player  \
            group by Name;'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        players = np.asarray(results)
        Names = players[:,0]
        players = players[:, 1:].astype("float")
    except:
        print ("Unable to fetch data")
    pairwise_sim = cosine_similarity(players, None)
    nonZero = np.nonzero(Names == player_name)
    if nonZero[0].shape[0] == 0:
        return []
    PlayerIndex = nonZero[0][0]
    ind = np.argpartition(pairwise_sim[PlayerIndex], -5)[-5:]
    print (pairwise_sim[PlayerIndex][ind])
    print (Names[ind])
    db.close()
    return Names[ind].tolist()

def main():
    FindTopKSimilar("Derrick Rose")

def getSimilarPlayers(playerName):#place holder
   return ['A', 'B', 'C', 'D', playerName]

def getSimilarTeams(playerName):# p h
   return ['A', 'B', 'C', 'D', playerName]

if __name__ == "__main__":
    main()