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
-- Table structure for table `Performance`
--

DROP TABLE IF EXISTS `Performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Performance` (
  `P_Email` varchar(45) NOT NULL,
  `Event_ID` int(11) NOT NULL,
  `Payment` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`P_Email`,`Event_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Performance`
--

LOCK TABLES `Performance` WRITE;
/*!40000 ALTER TABLE `Performance` DISABLE KEYS */;
INSERT INTO `Performance` VALUES ('darkswan@hotmail.it',1,'50.00'),('darkswan@hotmail.it',5,'48.00'),('dirtydancer@gmail.com',1,'30.00'),('dirtydancer@gmail.com',5,'32.00'),('everywantsme@gmail.com',1,'60.00'),('goosebumps@gmail.com',6,'65.00'),('hulksmash@gmail.com',10,'15.00'),('impression@gmail.com',2,'10.00'),('kungfungtime@gmail.com',3,'10.00'),('magickingdom@yahoo.ca',3,'20.00'),('makeyoucry@gmail.com',3,'30.00'),('makeyoucry@gmail.com',6,'40.00'),('moonwalkguru@gmail.it',5,'70.00'),('onmoney@gmail.com',2,'5.00'),('prettymodel@hotmail.com',1,'55.00'),('prettymodel@hotmail.com',8,'50.00'),('singdasong@gmail.com',6,'100.00');
/*!40000 ALTER TABLE `Performance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-12-08 17:22:23
