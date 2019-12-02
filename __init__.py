from flask import Flask, render_template, request, url_for
from Controller.pokemon import Pokemon

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', titulo='Pokedex')


app.run()




