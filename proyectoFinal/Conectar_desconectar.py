def conexion():
    import mysql.connector 
    from mysql.connector import Error
    conexion = None 
    try:
        conexion = mysql.connector.connect(
                                        
                                        host='localhost',
                                        port='3306',
                                        user='root',
                                        password='Elias123',
                                        db='tienda_online_final' #nombre de la BBDD
                                        )
        if conexion.is_connected():
                print("Conexión exitosa")

    except Error as ex:
        print("Error durante la conexión", ex)

    return (conexion)
    """finally:"""
#-----------------------------------------------------------------------------------------------------------

def desconexion(conexion1):
     conexion=conexion1 
     if conexion.is_connected():
        conexion.close() # se cerro la conexion a la BBDD
        print("La conexión ha finalizado");

