from modules import db
import csv

def insert():
  pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
  cursor = db.cursor

  print("Inserting pokemon_type...")

  for data in pokedex:
    sql = "SELECT id FROM type WHERE name = %s"
    value = (data['type1'])

    cursor.execute(sql, value)
    type_id = cursor.fetchone()
      
    db.CONNECTION.commit()

    sql = "INSERT INTO pokemon_type (pokemon_number, type_id) values (%s, %s)"
    values = (data['pokedex_number'], type_id['id'])

    cursor.execute(sql, values)
    db.CONNECTION.commit()

