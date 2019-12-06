from modules import db
import csv

def insert():
  pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
  cursor = db.cursor
  types = []

  for data in pokedex:

    if data['type1'] not in types:
      types.append(data['type1'])

    if data['type2'] not in types:
      types.append(data['type2'])
  
  print("Inserting type...")

  for i in range(len(types)):
    sql = "INSERT INTO type (name) value (%s)"
    value = (types[i])

    cursor.execute(sql, value)
    db.CONNECTION.commit()