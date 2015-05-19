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
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Event` (
  `Event_ID` int(11) NOT NULL,
  `Event_Title` varchar(45) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Begin_time` varchar(45) DEFAULT NULL,
  `End_time` varchar(45) DEFAULT NULL,
  `Price` varchar(45) DEFAULT NULL,
  `Description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`Event_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (1,'Fashion Extravaganza','2013-09-30','18:00','21:00','15.00','A fashion walk featuring the most promising undergound designers. Be prepared to be awed by eclectic styles paired with unique motifs.'),(2,'The Art of Arts','2012-08-31','13:00','16:00','10.00','A peculiar art gallery giving opportunities to starving artists to make a few bucks.'),(3,'Random stuff','2013-10-27','20:00','22:00','20.00','A event gathering performers from all walks of life, ranging from kungfu Masters to magic wizards.'),(4,'Summoner\'s Rift','2013-09-10','09:00','23:00','5.00','You are the hero that BU deservers, but not the one it needs now. '),(5,'Dance your pants off','2013-11-09','19:00','22:00','25.00','Featuring below average dancers. Will be amusing.'),(6,'Crazy vocals','2012-12-05','18:00','21:00','3.00','Join us in a sinphony of cacophonic bunch of amateurial singers'),(7,'Dress to amuse','2013-10-31','21:00','22:00','5.00','Dress to amuse in our annual Halloween party!'),(8,'Moonlight Ball','2013-09-20','20:00','1:00','30.00','Find your prince charming/cindarella at rythm of tunes by DJ Dean Brown.'),(9,'All star Balls','2013-11-11','11:11','16:16','8.00','Gather in team of 5 and join in a competition involving all sorts of sports that features some sort of ball.'),(10,'Buffet Warlords','2013-12-12','12:12','14:14','10:00','All hail to the Buffet Warlord. Who will have to most elastic stomach to contain the mountain of food?');
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
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
