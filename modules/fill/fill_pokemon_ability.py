from modules import db
import csv

def insert():
    pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
    cursor = db.cursor
    remove = "[]"

    print("Inserting pokemon_ability...")
      
    for row in pokedex:

      ability = row['abilities']

      for i in range(len(remove)):
        ability = ability.replace(remove[i], "")

        if i == 1:

          abilities = []
          abilities.append(ability.split(", "))

          
          for j in range(len(abilities[0])):
            cursor = db.cursor
            sql = "SELECT id FROM abilities WHERE name = %s"
            value = (abilities[0][j].replace("'", ""))

            cursor.execute(sql, value)
            ability_id = cursor.fetchone()

            sql = "INSERT INTO pokemon_ability (pokemon_number, ability_id) VALUES (%s, %s)"
            values = (row['pokedex_number'], ability_id['id'])

            cursor.execute(sql, values)
            db.CONNECTION.commit()



            
      