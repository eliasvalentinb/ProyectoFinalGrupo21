
def menu_principal():
    print("¡Bienvenido al menú principal!")
    print("1. Gestión de Usuarios y Accesos")
    print("2. Ingresar al sistema")
    print("3. Análisis de Datos")
    print("4. Salir de la aplicación")

    opcion = input("Seleccioná una opción: ")
    return opcion

def menu_Usuarios_Accesos():
    while True:
        print(" \n------------------------------")
        print("| GESTIÓN DE USUARIOS Y ACCESOS |")
        print(" ------------------------------")

        print("a. CRUD de usuarios")
        print("b. Mostrar datos de accesos")
        print("c. Ordenamiento y búsqueda de usuarios")
        print("d. Volver al Menú Principal")

        opcion = input("Seleccioná una opción: ").lower()

        if opcion == 'a':
            menu_crud_usuarios()
        elif opcion == 'b':
            menu_mostrar_accesos()
        elif opcion == 'c':
            menu_ordenamiento_busqueda()
        elif opcion == 'd':
            break
        else:
            print("Opción no válida. Intentá nuevamente.")

def menu_crud_usuarios():
    while True:
        print(" \n-----------------")
        print("| CRUD DE USUARIOS |")
        print(" -------------------")

        print("i. Agregar un nuevo usuario")
        print("ii. Modificar un usuario")
        print("iii. Eliminar un usuario")
        print("iv. Volver al Menú Principal")

        opcion = input("Seleccioná una opción: ").lower()

        if opcion == 'i':
            agregar_usuario()
        elif opcion == 'ii':
            modificar_usuario()
        elif opcion == 'iii':
            eliminar_usuario()
        elif opcion == 'iv':
            break
        else:
            print("Opción no válida. Intentá nuevamente.")

def menu_mostrar_accesos():
    while True:
        print(" \n----------------")
        print("| MOSTRAR ACCESOS |")
        print(" ------------------")

        print("i. Mostrar los accesos")
        print("ii. Mostrar logs de intentos fallidos")
        print("iii. Volver al Menú Principal")
    
        opcion = input("Seleccioná una opción: ").lower()

        if opcion == 'i':
            mostrar_accesos()
        elif opcion == 'ii':
            mostrar_logs_fallidos()
        elif opcion == 'iii':
            break
        else:
            print("Opción no válida. Intentá nuevamente.")

def menu_ordenamiento_busqueda():
    while True:
        print(" \n-----------------------------------")
        print("| ORDENAMIENTO Y BÚSQUEDA DE USUARIOS |")
        print(" -------------------------------------")

        print("i. Ordenar usuarios")
        print("ii. Buscar y mostrar usuarios")
        print("iii. Volver al Menú Principal")

        opcion = input("Seleccioná una opción: ").lower()

        if opcion == 'i':
            ordenar_usuarios()       
        elif opcion == 'ii':
            menu_busqueda_usuarios()      
        elif opcion == 'iii':
            break
        else:
            print("Opción no válida. Intentá nuevamente.")

def menu_busqueda_usuarios():
    while True:
        print("\nBuscar Usuarios:")
        print("1. Por DNI")
        print("2. Por username")
        print("3. Por email")
        print("4. Mostrar todos los usuarios")
        print("5. Volver al Menú anterior")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            buscar_usuario_por_dni()
        elif opcion == '2':
            buscar_usuario_por_username()
        elif opcion == '3':
            buscar_usuario_por_email()
        elif opcion == '4':
            mostrar_todos_los_usuarios()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def ingresar_al_Sistema():
    while True:
        print("\n---------------")
        print("| INICIAR SESIÓN |")
        print("-----------------")

