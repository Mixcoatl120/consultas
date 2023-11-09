from flask import Flask, render_template, request,send_file
from flask_bootstrap import Bootstrap
import psycopg2
from Funciones import imp_excel
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
def Index():
   # conexion con la db 
    conn = conexion()
    cursor = conn.cursor()
    # consultas a la db
    cursor.execute("SELECT materia FROM cat_materia")
    items = cursor.fetchall()
    #
    cursor.execute("SELECT tipo_ingreso FROM cat_tipo_ingreso order by id")
    tip_ingr = cursor.fetchall()
    #
    cursor.execute("select siglas from cat_dirgeneral where cve_unidad = 2")
    dir_gen = cursor.fetchall()
    # cierre de la db
    cursor.close()
    conn.close()
    
    return render_template('index.html', items=items, tip_ingr=tip_ingr,dir_gen=dir_gen)


@app.route('/consulta', methods=('GET','POST'))
def users():
    con_tipoingreso = ""
    if request.method == 'POST':
        f1 = request.form['fecha_inicial'] #variable de fecha inicial
        f2 = request.form['fecha_final']# variable de fecha final
        mat = request.form['materia']# variable de materia
        ti = request.form['ta']# variable con condiciones de tipo ingreso
        dg = request.form['dg']# variables con condiciones de direccion general

        print(ti)
        print(dg)  

    conn = conexion()
    cursor = conn.cursor()

    #consulta inicial esto es para la tabla que se visualiza en html 
    con_inicial = "SELECT" + \
    " seguimiento.fsolicitud," + \
    " cat_tipo_ingreso.tipo_ingreso," + \
    "seguimiento.bitacora_expediente," + \
    " cat_materia.materia," + \
    " seguimiento.rnomrazonsolcial," + \
    " dir_gral.siglas," + \
    " cat_estatus.estatus" + \
    " FROM seguimiento" + \
    " LEFT JOIN cat_tipo_ingreso ON seguimiento.tipo_ingreso = cat_tipo_ingreso.id" + \
    " LEFT JOIN cat_tipo_asunto ON seguimiento.tipo_asunto = cat_tipo_asunto.id" + \
    " LEFT JOIN cat_descripcion ON seguimiento.descripcion = cat_descripcion.id" + \
    " LEFT JOIN cat_materia ON seguimiento.materia = cat_materia.id" + \
    " LEFT JOIN cat_tramites ON seguimiento.tramite = cat_tramites.idtram" + \
    " LEFT JOIN cat_tipoinstalacion  ON seguimiento.tipoinstalacion = cat_tipoinstalacion.id" + \
    " LEFT JOIN cat_actividad ON seguimiento.cve_actividad = cat_actividad.id" + \
    " LEFT JOIN cat_personal AS evaluador ON seguimiento.nevaluador = evaluador.idpers" + \
    " LEFT JOIN cat_personal AS aar ON seguimiento.persona_ingresa = aar.idpers" +\
    " LEFT JOIN dir_gral ON seguimiento.dirgralfirma = dir_gral.id" + \
    " LEFT JOIN cat_sitact ON seguimiento.situacionactualtram = cat_sitact.id" + \
    " LEFT JOIN cat_sentido_resolucion ON seguimiento.sentido_resolucion = cat_sentido_resolucion.id" + \
    " LEFT JOIN cat_estatus ON seguimiento.estatus_tramite = cat_estatus.id" + \
    " WHERE"

    # string con la condicion de fecha
    con_fechas = "(seguimiento.fsolicitud >= " + "'" + f1 + "'" + " and seguimiento.fsolicitud <= " + "'" + f2 + "')"
    # string con condiciones tipo de ingreso
    if ti != "":
        con_tipoingreso = ti +")"
    # string con dicion de materia
    if mat != "TODO":
        con_materia = "and cat_materia.materia ='" + mat + "'"
    else:
        con_materia = ""
    # string con las condiciones de direccion general
    if dg !="":
        con_dirgeneral =dg + ")"
    else:
        con_dirgeneral = ""
    # string con la sentencia final completa
    query = con_inicial + " " + con_fechas + " " +con_tipoingreso + " " + con_materia + " " + con_dirgeneral
    # string con condiciones para la funcion de exportar excel
    con_where = con_fechas + " " +con_tipoingreso + " " + con_materia + " " + con_dirgeneral
    
    #funcion para realizar una consulta y crear un archivo en excel para su descarga
    imp_excel(con_where)
    #
    cursor.execute(query)
    users = cursor.fetchall()      
    
    conn.close()
    return render_template('consulta.html', users=users)

@app.route('/download')
def Download_File():
    #ruta para descargar el archivo
    PATH='source/Consulta.xlsx'
    return send_file(PATH,as_attachment=True,)

# inicio de la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
