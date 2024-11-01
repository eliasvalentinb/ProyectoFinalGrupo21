def vend_adm():
 import Conectar_desconectar
 import mysql.connector 
 from mysql.connector import Error
 conexion= Conectar_desconectar.conexion()
 dic={}
 if conexion.is_connected():
            cursor=conexion.cursor()
            cursor.execute("select * from Usuario;") 
            resultados=cursor.fetchall()
            for fila in resultados:       
             dic[fila[1]] =[fila[2] ,fila[3],fila[0]]  #se arma un diccionario  con lista usuario:password,perfil,id_usuario
            #print(dic)                #limpiar solo es para test  
            cu = 0                
            while True:
                print("                    LOGIN VENDEDOR/Admin                            ")
                print("====================================================================")
                USU=input("ingrese su usuario: ") #pide el usuario para validar 
                pass_perfil = dic.get(USU)
                #print(pass_perfil)
                pass_reg = pass_perfil[0]
                perfil = pass_perfil[1]
                id_Usu = pass_perfil[2]  
                #print(pass_reg)           #limpiar solo es para test
                usuarios=dic.keys()       #listado de las claves del diccionario     
                if USU not in usuarios:
                    print("Usuario invalido")
                    cu = cu + 1
                    if cu == 3:
                        break #permite tres intentos
                else:
                    cp = 0
                    while True:
                        PAS=input("ingrese su password: ")
                        #print("====================================================================")
                        print("********************************************************************")
                        if PAS != pass_reg:
                            print("password incorrecto")
                            cp = cp +1
                            if cp == 3:
                                break
                        else:
                            print("Bienvenido, ",USU)
                            if perfil == 3:
                                print("********************************************************************")
                                #print("====================================================================")
                                print("             Para MODIFICAR los PRECIOS  - ingresa 1                ")
                                print("             Para AGREGAR un PRODUCTO    - ingresa 2                ")
                                print("             Para AGREGAR USUARIO Admin  - ingresa 3                ")
                                print("--------------------------------------------------------------------")
                                llamar=int(input("ingrese una opcion. "))
                                print("--------------------------------------------------------------------")
                                print( )
                                if llamar == 1:
                                    modificar_precio(conexion)
                                elif llamar == 2: 
                                    agregar_producto(conexion)
                                elif llamar == 3:
                                    agregar_usuario(conexion)
                                else: 
                                    print("opcion incorrecta") 
                                    break   
                            if perfil == 2:
                                print("********************************************************************")
                                #print("====================================================================")
                                print("             Para MODIFICAR los PRECIOS  - ingresa 1                ")
                                print("             Para AGREGAR un PRODUCTO    - ingresa 2                ")
                                print("--------------------------------------------------------------------")
                                llamar2=int(input("ingrese una opcion. "))
                                print("--------------------------------------------------------------------")
                                print( )
                                #llamar2 = int(input("1 para alquiar cancha, 2 para sumarte a un partido "))
                                if llamar2 == 1:
                                    modificar_precio(conexion)
                                elif llamar2 == 2:
                                    agregar_producto(conexion)
                                else:
                                    print("opcion incorrecta") 
                                    break
                            break #sale del while del password
                    break #sale del while del usuario                           
           
 Conectar_desconectar.desconexion(conexion)
#----------------------------------------------------------------------------------------------------------------------------

def modificar_precio(conexion1):
   conexion = conexion1
   cursor=conexion.cursor()
   cursor.execute("select * from producto;") 
   tabla_producto = cursor.fetchall() 
   print("                         MODIFICAR PRECIOS                          ")
   print("====================================================================")      
   for filas in tabla_producto:
      print(f"Id: {filas[0]} - Producto: {filas[1]} - Precio: ${filas[3]}")
   print("--------------------------------------------------------------------")
   modificar = input("que precio quiere modificar? (ingrese el Id) ")
   Nuevo_precio = input("cual es el nuevo precio? ")
   sql= f"""UPDATE producto SET precio = {Nuevo_precio} WHERE Id_producto = {modificar}; """
   cursor=conexion.cursor()
   cursor.execute(sql) 
   conexion.commit()
   print("--------------------------------------------------------------------")
   print("El cambio fue registrado exitosamente")
   print()
   cursor=conexion.cursor()
   cursor.execute(f"""select * from producto WHERE Id_producto = {modificar};""") 
   tabla_producto = cursor.fetchall()       
   for filas in tabla_producto:
      print(f"Id: {filas[0]} - Producto: {filas[1]} - Precio: ${filas[3]}")    


def agregar_producto(conexion1):
   conexion = conexion1
   cursor=conexion.cursor()
   cursor.execute("select * from categoria;") 
   tabla_categoria = cursor.fetchall() 
   print("                    CATEGORIAS DE PRODUCTOS                         ")
   print("====================================================================")      
   for filas in tabla_categoria:
      print(f"Id: {filas[0]} - Descripción: {filas[1]}")
   print("--------------------------------------------------------------------")
   categ = input("que categoria quiere asignar al nuevo producto? (ingrese el Id) ")
   descrip = input("ingrese el nombre del producto: ")
   precio = float(input("indique el precio del producto: "))
   cursor=conexion.cursor()
   sql="""INSERT INTO producto(descripcion,id_categoria,precio) 
                VALUES (%s,%s,%s);"""
   valores=(descrip,categ,precio)
   cursor.execute(sql,valores)   
   conexion.commit()
   print("=============================================================================")
   print("sus datos se registraron correctamente") 
   print("=============================================================================")


def agregar_usuario(conexion1):
            conexion = conexion1
            print("=============================================================================")
            print("Por favor, ingresa un usuario para validar si esta disponible: ") 
            print("=============================================================================") 
            Lista=[] #creo una lista para contener los usuarios
            USU=input("ingrese un usuario: ") #pide el usuario para validar si esta disponible
            cursor=conexion.cursor()
            cursor.execute("select * from usuario;") 
            resultados=cursor.fetchall()
            for fila in resultados:       
                Lista.append(fila[1]) # me quedo con los usuarios creados en la tabla Usuarios
            #print(Lista)  #limpiar es para test
            if USU in Lista:
                print("El Usuario no esta Disponible.")
            else: 
                print("=============================================================================")
                print("Por favor, completa los siguientes datos: ") 
                print("=============================================================================")   
                Nombre=input("ingrese su nombre: ")
                apellido=input("Ingrese su apellido: ")                 
                cuit=input("Ingrese su documento: ")
                mail=input("Ingrese su mail: ") 
                pas=input("Ingrese su password: ")   
                cursor=conexion.cursor() #Genero el insert para completar los campos de la tabla usuarios
                sql="""INSERT INTO usuario(usuario,pass,id_rol,nombre,apellido,cuit,mail) 
                VALUES (%s,%s,%s,%s,%s,%s,%s);"""
                valores=(USU,pas,3,Nombre,apellido,cuit,mail)
                cursor.execute(sql,valores)   
                conexion.commit()
                print("=============================================================================")
                print("sus datos se registraron correctamente") 
                print("=============================================================================")
