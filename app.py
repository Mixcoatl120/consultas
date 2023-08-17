from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import psycopg2

#Credenciales para la coneccion de la base de datos.
db_config = {
    'dbname': 'siset',
    'user': 'postgres',
    'password': 'Asea2023',
    'host': 'localhost',
    'port': '5432'
}
#estableciondo la coneccion.
def conexion():
    conn = psycopg2.connect(**db_config)
    return conn

#Funciones relacionados con las rutas html
app = Flask(__name__)
bootstrap = Bootstrap(app)
#Home
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def users():
    conn = conexion()
    cursor = conn.cursor()

    # consulta con select de prueba
    cursor.execute("SELECT fsolicitud,bitacora_expediente,rnomrazonsolcial,rfc FROM seguimiento where fsolicitud ='2023-07-17'")
    users = cursor.fetchall()
    conn.close()
    return render_template('users.html', users=users)

#prueba de cambio de pagina
@app.route('/consultas')
def consultas():
    conn = conexion()
    cursor = conn.cursor()

    # consulta con select de prueba
    cursor.execute("SELECT fsolicitud,bitacora_expediente,rnomrazonsolcial,rfc FROM seguimiento where rfc='GNM9712017P7'")
    users = cursor.fetchall()
    conn.close()
    return render_template('consultas.html', users=users)

#
if __name__ == '__main__':
    app.run(debug = True)
