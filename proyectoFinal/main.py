import gestionUsuario
import registrosPluviales 
import gestionAccesos

#MENU PRINCIPAL
def menu_principal():

    while True:
        print("\nMenú Principal")
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al sistema con los datos de Usuario")
        print("3. Analisis de Datos")
        print("4. Salir de la Aplicación")
        opcion = input("Seleccione una opción: ")
        #USUARIOS Y ACCESOS A LA APLICACION
        if opcion == '1':                                               
            print("1.Quiero realizar un ABM de usuario:")
            print("2.Quiero ver los registros de acceso:")
            print("3.Quiero buscar/ ordenar usuarios:")
            print("4.Quiero volver al Menu principal:")
            opcion = input("Seleccione una opción: ")
            #REALIZA ABM
            if opcion =="1":  
                gestionUsuario.gestionUsuario_ABM() #agrega, modifica, elimina usuarios
                #VER REGISTROS DE ACCESOS  
            elif opcion == "2":
                gestionAccesos.mostrar_Accesos()
                #BUSCAR / ORDENAR USUARIO
            elif opcion == "3": 
                gestionUsuario.gestionUsuario_BO() 
            elif opcion == "4":
                break  
         #INGRESAR AL SISTEMA
        elif opcion == '2':                                             
             gestionUsuario.ingresar()
         #ANALISIS DE DATOS
        elif opcion == '3':                                             
            registrosPluviales.registrosPluviales()
         #SALIR DE LA APLICACION
        elif opcion == '4':                                             
            exit()
        else:
            print("Opción no válida.")
"""         elif opcion == '5':
            print("Desea ordenar por metodo QUICK SORT, ingrese 1")
            print("Desea ordenar por el metodo SORT de Python, ingrese 2")
            eleccion= input("Seleccione una opcion: ")
            if eleccion =='1':
             ordenar_quick_sort(usuarios)
            else:
             ordenar_sort(usuarios)   
        elif opcion =='6':    
            mostrar_usuarios(usuarios)
        elif opcion == '7':
            nombre_usuario = input("Ingrese nombre de usuario: ")
            password = input("Ingrese password: ")
            usuario = next((u for u in usuarios if u.nombre_usuario == nombre_usuario and u.password == password), None)
            if usuario:
                print("Ingreso exitoso.")
                registrar_acceso(usuario)
                while True:
                    print("\n1. Volver al Menú Principal")
                    print("2. Salir")
                    sub_opcion = input("Seleccione una opción: ")
                    if sub_opcion == '1':
                        break
                    elif sub_opcion == '2':
                        exit()
            else:
                print("Nombre de usuario o password incorrectos.")
                registrar_logueo_fallido(nombre_usuario, password)
        elif opcion == '8':
             año = int(input("Ingrese el año (ej. 2023): "))
             df = cargar_registros(año)
             mes1 = input("Ingrese el mes que desea consultar (ej. Enero): ")
             mes=mes1.capitalize() #pone en mayuscula la primer letra
             mostrar_registros_mes(df, mes)

        elif opcion == '9':
             año = int(input("Ingrese el año (ej. 2023): "))
             df = cargar_registros(año)
             graficar_lluvias(df, año)       
        elif opcion == '10':
            exit()
        else:
            print("Opción no válida.")
"""
if __name__ == "__main__":
    menu_principal()