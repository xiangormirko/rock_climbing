CREATE DATABASE  IF NOT EXISTS `xiang` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `xiang`;
-- MySQL dump 10.13  Distrib 5.6.13, for osx10.6 (i386)
--
-- Host: smgresearch1.bu.edu    Database: xiang
-- ------------------------------------------------------
-- Server version	5.1.71

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Performer`
--

DROP TABLE IF EXISTS `Performer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Performer` (
  `P_Email` varchar(45) NOT NULL,
  `P_FName` varchar(45) DEFAULT NULL,
  `P_LName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`P_Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Performer`
--

LOCK TABLES `Performer` WRITE;
/*!40000 ALTER TABLE `Performer` DISABLE KEYS */;
INSERT INTO `Performer` VALUES ('1inchpunch@gmail.com','Bruce','Lee'),('catwalkmaster@gmail.com','Naomi','Campbell'),('dacingintherain@hotmail.com','Charlie','Chaplin'),('daplayer@yahoo.com','David','Beckam'),('darkswan@hotmail.it','Natalie','Portman'),('dirtydancer@gmail.com','Jessica','Alba'),('everywantsme@gmail.com','Candice','Swanepoel'),('goosebumps@gmail.com','Adele','Wonderful'),('hulksmash@gmail.com','Hulk','Hogan'),('impression@gmail.com','Claude','Monet'),('kungfungtime@gmail.com','Chung','Li'),('magickingdom@yahoo.ca','David','Blaine'),('makeyoucry@gmail.com','Bryan','Adams'),('moonwalkguru@gmail.it','Michael','Jackson'),('onmoney@gmail.com','Picasso','Cambiasso'),('prettymodel@hotmail.com','Kate','Upton'),('singdasong@gmail.com','Macklemore','Awesome'),('theyoyomaster@gmail.com','Yo-Yo','Ma'),('victoriasecret@gmail.com','Victoria','Secret'),('youcantseeme@gmail.com','David','Copperfield');
/*!40000 ALTER TABLE `Performer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-08 17:22:24
