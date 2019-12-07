from modules import db
import csv

def insert():
    pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
    cursor = db.cursor

    abilities = []
    remove = "[]"

    for row in pokedex:

      ability = row['abilities']

      for i in range(len(remove)):
        ability = ability.replace(remove[i], "")

        if i == 1:
          abilities.append(ability.split(", "))
  
    diferent_abilities = []

    for i in range(len(abilities)):
      length = len(abilities[i])
      for j in range(length):

        if abilities[i][j].replace("'", "") not in diferent_abilities:
          diferent_abilities.append(abilities[i][j].replace("'", ""))
          print(abilities[i][j].replace("'", ""))
    
    
    cursor = db.cursor
    sql = "INSERT INTO abilities (name) VALUE (%s)"

    for i in range(len(diferent_abilities)):
       value = (diferent_abilities[i])
       cursor.execute(sql, value)
       db.CONNECTION.commit()








    
       

          
        
        

