
SELECT
    seguimiento.fingreso_siset AS "FECHA INGRESO SISET",
    seguimiento.fsolicitud AS "FECHA DE INGRESO",
    cat_tipo_ingreso.tipo_ingreso AS "TIPO DE INGRESO",
    cat_tipo_asunto.tipo AS "TIPO DE ASUNTO",
    -- cat_unidadministrativa.siglas_unidad AS "UNIDAD ADMINISTRARTIVA",
    cat_descripcion.descripcion AS "DESCRIPCION",
    seguimiento.personaingresa_externa "REMITENTE",
    cat_materia.materia AS "MATERIA",
    cat_tramites.cofemer AS "TRAMITE",
    -- cat_cofemer.cofemer AS "COFEMER",
    seguimiento.bitacora_expediente AS "BITACORA",
    -- seguimiento.bitacora_relacion AS "BITACORA RELACION",
    seguimiento.rnomrazonsolcial AS "RAZON SOCIAL",
    seguimiento.rfc AS "RFC",
    seguimiento.permiso_cre AS "PERMISO CRE",
    -- seguimiento.nomreplegal AS "NOMBRE REPRESENTANTE LEGAL",
    -- seguimiento.domreplegal AS "DOMICILIO REPRE LEGAL",
    -- cat_estado.estado AS "ENTIDAD FEDERATIVA REPRESENTANTE LEGAL",
    -- seguimiento.tel AS "TELEFONO",
    -- seguimiento.emailnotif AS "CORREO ELECTRONICO",
    -- seguimiento.nomproyecto AS "NOMBRE PROYECTO",
    -- cat_proyecto_critico.tipo AS "PRIORITARIO 01",
    -- impor_media.tipo AS "PRIORITARIO 02",
    -- monto.tipo AS "PRIORITARIO 03",
    -- impacto.tipo AS "PRIORITARIO 04",
    -- edo_proy.estado "EDO PROYECTO",
    -- at_municipios.municipio "MUN PROYECTO",
    -- seguimiento.domproyecto AS "DOMICILIO DEL PROYECTO",

    seguimiento.clave_proyecto AS "CLAVE DE PROYECTO",
    cat_tipoinstalacion.tipo_instalacion AS "TIPO DE INSTALACION",
    cat_actividad.actividad AS "ACTIVIDAD",
    dir_gral.siglas AS "DIRECCION GRAL. FIRMA",
    -- cat_personal.nombre AS "DIRECTOR DE ÁREA",
    seguimiento.fasigevaluador AS "FECHA ASIG. EVALUADOR",
    evaluador.nombre AS "EVALUADOR",

    seguimiento.contenido AS "CONTENIDO",
    seguimiento.observaciones AS "OBSERVACIONES",

    seguimiento.clave_documento AS "CLAVE DEL DOCUMENTO",
    seguimiento.fecha_documento AS "FECHA DEL DOCUMENTO",

    seguimiento.oficio_admintramite AS "OFICI ADMIN TRAMITE",
    seguimiento.fechaofi_admintramite AS "FECHA OFICI ADMIN TRAMITE",
    seguimiento.fechanotifi_admintramite AS "NOTIFICA ADMIN TRAMITE",

    seguimiento.numofapercb  AS "FOLIO APERCEBIMIENTO",
    seguimiento.foficioaprcb AS "FECHA FOLIO APERCEBIMIENTO",
    seguimiento.fnotifapercb AS "FECHA NOTI. APERCEBIMIENTO",
    seguimiento.fdeshapercb AS "FECHA DESAH. APERCEBIMIENTO",

    seguimiento.numofpreve AS "FOLIO PREVENCION",
    seguimiento.foficioprevencion AS "FECHA FOLIO PREVENCION",
    seguimiento.fnotificacionprev AS "FECHA NOTI. PREVENCION",
    seguimiento.fdesahogoprev AS "FECHA DESAH. PREVENCION",

    seguimiento.noficiosolinfadic AS "FOLIO INFO. ADICIONAL",
    seguimiento.foficiosolinfadic AS "FECHA FOLIO INFO. ADICIONAL",
    seguimiento.fnotifsolinfadic AS "FECHA NOTI. INFO. ADICIONAL",
    seguimiento.fdesahsolinfadic AS "FECHA DESAH. INFO. ADICIONAL",

    seguimiento.nresolucion_ofresptram AS "FOLIO RESOLUCION",
    seguimiento.fresol_ofresptatram AS "FECHA FOLIO RESOLUCION",
    seguimiento.fnotificacionresol AS "FECHA NOTIFI. RESOLUCION",
    cat_sentido_resolucion.sentido_resolucion AS "SENTIDO RESOLUCION",

    seguimiento.nfolio_prorroga AS "FOLIO PRORROGA",
    seguimiento.fingreso_prorroga AS "FECHA INGRESO",
    seguimiento.fsolicitud_prorroga AS "FECHA SOLICIUD",
    seguimiento.noficio_prorroga AS "OFICIO PRORROGA",
    seguimiento.foficio_prorroga AS "FECHA OFICIO PRORROGA",
    seguimiento.fnotifica_prorroga AS "FECHA NOTIF PRORROGA",

    seguimiento.noficio_amplia_plazo AS "OFICIO AMPLIA PLAZO",
    seguimiento.fnotifica_amplia_plazo AS "NOTIFICA AMPLIA PLAZO",

    cat_estatus.estatus AS "ESTATUS",
    cat_sitact.situacion_actual AS "SITUACION ACTUAL",

    -- cat_rondas.nomenclatura AS "RONDA",
    -- cat_licitacion.nomenclatura AS "LICITACION",
    -- cat_area_contractual.nomenclatura AS "AREA CONTRACTUAL",
    -- cat_campo.nombre_campo AS "CAMPO",
    -- seguimiento.contrato_cnh AS "CONTRATO CNH",

    -- seguimiento.folio_op AS "FOLIO 02",

    aar.nombre AS "INGRESA AAR"
FROM seguimiento
     LEFT JOIN cat_tipo_ingreso ON seguimiento.tipo_ingreso = cat_tipo_ingreso.id
     LEFT JOIN cat_tipo_asunto ON seguimiento.tipo_asunto = cat_tipo_asunto.id
     -- LEFT JOIN  cat_unidadministrativa ON seguimiento.cve_unidad = cat_unidadministrativa.cve_unidad
     LEFT JOIN cat_descripcion ON seguimiento.descripcion = cat_descripcion.id
     LEFT JOIN cat_materia ON seguimiento.materia = cat_materia.id
     LEFT JOIN cat_tramites ON seguimiento.tramite = cat_tramites.idtram
     -- LEFT JOIN cat_cofemer ON seguimiento.cofemer = cat_cofemer.id
     -- LEFT JOIN cat_proyecto_critico ON split_part(cve_proyecto_critico,';',1) = cat_proyecto_critico.id::text
     -- LEFT JOIN cat_proyecto_critico AS impor_media ON split_part(cve_proyecto_critico,';',2) = impor_media.id::text
     -- LEFT JOIN cat_proyecto_critico AS monto ON split_part(cve_proyecto_critico,';',3) = monto.id::text
     -- LEFT JOIN cat_proyecto_critico AS impacto ON split_part(cve_proyecto_critico,';',4) = impacto.id::text
     -- LEFT JOIN cat_estado ON seguimiento.estadoreplegal = cat_estado.id
     -- LEFT JOIN cat_estado edo_proy ON seguimiento.estadoproyecto = cat_estado.id::varchar
   	 -- LEFT JOIN cat_municipios ON seguimiento.munproyecto = cat_municipios.id::varchar
     LEFT JOIN cat_tipoinstalacion  ON seguimiento.tipoinstalacion = cat_tipoinstalacion.id
     LEFT JOIN cat_actividad ON seguimiento.cve_actividad = cat_actividad.id
     LEFT JOIN cat_personal AS evaluador ON seguimiento.nevaluador = evaluador.idpers
     LEFT JOIN cat_personal AS aar ON seguimiento.persona_ingresa = aar.idpers
     -- LEFT JOIN cat_personal ON seguimiento.turnado_da = cat_personal.idpers
     LEFT JOIN dir_gral ON seguimiento.dirgralfirma = dir_gral.id
     LEFT JOIN cat_sitact ON seguimiento.situacionactualtram = cat_sitact.id
     LEFT JOIN cat_sentido_resolucion ON seguimiento.sentido_resolucion = cat_sentido_resolucion.id
     LEFT JOIN cat_estatus ON seguimiento.estatus_tramite = cat_estatus.id
     -- LEFT JOIN cat_area_contractual ON seguimiento.area_contractual = cat_area_contractual.id
     -- LEFT JOIN cat_campo ON seguimiento.nombre_campo = cat_campo.id
     -- LEFT JOIN cat_rondas ON seguimiento.numero_ronda = cat_rondas.id
     -- LEFT JOIN cat_licitacion ON seguimiento.numero_licitacion = cat_licitacion.id
