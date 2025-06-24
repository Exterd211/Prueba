def menu():
    print("Sistema de contactos")
    print("*"*20)
    print("""
    1.- Crear Contacto.
    2.- Modificar Contactos.
    3.- Eliminar Contactos.
    4.- Listar Contactos.
    5.- Buscar Contactos.
    6.- Salir.
    """)
    op = input("ingrese una opcion (1/6)")
    return op

import re

def es_correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def contacto_crear(contacto):
    telf = []
    
    while True:
        nombre = input("ingrese un nombre de maximo 50 caracteres: ").strip()
        if len(nombre) <= 50 and len(nombre) >= 1:
            if nombre.isalpha():
                break
            else:
                print("ingrese un formato valido, no se permite espacios ni numeros")
    print("ahora debe ingresar hasta un maximo de 6 numeros en formato digital")
    while True:
        cantidad = int(input("ingrese la cantidad de numeros a agregar (minimo: 1 / maximo: 6)"))
        if cantidad >=1 and cantidad <=6:
            break
        else:
            print("ingrese una cantidad valida")
    for i in range(cantidad):
        while True:

            print("ingrese un numero intercional sin el + [numero internacional = 11 digitos]")
            telefono = input("ingrese un numero: ").strip()
            if telefono.isdigit() and len(telefono) == 11:
                telf.append(telefono)
                break
            else:
                print("ingrese un formato valido y 11 digitos: ")
    while True:
        correo = input("Ingrese correo electrónico: ").strip()
        if len(correo) <= 50 and es_correo_valido(correo):
            print("Correo válido")
            break
        else:
            print("Correo inválido")
    while True:
        direccion = input("ingrese direccion: ")
        if len(direccion) >= 1 and len(direccion) <= 60:
            break
        else:
            print("es muy largo o corto su direccion")
    contacto[nombre] = [telf, direccion, correo]
    print("Contacto agregado")
    return contacto
def modificar_contacto(contacto):
    nombre = input("Ingrese el nombre del contacto a modificar: ").strip()
    if nombre in contacto:
        print(f"Datos actuales: Teléfono: {contacto[nombre][0]}, Dirección: {contacto[nombre][1]}, Correo: {contacto[nombre][2]}")
        
        nuevo_telefono = input("Nuevo teléfono (enter para dejar igual): ").strip()
        nueva_direccion = input("Nueva dirección (enter para dejar igual): ").strip()
        nuevo_correo = input("Nuevo correo (enter para dejar igual): ").strip()

        if nuevo_telefono:
            contacto[nombre][0] = nuevo_telefono
        if nueva_direccion:
            contacto[nombre][1] = nueva_direccion
        if nuevo_correo:
            contacto[nombre][2] = nuevo_correo

        print("Contacto actualizado.")
    else:
        print("Contacto no encontrado.")

    return contacto
def eliminar_contacto(contacto):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ").strip()
    
    if nombre in contacto:
        confirmar = input(f"¿Está seguro que desea eliminar a '{nombre}'? (s/n): ").strip().lower()
        if confirmar == "s":
            del contacto[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")
    
    return contacto
def mostrar_contactos(contacto):
    if not contacto:
        print("No hay contactos guardados.")
        return

    print(" Lista de Contactos:")
    print("-" * 50)
    for nombre, datos in contacto.items():
        telefonos, direccion, correo = datos
        print(f"Nombre     : {nombre}")
        print(f"Teléfonos  : {', '.join(telefonos)}")
        print(f"Dirección  : {direccion}")
        print(f"Correo     : {correo}")
        print("-" * 50)
def mostrar_un_contacto(nombre, datos):
    if not datos or len(datos) != 3:
        print(f"❌ El contacto '{nombre}' no tiene datos válidos.")
        return

    telefonos, direccion, correo = datos
    print("-" * 50)
    print(f"Nombre     : {nombre}")
    print(f"Teléfonos  : {', '.join(telefonos)}")
    print(f"Dirección  : {direccion}")
    print(f"Correo     : {correo}")
    print("-" * 50)
def buscar_contacto(contacto):
    if not contacto:
        print("No hay contactos guardados.")
        return

    print("🔎 Buscar contacto por:")
    print("1. Nombre")
    print("2. Teléfono")
    print("3. Dirección")
    print("4. Correo Electrónico")

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        clave = input("Ingrese el nombre a buscar: ").strip()
        if clave in contacto:
            print(f"✅ Contacto encontrado: {clave}")
            mostrar_un_contacto(clave, contacto[clave])  

            print("❌ Contacto no encontrado.")

    elif opcion in ["2", "3", "4"]:
        valor_buscado = input("Ingrese el valor a buscar: ").strip()
        encontrado = False

        for nombre, datos in contacto.items():
            telefonos, direccion, correo = datos

            if (opcion == "2" and valor_buscado in telefonos) or \
               (opcion == "3" and valor_buscado.lower() in direccion.lower()) or \
               (opcion == "4" and valor_buscado.lower() == correo.lower()):
                print(f"✅ Contacto encontrado: {nombre}")
                mostrar_un_contacto(nombre, datos)
                encontrado = True

        if not encontrado:
            print("❌ No se encontró ningún contacto con ese dato.")
    else:
        print("Opción no válida.")