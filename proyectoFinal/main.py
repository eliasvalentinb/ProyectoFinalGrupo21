import gestionUsuario
import registrosPluviales 
import gestionAccesos

#MENU PRINCIPAL
def menu_principal():

    while True:
        print("\n ---------------")
        print("|MENÚ PRINCIPAL|")
        print(" ---------------")
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al sistema")
        print("3. Análisis de Datos")
        print("4. Salir de la Aplicación")
        opcion = input("\nSeleccione una opción: ")
        #USUARIOS Y ACCESOS A LA APLICACION
        if opcion == '1':
            print("\n -----------------")   
            print("|USUARIOS Y ACCESOS|")
            print(" -----------------")                                            
            print("1.Realizar un ABM de usuario:")
            print("2.Ver los registros de acceso:")
            print("3.Buscar/ ordenar usuarios:")
            print("4.Volver al Menu principal:")
            opcion = input("\nSeleccione una opción: ")
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
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__": 
    menu_principal()