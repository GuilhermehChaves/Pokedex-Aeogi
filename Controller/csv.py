class Csv:

  def read():
    import csv

    with open('./Info/pokemon.csv') as csv_file:
      data = csv.reader(csv_file, delimiter = ',')
      counter = 0

      pokedex_number = []
      name = []
      attack = []
      classfication = []
      defence = []
      height_m = []
      hp = []
      speed = []
      type1 = []
      type2 = []
      weight_kg = []
      generation = []
      is_legendary = []
      abilities = []


      for row in data:
        if counter != 0:

          pokedex_number.append(int(row[0]))
          name.append(row[1])
          attack.append(int(row[2]))
          classfication.append(row[3])
          defence.append(int(row[4]))
          height_m.append(row[5])
          hp.append(int(row[6]))
          speed.append(int(row[7]))
          type1.append(row[8])
          type2.append(row[9])
          weight_kg.append(row[10])
          generation.append(int(row[11]))
          is_legendary.append(int(row[12]))
          abilities.append(row[13])
        counter += 1

      pokedex = {}
      pokedex['pokedex_number'] = pokedex_number
      pokedex['name'] = name
      pokedex['attack'] = attack
      pokedex['classification'] = classfication
      pokedex['defence'] = defence
      pokedex['height_m'] = height_m
      pokedex['hp'] = hp
      pokedex['speed'] = speed
      pokedex['type1'] = type1
      pokedex['type2'] = type2
      pokedex['weight_kg'] = weight_kg
      pokedex['generation'] = generation
      pokedex['is_legendary'] = is_legendary
      pokedex['abilities'] = abilities

      return pokedex


