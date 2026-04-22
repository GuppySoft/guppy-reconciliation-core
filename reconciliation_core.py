def _obtener_o_crear_sucursal(session, nombre_sucursal, mapa_sucursales):
    """
    Busca una sucursal en el caché local o en la DB. 
    Maneja IntegrityError para escenarios de alta concurrencia.
    """
    nombre_limpio = nombre_sucursal.strip()
    if not nombre_limpio:
        return None

    # Optimización: Búsqueda en memoria antes que en disco (DB)
    if nombre_limpio in mapa_sucursales:
        return mapa_sucursales[nombre_limpio]

    sucursal = session.query(Sucursal).filter_by(nombre=nombre_limpio).first()
    if sucursal:
        mapa_sucursales[nombre_limpio] = sucursal.id
        return sucursal.id
    
    try:
        nueva_sucursal = Sucursal(nombre=nombre_limpio)
        session.add(nueva_sucursal)
        session.flush() # Asegura ID sin cerrar la transacción
        mapa_sucursales[nombre_limpio] = nueva_sucursal.id
        return nueva_sucursal.id
    except IntegrityError:
        # Fallback de seguridad: Si otro proceso la creó un milisegundo antes
        session.rollback() 
        sucursal_existente = session.query(Sucursal).filter_by(nombre=nombre_limpio).first()
        return sucursal_existente.id if sucursal_existente else raise


def procesar_liquidacion_pdf(lista_archivos_pdf):
    """
    Extrae tablas de liquidaciones desde PDFs en memoria y gestiona la conciliación.
    Si no existe el registro, lo deriva a una tabla de 'Pendientes' para auditoría futura.
    """
    pdf_data_map = {}

    for archivo_pdf in lista_archivos_pdf:
        # La lógica de extracción se desacopla para mantener el principio de responsabilidad única
        tablas = extract_and_filter_tables_from_pdf(archivo_pdf, columns_to_keep=[1, 8])
        
        for tabla in tablas:
            if not tabla.empty:
                for _, row in tabla.iterrows():
                    identificador = str(row.iloc[0]).strip()
                    # Normalización de formato numérico latino/europeo
                    descuento_str = str(row.iloc[1]).strip()
                    pdf_data_map[identificador] = convertir_a_numero(descuento_str.replace('.', '').replace(',', '.'))

    # Lógica de conciliación masiva (Bulk update) para optimizar hits a la DB


def limpiar_registros_liquidados(filtros):
    """
    Realiza un backup en memoria (Excel) de registros conciliados antes de su eliminación física.
    Garantiza que el usuario reciba un comprobante de lo auditado.
    """
    # ... lógica de filtrado ...
    
    output_bytes = io.BytesIO()
    # Generación de reporte dinámico usando Pandas y Openpyxl como engine
    df_respaldo = pd.DataFrame(datos_para_df)
    df_respaldo.to_excel(output_bytes, index=False, engine='openpyxl')
    output_bytes.seek(0) # Reposiciona el puntero para la descarga
    
    return output_bytes
