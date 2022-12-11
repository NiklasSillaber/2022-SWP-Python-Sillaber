import mysql.connector as db
from sqlalchemy import null
import errno

class RepositoryDB():
    
    def __init__(self):
        self.con = null
        self.cursor = null
        
    def connect(self):
        
        if hasattr(self.con, 'is_connected'):
                if not self.con.is_connected():
                    try:
                        self.con = db.connect(
                            host = 'localhost', 
                            user = 'root', 
                            passwd = '',
                            database = 'schere')
            
                        self.cursor = self.con.cursor()

                    except db.Error as err:
                        print("Can't connect to DB: " + str(err))
        else:
            try:
                self.con = db.connect(
                    host = 'localhost', 
                    user = 'root', 
                    passwd = '', 
                    database = 'schere')
    
                self.cursor = self.con.cursor()

            except db.Error as err:
                print("Can't connect to DB: " + str(err))
    
    
    def disconnect(self):
        
        if hasattr(self.con, 'is_connected'):
                if self.con.is_connected():
                    self.cursor.close()
                    self.con.close()
        
        
    def insertStatistics(self, stat):
        
        if hasattr(self.con, 'is_connected'):
            if self.con.is_connected():
    
                sqlstatement1 = 'INSERT INTO statData (name, wins, draws, schere, stein, papier, spock, echse) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                val1 = ('PLAYER', stat['PLAYER'][0], stat['PLAYER'][1], stat['PLAYER'][2], stat['PLAYER'][3], stat['PLAYER'][4], stat['PLAYER'][5], stat['PLAYER'][6])
                sqlstatement2 = 'INSERT INTO statData (name, wins, draws, schere, stein, papier, spock, echse) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                val2 = ('COMP', stat['COMP'][0], stat['COMP'][1], stat['COMP'][2], stat['COMP'][3], stat['COMP'][4], stat['COMP'][5], stat['COMP'][6])
                
                try:
                    self.cursor.execute(sqlstatement1, val1)
                    self.cursor.execute(sqlstatement2, val2)
                    self.con.commit()
                    return True
                
                except db.IntegrityError:
                    return False
            else:
                return False
        else:
            return False

    
    def deleteStatistics(self):
        
        if hasattr(self.con, 'is_connected'):
            if self.con.is_connected():
                
                sqlstatement = 'delete from statData'

                try:
                    self.cursor.execute(sqlstatement)
                    self.con.commit()
                    return True
                
                except db.IntegrityError:
                    return False
            else:
                return False
        else:
            return False
    
    def getStatistics(self):
        
        statistics = {}
        
        if hasattr(self.con, 'is_connected'):
            if self.con.is_connected():
                
                sqlstatement = 'SELECT * FROM statData'

                self.cursor.execute(sqlstatement)
                result = self.cursor.fetchall()
                
                if len(result) != 0:
                    for dbSet in result:
                        data = [dbSet[1], dbSet[2], dbSet[3], dbSet[4], dbSet[5], dbSet[6], dbSet[7]]
                        statistics.update({dbSet[0]: data})
                else:
                    statistics = {"PLAYER" : [0, 0, 0, 0, 0, 0, 0], "COMP" : [0, 0, 0, 0, 0, 0, 0]}
                
        return statistics 


if __name__ == '__main__':
    #statistics = {"PLAYER" : [0, 0, 0, 5, 3, 0, 0], "COMP" : [0, 2, 0, 0, 0, 0, 0]}
    rep = RepositoryDB()
    rep.connect()
    #rep.insertStatistics(statistics)
    #rep.deleteStatistics()
    #stat = rep.getStatistics()
    #print(stat)
    #rep.disconnect()
    