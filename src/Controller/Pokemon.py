from modules import db

def selectAll():
  cursor = db.cursor
  sql = "SELECT * FROM pokemon"
  cursor.execute(sql)
  pokemons = cursor.fetchall()
  db.CONNECTION.commit()
  
  return pokemons

def selectOne(search):
  cursor = db.cursor
  sql = "SELECT * FROM pokemon WHERE pokedex_number = %s OR name = %s"
  values = (search, search)
  cursor.execute(sql, values)
  pokemons = cursor.fetchall()
  db.CONNECTION.commit()
  
  return pokemons