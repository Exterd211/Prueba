import profe as pr
contacto = {}
opciones = ""

while opciones != "6":
    opciones = pr.menu()
    
    if opciones == "6":
        print("Cerrando Sistema")
        break

    elif opciones == "1":
        print("Agregar Contacto")
        contacto = pr.contacto_crear(contacto)
        print(f"{contacto}")

    elif opciones == "2":
        print("Modificar contacto")
        contacto = pr.modificar_contacto(contacto) 

    elif opciones == "3":
        print("Eliminar contacto")
        contacto = pr.eliminar_contacto(contacto)  
    elif opciones == "4":
        print("Mostrar lista de contactos")
        pr.mostrar_contactos(contacto)


    elif opciones == "5":
        print("Buscar contacto")
        pr.buscar_contacto(contacto)

    else:
        print("Opción no válida. Intente nuevamente.")