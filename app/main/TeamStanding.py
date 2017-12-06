import MySQLdb
import numpy as np

HOST = 'localhost'
PORT = '3306'
USER_NAME = 'root'
PASSWORD = 'root'
DB_NAME = 'NBA'

TABLE_PLAYER = 'Player'
TABLE_TEAM = 'Team'

def TeamStanding(team_name):
    db = MySQLdb.connect(host=HOST, port=int(PORT), user=USER_NAME, passwd=PASSWORD, db=DB_NAME)
    cursor = db.cursor()
    sql = "select TeamStats.* from TeamStats, Team \
            where TeamAbbr = Abbr \
            and Franchise='" + team_name + "';"
    try:
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return []
        results = cursor.fetchall()
        teamStats = np.asarray(results)
    except:
        print ("Unable to fetch data1")
    db.close()
    print(teamStats)
    return teamStats.tolist()

def main():
    TeamStanding("Houston Rockets")

if __name__ == "__main__":
    main()