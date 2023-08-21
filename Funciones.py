import pandas as pd
import psycopg2


#Credenciales para la coneccion de la base de datos.
db_config = {
    'dbname': 'siset',
    'user': 'postgres',
    'password': 'Asea2023',
    'host': 'localhost',
    'port': '5432'
}

def conexion():
    conn = psycopg2.connect(**db_config)
    return conn

def crear_excel():
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT seguimiento.fsolicitud, cat_tipo_ingreso.tipo_ingreso, cat_materia.materia, cat_tramites.cofemer,seguimiento.rnomrazonsolcial, dir_gral.siglas,cat_estatus.estatus   FROM seguimiento LEFT JOIN cat_tipo_ingreso ON seguimiento.tipo_ingreso = cat_tipo_ingreso.id LEFT JOIN cat_tipo_asunto ON seguimiento.tipo_asunto = cat_tipo_asunto.id LEFT JOIN cat_descripcion ON seguimiento.descripcion = cat_descripcion.id LEFT JOIN cat_materia ON seguimiento.materia = cat_materia.id LEFT JOIN cat_tramites ON seguimiento.tramite = cat_tramites.idtram LEFT JOIN cat_tipoinstalacion  ON seguimiento.tipoinstalacion = cat_tipoinstalacion.id LEFT JOIN cat_actividad ON seguimiento.cve_actividad = cat_actividad.id LEFT JOIN cat_personal AS evaluador ON seguimiento.nevaluador = evaluador.idpers LEFT JOIN cat_personal AS aar ON seguimiento.persona_ingresa = aar.idpers LEFT JOIN dir_gral ON seguimiento.dirgralfirma = dir_gral.id LEFT JOIN cat_sitact ON seguimiento.situacionactualtram = cat_sitact.id LEFT JOIN cat_sentido_resolucion ON seguimiento.sentido_resolucion = cat_sentido_resolucion.id LEFT JOIN cat_estatus ON seguimiento.estatus_tramite = cat_estatus.id WHERE cat_tipo_ingreso.tipo_ingreso = 'ASUNTO' AND cat_materia.materia ='SASISOPA'")
    row = cursor.fetchall()
    conn.commit()
    conn.close()

   # create excel writer object
    writer = pd.ExcelWriter('source/Consulta.xlsx')
    # write dataframe to excel
    #datos.to_excel(writer)
    # save the excel
    writer.save()



crear_excel()