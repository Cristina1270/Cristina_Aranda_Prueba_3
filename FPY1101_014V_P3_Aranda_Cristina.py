import re
import random
import os

# Variable global
vehiculos = []

# Funciones

def validar_patente(patente):
    #Se verifica si la patente cumple el siguiente formato: 4 consonantes seguidas de 2 números
    return bool(re.match(r'^[ABCDFGHJKLPQRSTVWXYZ]{4}\d{2}$', patente))


def validar_marca(marca):
    #Se verifica que la marca tenga entre 2 y 15 caracteres
    return 2 <= len(marca) <= 15


def validar_precio(precio):
    #Se verifica que el precio sea mayor a 5.000.000
    return precio > 5000000


def grabar_vehiculo():
    tipo = input("Ingrese el tipo de vehiculo (Automovil, Camión, Camioneta, Moto): ")
    while tipo not in ["Automovil", "Camión", "Camioneta", "Moto"]:
        tipo = input("Tipo invalido. Ingrese el tipo de vehiculo (Automovil, Camión, Camioneta, Moto): ")
    
    patente = input("Ingrese la patente del vehiculo (Ejemplo: BCDF12): ")
    while not validar_patente(patente):
        patente = input("Patente invalida. Ingrese la patente del vehiculo (4 consonantes y 2 números): ")

    marca = input("Ingrese la marca del vehiculo: ")
    while not validar_marca(marca):
        marca = input("Marca invalida. Ingrese la marca del vehiculo (entre 2 y 15 caracteres): ")

    try:
        precio = int(input("Ingrese el precio del vehiculo: "))
    except:
        precio = -1

    while not validar_precio(precio):
        try:
            precio = int(input("Precio invalido. Ingrese el precio del vehiculo (mayor a 5.000.000): "))
        except:
            precio = 0

    multas = []

    try:
        cantidad_multas = int(input("Ingrese la cantidad de multas del vehiculo: "))
    except:
        cantidad_multas = -1

    for i in range(cantidad_multas):

        while True:
            try:
                monto = int(input("Ingrese el monto de la multa: "))
                if monto <=0:
                    print("Por favor, ingrese correctamente el monto")
                else:
                    fecha = int(input("Ingrese la fecha de la multa (Los números deben estar juntos Ejemplo: XXXXXXXX): "))
                    if fecha <=0 :
                        print("Por favor, ingrese correctamente la fecha.")
                    else:
                        break         
            except:
                print("Falta ingresar datos.")

        multas.append((monto, fecha))

    
    while True:
        try:
            run_duenio = int(input("Ingrese el RUN del dueño del vehiculo (sin puntos ni guion): "))
        except:
            run_duenio=-1
            
        if 500000<run_duenio<399999999:
            break
        else:
            print("Rut no válido")
    while True:
        nombre_duenio = input("Ingrese el nombre del dueño del vehiculo: ")
        fecha_registro = input("Ingrese la fecha de registro del vehiculo: ")
        if len(nombre_duenio)==0 and len(fecha_registro)==0:
            print("Falta Ingresar datos.")
        else:
            break

    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha_registro": fecha_registro,
        "run_duenio": run_duenio,
        "nombre_duenio": nombre_duenio
    }
    vehiculos.append(vehiculo)
    print("Vehiculo registrado exitosamente.")


def buscar_vehiculo():
    patente = input("Ingrese la patente del vehiculo a buscar: ")
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print(f"Tipo: {vehiculo['tipo']}")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Marca: {vehiculo['marca']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Multas: {vehiculo['multas']}")
            print(f"Fecha de registro: {vehiculo['fecha_registro']}")
            print(f"RUN del dueño: {vehiculo['run_duenio']}")
            print(f"Nombre del dueño: {vehiculo['nombre_duenio']}")
            return
    print("Vehiculo no encontrado.")


def imprimir_certificados():
    patente = input("Ingrese la patente del vehiculo para imprimir certificados: ")
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            certificados = ["Emision de contaminantes", "Anotaciones vigentes", "Multas"]
            for certificado in certificados:
                valor = random.randint(1500, 3500)
                print(f"Certificado de {certificado}")
                print(f"Patente: {vehiculo['patente']}")
                print(f"Nombre del dueño: {vehiculo['nombre_duenio']}")
                print(f"RUN del dueño: {vehiculo['run_duenio']}")
                print(f"Valor: {valor}\n")
            return
    print("Vehiculo no encontrado.")

os.system("cls")
while True:
    print("\nMenu:")
    print("(1) Grabar")
    print("(2) Buscar")
    print("(3) Imprimir certificados")
    print("(4) Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        grabar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        imprimir_certificados()
    elif opcion == "4":
        print("Gracias por usar el programa. Autor: [Cristina Aranda]. Version: 1.0")
        break
    else:
        print("Opcion invalida. Por favor, intente nuevamente.")