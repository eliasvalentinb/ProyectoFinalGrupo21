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
            gestionUsuario.usuarios_accesos()                                          
         #INGRESAR AL SISTEMA
        elif opcion == '2':
            print("\n -------------------")   
            print("| INGRESAR AL SISTEMA |")
            print(" ---------------------")                                             
            gestionUsuario.ingresar()
         #ANALISIS DE DATOS
        elif opcion == '3':
            print("\n -------------------")   
            print("| ANALISIS DE DATOS |")
            print(" --------------------")                                             
            registrosPluviales.registrosPluviales()
         #SALIR DE LA APLICACION
        elif opcion == '4':
            print("Gracias por su visita!")                                             
            exit()
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__": 
    menu_principal()