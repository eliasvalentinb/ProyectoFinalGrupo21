def conexion():
    import mysql.connector 
    from mysql.connector import Error

    try:
        conexion = mysql.connector.connect(
                                        
                                        host='localhost',
                                        port='3306',
                                        user='root',
                                        password='Betun$2025',
                                        db='tienda_online' #nombre de la BBDD
                                        )
        if conexion.is_connected():
                print("conexion exitosa")

    except Error as ex:
        print("error durante la conexion", ex)

    return (conexion)
    """finally:"""
#-----------------------------------------------------------------------------------------------------------

def desconexion(conexion1):
     conexion=conexion1 
     if conexion.is_connected():
        conexion.close() # se cerro la conexion a la BBDD
        print("la conexion ha finalizado");

