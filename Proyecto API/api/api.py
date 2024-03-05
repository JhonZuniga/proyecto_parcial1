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
results = client .get("ch4u-f3i5", limit =5)

# Convertir a un DataFrame de pandas
results_df = pd.DataFrame.from_records(results)

print(results_df)

columns_to_display = ['departamento', 'municipio', 'cultivo', 'estado', 'tiempo_establecimiento']
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
