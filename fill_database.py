import db
import csv

pokedex = csv.DictReader(open("./Info/pokemon.csv", encoding = 'utf8'))
cursor = db.cursor


counter = 0

for row in pokedex:
  sql = "INSERT INTO pokemon VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

  values = (int(row['pokedex_number']),
            row['name'],
            int(row['attack']),
            row['classfication'],
            int(row['defense']),
            row['height_m'],
            int(row['hp']),
            int(row['speed']),
            row['type1'],
            row['type2'],
            row['weight_kg'],
            int(row['generation']),
            int(row['is_legendary'])
           )

  cursor.execute(sql,values)
  counter += 1
  print(counter, "Successed insert...")
  db.CONNECTION.commit()

db.CONNECTION.close()














  # # index = ['pokedex_number', 'name', 'attack', 'classfication', 'defense',        
  # #         'height_m', 'hp', 'speed', 'type1', 'type2', 'weight_kg', 'generation',
  # #         'is_legendary', 'abilities']

  

  # for i in range(index):    
  #   print(pokedex['pokedex_number'])