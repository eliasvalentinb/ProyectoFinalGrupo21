/* select para la validacion de usuarios se utilizaria en el bloque de login*/
SELECT 
	usuario
	,pass
FROM usuarios
LIMIT 10;

/*Insert para incorporar un nuevo usuario*/
INSERT INTO usuarios (Usuario,Pass,IdRol,Nombre,Apellido,cuit,mail) VALUES
("fcordoba",	"1234",	3,	"Federico",	"Cordoba",	"11111111111",	"mail@mail.com");

/*Update para actualizacion de datos*/
UPDATE inventario
SET cantidad = 200
WHERE Id_Inventario= 10;

/*DELETE para borrar un usuario*/
DELETE FROM Proveedor WHERE Id_proveedor =3;

/* Consulta que muestra los usuarios con la descripcion del rol correspondiente*/
SELECT
	 u.Nombre
	,u.Apellido
	,u.usuario
	,r.Nombre   as Rol
FROM usuarios u
INNER JOIN rol r ON (u.IdRol = r.idRol);

/* consulta que muestra la cantidad de productos por categorias y proveedor */
SELECT 
	c.descripcion          AS Categoria
	,p.Nombre              AS Proveedor
	,SUM(i.cantidad)       AS Total
FROM inventario i
INNER JOIN proveedor p ON (i.Id_proveedor = p.Id_proveedor)
INNER JOIN Productos pr ON (i.Id_producto = pr.id_producto)
INNER JOIN Categoria c ON (pr.id_categoria = c.id_categoria)
GROUP BY c.descripcion, p.Nombre;