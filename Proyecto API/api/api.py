import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata

# Asegúrate de instalar estos paquetes antes de ejecutar :
# pip install pandas
# pip install sodapy
# pip install matplotlib

# Clave de API
app_token = "NKCHi3LOO1xctFBVZHnC9RAvp"

user = "jhon.zuniga@utp.edu.co"
clave = "Buenas2016@"
# Autenticación con la clave de API y el secreto
client = Socrata("www.datos.gov.co", app_token, user, clave)

# ID del conjunto de datos que deseas acceder
dataset_id = "ch4u-f3i5"

# Primeros 50 resultados, retornados como JSON desde la API / convertidos a una lista de diccionarios de Python por sodapy
results = client.get("ch4u-f3i5", limit=10)

# Convertir a un DataFrame de pandas
results_df = pd.DataFrame.from_records(results)

# Renombrar las columnas
results_df.rename(columns={'ph_agua_suelo_2_5_1_0': 'ph', 
                            'f_sforo_p_bray_ii_mg_kg': 'fosforo (p)', 
                            'potasio_k_intercambiable_cmol_kg': 'potasio (k)'}, inplace=True)

columns_to_display = ['departamento', 'municipio', 'cultivo', 'estado', 'tiempo_establecimiento', 'ph', 'fosforo (p)', 'potasio (k)']
results_df_subset = results_df[columns_to_display]

# Configurar el tamaño de la figura
plt.figure(figsize=(10, 6))

# Configurar la tabla
tabla = plt.table(cellText=results_df_subset.values, colLabels=results_df_subset.columns, loc='center')

# Ocultar ejes
ax = plt.gca()
ax.axis('off')

# Mostrar tabla
plt.show()
