from ui import consultar_por_departamento

def main():
    departamento_usuario = input("Ingresa el nombre del departamento para consultar los datos: ")
    municipio_usuario = input("Ingresa el nombre del municipio para consultar los datos (opcional): ")
    cultivo_usuario = input("Ingresa el nombre del cultivo para consultar los datos (opcional): ")

    datos_departamento = consultar_por_departamento(departamento_usuario, municipio_usuario, cultivo_usuario)
if __name__ == "__main__":
    main()
