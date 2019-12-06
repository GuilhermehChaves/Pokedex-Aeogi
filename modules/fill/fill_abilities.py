from modules import db
import csv

def insert():
    pokedex = csv.DictReader(open("./src/Info/pokemon.csv", encoding = 'utf8'))
    cursor = db.cursor

    abilities = []
    remove = "[],"

    for row in pokedex:

      ability = row['abilities']

      for i in range(len(remove)):
        print(ability)
        ability = ability.replace(remove[i], "")

       

          
        
        

