from modules import db
import csv


def insert():
  pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
  cursor = db.cursor
  counter = 0

  print("Inserting pokemon...")
  
  for row in pokedex:
    sql = "INSERT INTO pokemon VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    values = (int(row['pokedex_number']),
              row['name'],
              int(row['attack']),
              row['classfication'],
              int(row['defense']),   
              row['height_m'],
              int(row['hp']),
              int(row['speed']),
              row['weight_kg'],
              int(row['is_legendary']),
              int(row['generation'])
            )

    cursor.execute(sql,values)
    counter += 1
    db.CONNECTION.commit()