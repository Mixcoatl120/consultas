from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html')
#'<h1>hola mundo</h1> <button type="button" class="btn btn-primary btn-sm">Consultas</button>'

if __name__ == '__main__':
    app.run(debug = True)
