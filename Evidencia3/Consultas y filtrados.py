import Conectar_desconectar
import mysql.connector 
from mysql.connector import Error
conexion = Conectar_desconectar.conexion()

if conexion.is_connected():
  
   # SELECT PARA CONSULTAR LOS USUARIOS CREADOS
  Lista=[]
USU=input("ingrese un usuario: ") #pide el usuario para validar si esta disponible
if conexion.is_connected():
        print("conexion exitosa")
        cursor=conexion.cursor()
        cursor.execute("select * from Usuario;") 
        resultados=cursor.fetchall()
        for fila in resultados:       
            Lista.append(fila[1]) # me quedo con los usuarios creados en la tabla Usuarios
        print(Lista)
# INSERT PARA INCORPORAR UN NUEVO USUARIO
Usuario=input("ingrese su Nombre de Usuario: ")
Pass= input("Defina su contraseña: ")
Nombre=input("ingrese su nombre: ")
apellido=input("Ingrese su apellido: ") 
cuit=input("Ingrese su cuit: ")
mail=input("Ingrese su mail: ") 
cursor=conexion.cursor() 
    #Genero el insert para completar los campos de la tabla usuarios
sql="INSERT INTO Usuario(Usuario,Pass,id_rol,Nombre,Apellido,cuit,mail) VALUES (%s,%s,%s,%s,%s,%s,%s);"
valores=(Usuario,Pass,"1",Nombre,apellido,cuit,mail) #todos los usuarios por plataforma son rol cliente
cursor.execute(sql,valores)   
conexion.commit() 

    # UPDATE PARA ACTUALIZACION DE DATOS
cursor=conexion.cursor() 
modificar = input("que producto quiere modificar? (ingrese el Id) ")
Nueva_cantidad = input("cual es el nuevo stock? ")
sql= f"""UPDATE inventario SET canticad = {Nueva_cantidad} WHERE id_inventario = {modificar}; """
cursor=conexion.cursor()
cursor.execute(sql) 
conexion.commit()

    # DELETE PARA BORRAR UN USUARIO
Usuario=input("ingrese el Nombre de Usuario a eliminar: ")
cursor=conexion.cursor()
sql= f"""DELETE USUARIO WHERE Usuario = {Usuario}; """
cursor=conexion.cursor()
cursor.execute(sql) 
conexion.commit()

    #CONSULTA QUE MUESTRALOS USAUARIOS CON LA DESCRIPCION DEL ROL CORRESPONDIENTE
cursor=conexion.cursor()
sql= f"""SELECT
	            u.Nombre
	           ,u.Apellido
	           ,u.usuario
	           ,r.Nombre       as Rol
             FROM usuario u
             INNER JOIN rol r ON (u.id_rol = r.idRol); """
cursor.execute(sql) 
resultados=cursor.fetchall()
for fila in resultados:       
       print(fila)

   #CONSULTA QUE MUESTRA CANTIDAD DEPRODUCTOS POR CATEGORIA Y PROVEEDOR
cursor=conexion.cursor()
sql= f"""SELECT 
	             c.descripcion         AS Categoria
	            ,p.Nombre              AS Proveedor
	            ,SUM(i.cantidad)       AS Total
             FROM inventario i
             INNER JOIN proveedor p ON (i.Id_proveedor = p.Id_proveedor)
             INNER JOIN Producto pr ON (i.Id_producto = pr.id_producto)
             INNER JOIN Categoria c ON (pr.id_categoria = c.id_categoria)
             GROUP BY c.descripcion, p.Nombre; """
cursor.execute(sql) 
resultados=cursor.fetchall()
for fila in resultados:       
       print(fila)
       
         
Conectar_desconectar.desconexion(conexion)