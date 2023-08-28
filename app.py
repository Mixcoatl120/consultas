import re
from flask import Flask, render_template, request, url_for
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
@app.route('/', methods=('GET','POST'))# pagina de inicio con el metodo post y get para obtener la informacioan de
def home():
    return render_template('home.html')


@app.route('/consulta', methods=('GET','POST'))
def users():
    if request.method == 'POST':
        f1 = request.form['fecha_inicial'] #variable de fecha inicial
        f2 = request.form['fecha_final']# variable de fecha final
        mat = request.form['materia']#variable de materia

        print(con)
        print(f1)
        print(f2)
        print(mat)
    conn = conexion()
    cursor = conn.cursor()

    #consulta inicial con condicion de fechas 
    con_inicial = "SELECT seguimiento.fsolicitud, cat_tipo_ingreso.tipo_ingreso, cat_materia.materia, cat_tramites.cofemer,seguimiento.rnomrazonsolcial, dir_gral.siglas,cat_estatus.estatus   FROM seguimiento LEFT JOIN cat_tipo_ingreso ON seguimiento.tipo_ingreso = cat_tipo_ingreso.id LEFT JOIN cat_tipo_asunto ON seguimiento.tipo_asunto = cat_tipo_asunto.id LEFT JOIN cat_descripcion ON seguimiento.descripcion = cat_descripcion.id LEFT JOIN cat_materia ON seguimiento.materia = cat_materia.id LEFT JOIN cat_tramites ON seguimiento.tramite = cat_tramites.idtram LEFT JOIN cat_tipoinstalacion  ON seguimiento.tipoinstalacion = cat_tipoinstalacion.id LEFT JOIN cat_actividad ON seguimiento.cve_actividad = cat_actividad.id LEFT JOIN cat_personal AS evaluador ON seguimiento.nevaluador = evaluador.idpers LEFT JOIN cat_personal AS aar ON seguimiento.persona_ingresa = aar.idpers LEFT JOIN dir_gral ON seguimiento.dirgralfirma = dir_gral.id LEFT JOIN cat_sitact ON seguimiento.situacionactualtram = cat_sitact.id LEFT JOIN cat_sentido_resolucion ON seguimiento.sentido_resolucion = cat_sentido_resolucion.id LEFT JOIN cat_estatus ON seguimiento.estatus_tramite = cat_estatus.id WHERE (seguimiento.fsolicitud >= " + "'" + f1 + "'" + " and seguimiento.fsolicitud <= " + "'" + f2 + "')" 
    #string con condiciones tipo de ingreso
    #con_tipoingreso = 
    #string con dicion de materia
    con_materia = "and materia ='" + mat + "' "
    #string con las condiciones de direccion general
    #con_dirgeneral =
    #string con la tentencia final completa
    #query = con_inicial + " " +con_tipoingreso + " " + con_materia + " " + con_dirgeneral + "; " 
    users = cursor.fetchall(query)       
    conn.close()
    return render_template('consulta.html', users=users)


#prueba de cambio de pagina
#@app.route('/FAT')
#def consultas():
    #conn = conexion()
    #cursor = conn.cursor()
    # consulta con select de prueba
    #cursor.execute("SELECT fsolicitud,bitacora_expediente,rnomrazonsolcial,rfc FROM seguimiento WHERE fsolicitud = '2023-07-17'")
    #users = cursor.fetchall()
    #conn.close()
    #return render_template('tabla_prueba.html', users=users)

#inicio de aplicacion
if __name__ == '__main__':
    app.run(debug = True)
