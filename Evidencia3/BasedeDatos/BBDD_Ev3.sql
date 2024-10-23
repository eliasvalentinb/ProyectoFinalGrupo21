-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: tienda_online
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categoria`
--

DROP TABLE IF EXISTS `categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categoria` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `descripcion` text,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoria`
--

LOCK TABLES `categoria` WRITE;
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` VALUES (1,'Limpieza Cocina'),(2,'Limpieza Baño'),(3,'Superfices Delicadas'),(4,'Limpieza Ropa'),(5,'Accesorios'),(6,'Aromatizantes y desinfección');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_pedido`
--

DROP TABLE IF EXISTS `detalle_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_pedido` (
  `id_detalle_pedido` int NOT NULL,
  `id_pedido` int NOT NULL,
  `id_producto` int NOT NULL,
  PRIMARY KEY (`id_detalle_pedido`),
  KEY `Id_producto_idx` (`id_producto`),
  KEY `Id_pedido_idx` (`id_pedido`),
  CONSTRAINT `Id_pedido` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`),
  CONSTRAINT `Id_producto_D` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_pedido`
--

LOCK TABLES `detalle_pedido` WRITE;
/*!40000 ALTER TABLE `detalle_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `id_inventario` int NOT NULL AUTO_INCREMENT,
  `id_proveedor` int NOT NULL,
  `id_producto` int NOT NULL,
  `Cantidad` int NOT NULL,
  PRIMARY KEY (`id_inventario`),
  KEY `Id_producto_idx` (`id_producto`),
  KEY `Id_proveedor_idx` (`id_proveedor`),
  CONSTRAINT `Id_producto_I` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  CONSTRAINT `Id_proveedor_P` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
INSERT INTO `inventario` VALUES (1,1,1,100),(2,1,2,100),(3,1,3,100),(4,1,4,100),(5,1,5,100),(6,1,6,100),(7,1,7,100),(8,2,8,100),(9,2,9,100),(10,2,10,100),(11,2,11,100),(12,3,12,100),(13,3,13,100),(14,3,14,100),(15,3,15,100),(16,3,16,100),(17,4,17,100),(18,4,18,100),(19,4,19,100),(20,4,20,100),(21,4,21,100),(22,1,22,100),(23,1,23,100),(24,1,24,100);
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `id_usuario` int NOT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `Id_Usuario_idx` (`id_usuario`),
  CONSTRAINT `Usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuarios`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `descripcion` text,
  `id_categoria` int NOT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `Id_categoria_idx` (`id_categoria`),
  CONSTRAINT `Id_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Limpia Hornos',1),(2,'Detergente',1),(3,'Desengrasante',1),(4,'Limpia Inodoros',2),(5,'Lisoform',6),(6,'Poet',6),(7,'Lavandina',6),(8,'Cif Gel',6),(9,'Cera Para Piso',6),(10,'Lustra Muesbles',3),(11,'Limpia Vidrios',3),(12,'Blem Electro',3),(13,'Suavizante',4),(14,'Jabon Liquido',4),(15,'Jabon En Polvo',4),(16,'Jabon En Pan',4),(17,'Quita Manchas',4),(18,'Escobas',5),(19,'Escobillones',5),(20,'Secadores',5),(21,'Rejillas',5),(22,'Esponjas',5),(23,'Paño Amarillo',5),(24,'Trapo Piso',5);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  `cuit` varchar(64) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'351111116','Don Manolo','3512111111'),(2,'358888884','LIMPRO','3526444444'),(3,'352222221','Jhonson','2654333333'),(4,'3599999997','Dalton','8002226564');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `idRol` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  PRIMARY KEY (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'Cliente','Hacer comparas'),(2,'Vendedor','Ver reportes '),(3,'Administrador','Administrador');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuarios` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(45) NOT NULL,
  `pass` varchar(64) NOT NULL,
  `id_rol` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `cuit` varchar(45) NOT NULL,
  `mail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuarios`),
  KEY `IdRol_idx` (`id_rol`),
  CONSTRAINT `IdRol` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'fcordoba','1234',3,'Federico','Cordoba','11111111111','mail@mail.com'),(2,'evaldez','1234',3,'Elías','Valdez','11111111112','mail@mail.com'),(3,'adelosanto','1234',3,'Adriel','Delosanto','11111111113','mail@mail.com'),(4,'ypesqueira','1234',3,'Yesica','Pesqueira','11111111114','mail@mail.com'),(5,'cmontivero','1234',3,'María Celeste','Montivero','11111111115','mail@mail.com'),(6,'lferreyra','1234',3,'Lourdes','Ferreyra Farías','11111111116','mail@mail.com');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-21  8:44:17
