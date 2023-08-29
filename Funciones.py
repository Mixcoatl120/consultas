import pandas as pd
import openpyxl
import psycopg2


#Credenciales para la coneccion de la base de datos.
db_config = {
    'dbname': 'siset',
    'user': 'postgres',
    'password': 'Asea2023',
    'host': 'localhost',
    'port': '5432'
}

def imp_excel(con_where):
    conn = psycopg2.connect(**db_config)
    # Define your SQL query and retrieve data using pandas
    query = "SELECT" + \
    " seguimiento.fingreso_siset,"  + \
    " seguimiento.fsolicitud," + \
    " cat_tipo_ingreso.tipo_ingreso," + \
    " cat_tipo_asunto.tipo," + \
    " cat_descripcion.descripcion," + \
    " seguimiento.personaingresa_externa," + \
    " cat_materia.materia," + \
    " cat_tramites.cofemer," + \
    " seguimiento.bitacora_expediente," + \
    " seguimiento.rnomrazonsolcial," + \
    " seguimiento.rfc," + \
    " seguimiento.permiso_cre," + \
    " seguimiento.clave_proyecto," + \
    " cat_tipoinstalacion.tipo_instalacion," + \
    " cat_actividad.actividad," + \
    " dir_gral.siglas," + \
    " seguimiento.fasigevaluador, " + \
    " evaluador.nombre,"+ \
    " seguimiento.contenido," + \
    " seguimiento.observaciones," + \
    " seguimiento.clave_documento,"+ \
    " seguimiento.fecha_documento,"+ \
    " seguimiento.oficio_admintramite,"+ \
    " seguimiento.fechaofi_admintramite,"+ \
    " seguimiento.fechanotifi_admintramite,"+ \
    " seguimiento.numofapercb,"+ \
    " seguimiento.foficioaprcb,"+ \
    " seguimiento.fnotifapercb,"+ \
    " seguimiento.fdeshapercb,"+ \
    " seguimiento.numofpreve,"+ \
    " seguimiento.foficioprevencion,"+ \
    " seguimiento.fnotificacionprev,"+ \
    " seguimiento.fdesahogoprev,"+ \
    " seguimiento.noficiosolinfadic,"+ \
    " seguimiento.foficiosolinfadic,"+ \
    " seguimiento.fnotifsolinfadic,"+ \
    " seguimiento.fdesahsolinfadic,"+ \
    " seguimiento.nresolucion_ofresptram,"+ \
    " seguimiento.fresol_ofresptatram,"+ \
    " seguimiento.fnotificacionresol,"+ \
    " cat_sentido_resolucion.sentido_resolucion,"+ \
    " seguimiento.nfolio_prorroga,"+ \
    " seguimiento.fingreso_prorroga,"+ \
    " seguimiento.fsolicitud_prorroga,"+ \
    " seguimiento.noficio_prorroga,"+ \
    " seguimiento.foficio_prorroga,"+ \
    " seguimiento.fnotifica_prorroga,"+ \
    " seguimiento.noficio_amplia_plazo,"+ \
    " seguimiento.fnotifica_amplia_plazo,"+ \
    " cat_estatus.estatus,"+\
    " cat_sitact.situacion_actual,"+\
    " aar.nombre" +\
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


    final = query + " " + con_where

    dataframe = pd.read_sql_query(final, conn)
    # Close the database connection
    conn.close()
    # Save the data to an Excel file
    excel_file_path = 'source/Consulta.xlsx'
    dataframe.to_excel(excel_file_path, index=False, engine='openpyxl')
