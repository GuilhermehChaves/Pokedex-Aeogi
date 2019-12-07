from modules import db

def selectAll():
  cursor = db.cursor
  sql = "SELECT * FROM pokemon"
  cursor.execute(sql)
  pokemons = cursor.fetchall()
  db.CONNECTION.commit()
  
  return pokemons

  