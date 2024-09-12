from flask import Flask, render_template, request,send_file
import psycopg2
from Funciones import imp_excel
from dbModel import * 

#Funciones relacionados con las rutas html
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Jvm2OrrMd4QaRNHzvtgqfxyLir8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mixcoatl120.@localhost/siset'

# database
db.init_app(app)
#Home
@app.route('/', methods=('GET','POST'))# pagina de inicio con el metodo post y get para obtener la informacioan de
def Index():
    # consultas a la db
    items =  Materia.query.all() # consulta a materia.
    tip_ingr = Tip_ing.query.order_by(Tip_ing.id).all() # consulta a tipo ingreso
    dir_gen = Dir_Gen.query.filter_by(cve_unidad = 2).all() # consuta a direccion general
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
        print(mat)  

    #consulta inicial esto es para la tabla que se visualiza en html 
    resultados = (db.session.query(
        Seguimiento.fsolicitud,
        Tip_ing.tipo_ingreso,
        Seguimiento.bitacora_expediente,
        Materia.materia,
        Seguimiento.rnomrazonsolcial,
        Dir_Gen.siglas,
        Estatus.estatus
    ).join(Tip_ing,Seguimiento.tipo_ingreso == Tip_ing.id)
    .join(Asunto,Seguimiento.tipo_asunto == Asunto.id)
    .join(Descripcion,Seguimiento.descripcion == Descripcion.id)
    .join(Materia,Seguimiento.materia == Materia.id)
    .join(Tramite,Seguimiento.tramite == Tramite.idtram)
    .join(Dir_Gen,Seguimiento.dirgralfirma == Dir_Gen.id)
    .join(Estatus,Seguimiento.estatus_tramite == Estatus.id)
    .filter(Seguimiento.fsolicitud >= f1,Seguimiento.fsolicitud <= f2)
    .order_by(Seguimiento.fsolicitud).all()
    )
    #print(resultados)
    # string con la condicion de fecha
    #con_fechas = "(seguimiento.fsolicitud >= " + "'" + f1 + "'" + " and seguimiento.fsolicitud <= " + "'" + f2 + "')"
    # string con condiciones tipo de ingreso
    #if ti != "":
    #    con_tipoingreso = ti +")"
    # string con dicion de materia
    #if mat != "TODO":
    #    con_materia = "and cat_materia.materia ='" + mat + "'"
    #else:
    #    con_materia = ""
    # string con las condiciones de direccion general
    #if dg !="":
    #    con_dirgeneral =dg + ")"
    #else:
    #    con_dirgeneral = ""
    # string con la sentencia final completa
    #query = str(resultados) + " " + con_fechas + " " +con_tipoingreso + " " + con_materia + " " + con_dirgeneral
    #print(query)
    # string con condiciones para la funcion de exportar excel
    #con_where = con_fechas + " " +con_tipoingreso + " " + con_materia + " " + con_dirgeneral
    
    #funcion para realizar una consulta y crear un archivo en excel para su descarga
    #imp_excel(con_where)
    return render_template('consulta.html', resultados = resultados)

@app.route('/download')
def Download_File():
    #ruta para descargar el archivo
    PATH='source/Consulta.xlsx'
    return send_file(PATH,as_attachment=True,)

# inicio de la aplicacion
if __name__ == '__main__':
    app.run()
