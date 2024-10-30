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

if __name__ == "__main__": 
    menu_principal()