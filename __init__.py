from flask import Flask, render_template, request, url_for
from src.Controller import Pokemon, Type

app = Flask(__name__)

@app.route('/')
def index():

  pokemons = Pokemon.selectAll()
  types = Type.selectAll()

  return render_template('index.html', title='Pokedex', 
                                       img=['https://assets.pokemon.com/assets/cms2/img/pokedex/full/00',
                                            'https://assets.pokemon.com/assets/cms2/img/pokedex/full/0',
                                            'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'],
                                      pokemons = pokemons,
                                      types = types)




@app.route('/pokemon/<string:search>', methods = ["GET"])
def pokemon(search):

  pokemon = Pokemon.selectOne(search)
  title = pokemon[0]['name']

  return render_template('pokemon.html', title=title,
                                         pokemon=pokemon,
                                         img=['https://assets.pokemon.com/assets/cms2/img/pokedex/full/00',
                                              'https://assets.pokemon.com/assets/cms2/img/pokedex/full/0',
                                              'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'] )
app.run()




