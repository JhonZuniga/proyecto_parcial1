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
def consultar_por_departamento(departamento):
    query = f"departamento='{departamento.upper()}'"
    results = client.get(dataset_id, where=query, limit=10)
    if results:
        results_df = pd.DataFrame.from_records(results)
        return results_df
    else:
        print("No se encontraron datos para ese departamento.")
        return None

# Input de usuario para ingresar departamento
departamento_usuario = input("Ingresa el nombre del departamento para consultar los datos: ")

# Consultar datos y mostrarlos si existen
datos_departamento = consultar_por_departamento(departamento_usuario)

if datos_departamento is not None:
    columns_to_display = ['departamento', 'municipio', 'cultivo', 'estado', 'tiempo_establecimiento']
    results_df_subset = datos_departamento[columns_to_display]

    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 6))

    # Configurar la tabla
    tabla = plt.table(cellText=results_df_subset.values, colLabels=results_df_subset.columns, loc='center')

    # Ocultar ejes
    ax = plt.gca()
    ax.axis('off')

    # Mostrar tabla
    plt.show()
