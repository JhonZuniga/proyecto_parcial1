import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata

def buscar_datos():
    # Clave de API
    app_token = "NKCHi3LOO1xctFBVZHnC9RAvp"
    user = "jhon.zuniga@utp.edu.co"
    clave = "Buenas2016"
    # Autenticación con la clave de API y el secreto
    client = Socrata("https://www.datos.gov.co/resource/ch4u-f3i5.json", app_token, user, clave)

    # ID del conjunto de datos que deseas acceder
    dataset_id = "ch4u-f3i5"

    # Primeros 50 resultados, retornados como JSON desde la API / convertidos a una lista de diccionarios de Python por sodapy
    results = client.get("ch4u-f3i5", limit=5)

    # Convertir a un DataFrame de pandas
    results_df = pd.DataFrame.from_records(results)

    # Filtrar los datos según el departamento seleccionado
    departamento = departamento_combobox.get()
    if departamento:
        results_df = results_df[results_df['departamento'] == departamento]

    # Mostrar los datos en la consola
    print(results_df)

    # Crear un gráfico
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

# Crear la ventana principal
root = tk.Tk()
root.title("Consulta de Datos")

# Crear etiqueta y campo de entrada para el departamento
departamento_label = ttk.Label(root, text="Departamento:")
departamento_label.grid(row=0, column=0, padx=5, pady=5)
departamento_combobox = ttk.Combobox(root, values=["", "Amazonas", "Antioquia", "Arauca", "Atlántico"], state="readonly")
departamento_combobox.grid(row=0, column=1, padx=5, pady=5)
departamento_combobox.current(0)

# Crear botón de búsqueda
buscar_button = ttk.Button(root, text="Buscar", command=buscar_datos)
buscar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar el bucle de eventos
root.mainloop()
