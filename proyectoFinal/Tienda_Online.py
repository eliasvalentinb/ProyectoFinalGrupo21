def carrito(usuario): #la funcion recibe como parametro el usuario que accedio, para luego asociarlo al pedido registrado en BBDD
 import datetime
 import Conectar_desconectar
 import mysql.connector 
 from mysql.connector import Error
 conexion= Conectar_desconectar.conexion() 
 
 if conexion.is_connected():

        cliente = usuario
        carrito={}
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
            print("                    CATEGORIAS DE PRODUCTOS                         ")
            print("====================================================================")
            print ("Podemos ofrecerte las siguientes opciones")
            print("--------------------------------------------------------------------")
           
            categorias={}
            for fila in resultados:
                id_categoria, descripcion = fila  # Desempaquetar los resultados
                categorias[id_categoria] = descripcion  # Llenar el diccionario
                print(f"Ingrese: {id_categoria}, para la Categoría: {descripcion}")  
            print( " ")
            print("--------------------------------------------------------------------")
            
            Eleccion = int(input("ingrese el numero de la categoria elegida: "))
            sql =f"""select p.id_producto
                        ,p.descripcion
                        ,p.id_categoria
                        from producto p
                        where p.id_categoria ={Eleccion}"""
            cursor.execute(sql) 
            resultados=cursor.fetchall()

            print("====================================================================")
            print ("Podemos ofrecerte los siguientes PRODUCTOS dentro de esta categoria")
            print("--------------------------------------------------------------------")
            
            productos={}
            for fila in resultados:
                id_producto, descripcion,id_categoria = fila  # Desempaquetar los resultados
                productos[id_producto] = [descripcion,id_categoria]  # Llenar el diccionario
                print(f"Ingrese: {id_producto}, para el producto: {descripcion} - precio unitario:  {id_categoria}")  
            print( " ")
            print("--------------------------------------------------------------------")

            id_prod = int(input("ingrese el numero del producto elegido: "))
            descrip = productos[id_prod][0]  # Obtener la descripción del producto
            precio = productos[id_prod][1]
            print(f"¿Que candidad de {descrip} quiere comprar? ")
            cantidad = int(input(f"Ingrese la cantidad: "))
            Total = (cantidad * precio)

            carrito[id_prod]=[cantidad,descrip,precio,Total]
            total_compra += Total  # Acumula el total de la compra

            otra_compra = input("¿Desea agregar otro producto? (s/n): ")
            if otra_compra.lower() != 's':
              continuar = False

        print("--------------------------------------------------------------------")
        print("                      SU CARRITO DE COMPRAS                         ")
        print("====================================================================")

        for item in carrito.values():   
            print(f"Cantidad: {item[0]} - {item[1]} - Precio: ${item[2]} - Total: ${item[3]}")
        print("====================================================================")
        print(f"                          Total de la compra:       ${total_compra}")


      # me falta sumar que pegue el pedido en la BBDD y luego el detalle de la compra

 Conectar_desconectar.desconexion(conexion)



carrito()
