from modules import db
import csv

pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
cursor = db.cursor




def savePokemons():
  counter = 0
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
    print(counter, "Successed insert...")
    db.CONNECTION.commit()

def getDiferentTypes():
  types = []

  for row in pokedex:  
    if row['type1'] not in types:
      types.append(row['type1'])

    if row['type2'] not in types:
      types.append(row['type2'])

  return types


def saveTypes():
  types = getDiferentTypes()
  print(len(types))

  for i in range(len(types)):
    sql = "INSERT INTO type (name) VALUE(%s)"
    value = (types[i])
    print(types[i])

    cursor.execute(sql, value)
    print('Successed insert...')
    db.CONNECTION.commit()


print('Inserting Pokemons...')
savePokemons()
print('Inserting Types...')
saveTypes()
