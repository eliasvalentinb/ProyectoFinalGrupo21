# ProyectoFinalGrupo21
# INTEGRANTES  
*1.- Elías Valdez
*2.- Federico Cordoba
*3.- Adriel Delosanto
# PROYECTO FINAL
# SISTEMA DE GESTIÓN PARA TIENDA ONLINE 
## Descripción
Este proyecto consiste en el desarrollo de un sistema de gestión integral para una tienda online, cuya función es organizar y manipular los datos de productos, clientes y transacciones en una base de datos estructurada en MySQL. La tienda online permite registrar, actualizar, eliminar y visualizar datos relevantes para la
administración de inventario y ventas, brindando una solución completa de ecommerce de backend. La implementación de este sistema ha sido llevada a cabo en Python para la
lógica de negocio y conexión a la base de datos, con MySQL como sistema de almacenamiento. Se utilizaron bibliotecas adicionales de Python, como mysql.connector para la conexión y pandas para el manejo de datos.

## Estructura del proyecto final

Registro de Productos: Función para agregar nuevos productos a la base de datos.

Actualización de Productos: Función para modificar los detalles de productos existentes.

Eliminación de Productos: Función para eliminar productos del inventario.

Registro de Clientes: Función para agregar nuevos clientes.

Gestión de Transacciones: Funciones para registrar nuevas transacciones y actualizar el inventario.

Visualización de Datos: Funciones para recuperar y mostrar datos relevantes, como el inventario actual y el historial de ventas.

mysql.connector: Para establecer y gestionar la conexión con la base de datos MySQL.

## Funcionalidades Principales
El desarrollo de una tienda online permite automatizar la administración de productos e información de clientes, lo que facilita la organización de inventario y el seguimiento de ventas. Este proyecto busca ofrecer una herramienta útil y funcional que permita a pequeñas y medianas empresas llevar un registro eficiente
y detallado de sus transacciones sin depender de sistemas externos o pagos adicionales. Además, se eligió este proyecto para poner en práctica el uso de bases de datos, conexiones remotas y operaciones CRUD, competencias fundamentales en el área de desarrollo de software y ciencia de datos.


# EVIDENCIA 3
En la siguiente carpeta, de Evidencia3, encontraremos un proyecto de trabajo en donde anexamos a nuestra evidencia 2 ya presentada anteriormente. Un registro  de usuarios como el acceso se le anexo y tambien se le sumo un regitro flubial mensual en donde se puede ver la info guarda generando graficos en donde muestren dicha informacion de manera mas facil de leer y entendible.
Su respectivo archivo BBDD tambien fue adaptado para poder guardar dichos datos nuevos pedidos.

ARCHIVOS que Existen en la carpeta EVIDENCIA3:
BasedeDatos: encontraremos el script sql que utilizado para la correcta creacion de la base de datos 
Programcion1: contiene 4 archivos python donde se detallan los siguientes: 1 PROGRAMA COMPLETO Ev3 en donde contiene todo lo de la evidencia 2 pedida pero se le sumo el acceso y el registro de usuario como asi tambien los registros fluviales pedidos en esta evidencia.
Conectar_desconectar,  n donde tiene la conexion y la desconeccion del programa principal a la bases de datos misma
Consultas y filtrados, donde podran hacer consultas de los usuarios cargados en nuestra bases de datos 
Registro de Lluvias con Graficos donde podremos cargar un registro detallado y prolijo fluvial, como asi tambien poder generar graficos con dicha informacion cargada, para una mejor compresion y lectura.
En cuanto a una de las preguntas disparadoras, ¿Es necesario instalar algo, además de Python, para ejecutar el programa?, nuestra respuesta es la siguiente.
Para poder usar y poder ejecutar de manera correcta el archivo Python (1 PROGRAMA COMPLETO Ev3), debemos instalar la libreria pickle y esto se hace con el siguiente comando pip install pickle-mixin 
Tambien las librerias pandas y numpy ( con los siguientes comandos pip install pandas y pip install numpy) y la siguiente que es matplotlib (pip install matplotlib)
para la coneccion con la base de datos necesitamos instalar el comando  -m pip install mysql-connector-python





#EVIDENCIA 2
En la siguiente carpeta, de Evidencia2, encontraremos un proyecto de trabajo en donde anexamos a nuestra evidencia 1, ya presentada anteriormente, un sistema para el AGREGADO, MODIFICADO GUARDADO y ELIMINADO de usuarios (clientes) de nuestra tienda. 
Un menú desplegable y fácil de usar permite esto, desarrollado exclusivamente en Python. Además, ideamos, para la manipulación de estos datos sensibles, una base de datos en donde se podrá tener un seguimiento de los mismos.

ARCHIVOS que Existen en la carpeta EVIDENCIA2:
CARPETA Basededatos: Archivo BBDD_Tienda Online_Final (contiene el creado de tablas de la base de datos) y el Archivo Consigna de Evidencia 2 (contiene las consultas SQL solicitadas)
CARPETA Programacion1: Archivo 1 PROGRAMA COMPLETO (contiene el menú completo para el crud de los usuarios) y los demás archivos Python, por separados, que forman al menú antes mencionado)

En cuanto a una de las preguntas disparadoras, ¿Es necesario instalar algo, además de Python, para ejecutar el programa?, nuestra respuesta es la siguiente.
Para poder usar y poder ejecutar de manera correcta el archivo Python (1 PROGRAMA COMPLETO), debemos instalar la libreria pickle y esto se hace con el siguiente comando pip install pickle-mixin

Respecto de otra de las preguntas disparadoras, ¿Cómo ejecutar y probar este programa?, nuestra respuesta está a continuación.
Con solo abrir el programa (1 PROGRAMA COMPLETO), se encontrarán con un menú de opciones enumeradas que ejecutan distintas consignas, como el agregado y eliminado de usuarios, entre otros.












#EVIDENCIA 1
En equipo, hemos decidido armar una tienda online sobre productos de limpieza. A través de ella, los diversos usuarios (cliente y administrador) podrán navegar por categorías como "productos" y "pedidos", entre otros.
El fin último es que las compras sean ágiles y organizadas, y que los análisis de las compras permitan obtener evidencias para futuras mejoras.
Detallamos qué hallarán en cada carpeta:
**EVIDENCIA 1 / APLICACIÓN**: carpeta contenedora de todos los archivos solicitados para la evidencia 1.
**Documentos / Base de datos**: archivos "cimientos" de nuestra futura app, tales como la estructura del proyecto, los detalles de la base de datos y el DER.
**__pycache__**: archivos Python, solicitados desde Programación I, tales como "aritmética.cpython-312.pyc" y "registro.cpython-312.pyc".
Y luego, los archivos propios solicitados desde Programación I, tales como "aritmetica.py", "principal.py", "registrarse.py" y "prueba_aritmetica.py".
