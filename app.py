from flask import Flask
from flask_boostrap import Bostrap

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return '<h1>hola mundo</h1> <button type="button" class="btn btn-primary btn-sm">Small button</button>'

@app.route('/consultas')
def consulta():
    return '<h1>Consultas</h1>'
