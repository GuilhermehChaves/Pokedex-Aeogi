from modules import db
import csv
import numpy as np

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
  

    abilities = np.asarray(abilities)
    print(len(abilities))
    print(len(abilities[10]))
    abilities.reshape(-1, 3)



    # for i in range(len(abilities)):
    #   print(abilities[i])
    

       

          
        
        

