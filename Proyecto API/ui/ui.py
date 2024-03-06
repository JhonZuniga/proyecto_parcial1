import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata

# Clave de API
app_token = "NKCHi3LOO1xctFBVZHnC9RAvp"
user = "jhon.zuniga@utp.edu.co"
clave = "Buenas2016@"

# Autenticación con la clave de API y el secreto
client = Socrata("www.datos.gov.co", app_token, user, clave)

# ID del conjunto de datos que deseas acceder
dataset_id = "ch4u-f3i5"

# Función para consultar datos por departamento
def consultar_por_departamento(departamento, municipio, cultivo, limite=10):
    query = f"departamento='{departamento.upper()}'"
    if municipio:
        query += f" and municipio='{municipio.upper()}'"
    if cultivo:
        query += f" and cultivo='{cultivo}'"
    print(f"Consultando datos con el siguiente filtro: {query}")
    results = client.get(dataset_id, where=query, limit=1000)

    if results:
        results_df = pd.DataFrame.from_records(results)
        return results_df
    else:
        print("No se encontraron datos para esos filtros.")
        return None

# Input de usuario para ingresar departamento
departamento_usuario = input("Ingresa el nombre del departamento para consultar los datos: ")
municipio_usuario = input("Ingresa el nombre del municipio para consultar los datos: ")
cultivo_usuario = input("Ingresa el nombre del cultivo para consultar los datos: ")

# Consultar datos y mostrarlos si existen
datos_departamento = consultar_por_departamento(departamento_usuario,municipio_usuario,cultivo_usuario)

if datos_departamento is not None:

    variables_edaficas = ['ph_agua_suelo_2_5_1_0', 'f_sforo_p_bray_ii_mg_kg', 'potasio_k_intercambiable_cmol_kg']
    for variable in variables_edaficas:
        datos_departamento[variable] = pd.to_numeric(datos_departamento[variable], errors='coerce')

    medianas_edaficas = datos_departamento[variables_edaficas].median()

    data_to_display = {
        'Departamento': [departamento_usuario],
        'Municipio': [datos_departamento['municipio'].iloc[0]],
        'Cultivo': [datos_departamento['cultivo'].iloc[0]],
        'Topología': [datos_departamento['topografia'].iloc[0]],
        'Mediana pH': [medianas_edaficas['ph_agua_suelo_2_5_1_0']],
        'Mediana Fósforo(P)': [medianas_edaficas['f_sforo_p_bray_ii_mg_kg']],
        'Mediana Potasio(K)': [medianas_edaficas['potasio_k_intercambiable_cmol_kg']]
    }

    # Crear DataFrame
    df_to_display = pd.DataFrame(data_to_display)

    # Configurar el tamaño de la figura
    plt.figure(figsize=(12, 8))

    # Configurar la tabla
    tabla = plt.table(cellText=df_to_display.values, colLabels=df_to_display.columns, loc='center', cellLoc='center', colColours=['lightblue']*len(df_to_display.columns))

    # Establecer propiedades de la tabla
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(12)
    tabla.scale(1.2, 1.2)

    # Ocultar ejes
    plt.axis('off')

    # Mostrar tabla
    plt.show()