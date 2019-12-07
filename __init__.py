from flask import Flask, render_template, request, url_for
from src.Controller import Pokemon

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', title='Pokedex', 
                                       img=['https://assets.pokemon.com/assets/cms2/img/pokedex/full/00',
                                            'https://assets.pokemon.com/assets/cms2/img/pokedex/full/0',
                                            'https://assets.pokemon.com/assets/cms2/img/pokedex/full/']
                        )


app.run()




