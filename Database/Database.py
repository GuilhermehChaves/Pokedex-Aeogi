import pymysql

# Import do database
# from Database import database
# database.Database('localhost', 'root', '', 'pokedex')
class Database:

  def __init__(self,host,user,password,database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    
  def getDb(self):
    return self.db

  def connect(self):
    self.db = pymysql.connect(self.host, self.user, self.password, self.database)
  
  def close(self):
    self.db.close()

  



