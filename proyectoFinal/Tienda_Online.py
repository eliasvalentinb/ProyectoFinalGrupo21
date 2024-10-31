def carrito(usuario): #la funcion recibe como parametro el usuario que accedio, para luego asociarlo al pedido registrado en BBDD

 from datetime import datetime
 import Conectar_desconectar
 import mysql.connector 
 from mysql.connector import Error
 conexion= Conectar_desconectar.conexion()

 if conexion is None:  # Verifica si la conexión es None
    print("No se pudo establecer la conexión a la base de datos.")  
    return  # Sale de la función si no hay conexión 
 
 if conexion.is_connected():

        cliente = usuario #recibe el usuario que accedio para registrar el pedido
        carrito=[]
        total_compra = 0
        continuar = True
        while continuar:

            sql =f"""select c.id_categoria
                       ,c.descripcion
                    from categoria c 
                    where id_categoria is not null"""
            
            cursor=conexion.cursor()
            cursor.execute(sql) 
            resultados=cursor.fetchall()
            print(" ")
            print("                    CATEGORÍAS DE PRODUCTOS                         ")
            print("====================================================================")
            print ("Podemos ofrecerte las siguientes opciones: ")
            print("--------------------------------------------------------------------")
           
            categorias={}
            for fila in resultados:
                id_categoria, descripcion = fila  # Desempaquetar los resultados
                categorias[id_categoria] = descripcion  # Llenar el diccionario
                print(f"Ingrese: {id_categoria}, para la Categoría: {descripcion}")  
            print( " ")
            print("--------------------------------------------------------------------")
            
            Eleccion = int(input("Ingrese el numero de la categoria elegida: "))
            sql =f"""select p.id_producto
                        ,p.descripcion
                        ,p.precio
                        from producto p
                        where p.id_categoria ={Eleccion}"""
            cursor.execute(sql) 
            resultados=cursor.fetchall()

            print("====================================================================")
            print ("Podemos ofrecerte los siguientes PRODUCTOS dentro de esta categoría: ")
            print("--------------------------------------------------------------------")
            
            productos={}
            for fila in resultados:
                id_producto, descripcion,precio = fila  # Desempaquetar los resultados
                productos[id_producto] = [descripcion,precio]  # Llenar el diccionario
                print(f"Ingrese: {id_producto}, para el producto: {descripcion} - precio unitario: ${precio}")  
            print( " ")
            print("--------------------------------------------------------------------")

            id_prod = int(input("Ingrese el número del producto elegido: "))
            descrip = productos[id_prod][0]  # Obtener la descripción del producto
            precio = productos[id_prod][1]
            print(f"¿Qué candidad de {descrip} quiere comprar? ")
            cantidad = int(input(f"Ingrese la cantidad: "))
            Total = (cantidad * precio)

            carrito.append([id_prod,cantidad,descrip,precio,Total])
            total_compra += Total  # Acumula el total de la compra

            otra_compra = input("¿Desea agregar otro producto? (s/n): ")
            if otra_compra.lower() != 's':
              continuar = False

        print("--------------------------------------------------------------------")
        print("                      SU CARRITO DE COMPRAS                         ")
        print("====================================================================")

        for item in carrito:   
            print(f"Cantidad: {item[1]} - {item[2]} - Precio u.: ${item[3]} - Total: ${item[4]}")
        print("====================================================================")
        print(f"                          Total de la compra:       ${total_compra}")

        #GUARDA LA FECHA PARA REGISTRAR EL PEDIDO
        fecha = datetime.now()#.strftime("%Y%m%d-%Hh%Mm") #guarda la fecha

        #INSERT A TABLA PEDIDO
        cursor=conexion.cursor() #Genero el insert para completar los campos de la tabla pedidos
        sql="INSERT INTO pedido(fecha,usuario,monto) VALUES (%s,%s,%s);"
        valores=(fecha,cliente,total_compra)
        cursor.execute(sql,valores)   
        conexion.commit() 

        #BUSCA EL ID DEL ULTIMO PEDIDO PARA CARGAR EL DETALLE
        sql=" select max(id_pedido) from pedido; "
        cursor.execute(sql) 
        resultado = cursor.fetchone()
        id_pedido = resultado[0]


        #INSERTA EL DETALLE DE LOS PEDIDOS
        for item in carrito:
            sql="INSERT INTO detalle_pedido(id_pedido,id_producto,precio,cantidad) VALUES (%s,%s,%s,%s);"
            valores=(id_pedido,item[0],item[3],item[1])
            cursor.execute(sql,valores)   
        conexion.commit() 
        cursor.close()  # Cierra el cursor

    

 Conectar_desconectar.desconexion(conexion)



carrito("fcordoba")
