-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: chilamlol.mysql.pythonanywhere-services.com    Database: chilamlol$alumni
-- ------------------------------------------------------
-- Server version	5.7.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_alumni`
--

DROP TABLE IF EXISTS `tbl_alumni`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_alumni` (
  `alumniId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `identificationCard` varchar(30) DEFAULT NULL,
  `studentId` varchar(20) DEFAULT NULL,
  `personalEmail` varchar(50) DEFAULT NULL,
  `studentHandphone` varchar(20) DEFAULT NULL,
  `studentTelephoneNumber` varchar(20) DEFAULT NULL,
  `graduatingCampus` varchar(10) DEFAULT NULL,
  `yearOfGraduation` varchar(20) DEFAULT NULL,
  `graduatingProgramme` varchar(20) DEFAULT NULL,
  `graduatedProgrammeName` varchar(100) DEFAULT NULL,
  `levelOfStudy` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`alumniId`),
  UNIQUE KEY `studentId` (`studentId`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_alumni`
--

LOCK TABLES `tbl_alumni` WRITE;
/*!40000 ALTER TABLE `tbl_alumni` DISABLE KEYS */;
INSERT INTO `tbl_alumni` VALUES (1,'Chin Thiam Fatt','000308141505','I18014685','stevechin83@gmail.com','60128388813','60128388813','IU','2019','DITN','Diploma in IT','diploma'),(3,'Syakirah Noorizam','A1273845','J180141111','test@com.com','911','911','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(4,'Larry King','991221141234','J180142222','guanhong2@gmail.com','60123456789','60123456789','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(5,'Hugh Jackman','721212121212','J180143333','Jackman@gmail.com','0123456789','60123456789','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(6,'Beff Jezos','001122345678','J9876543210','guanhong2@gmail.com','60123456789','60123456789','IICS','2022','DITN','Diploma in IT','diploma'),(7,'steady','123456121234','J123456789','syakirah.noorizam@newinti.edu.my','0123853230','0123853230','iics','2022','CSIT','Computer Science','Degree'),(9,'Thiam Fatt CHIN','991212141212','J20020200','stevechin83@gmail.com','0128388813','0128388813','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(11,'Chin Thiam Fatt','991212151212','J20022200','stevechin83@gmail.com','60128388813','60128388813','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(12,'Chin Thiam Fatt','991212141212','J20023200','stevechin83@gmail.com','60128388813','0128388813','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(13,'a','a','a','a','11111111111,,,','1234567890','a','a','a','e','diploma'),(15,'Johnny Depp','000000100000','firstlogin','kokhau000904@gmail.com','0122172333','123456789-','iics','2022','csit','computer science','degree'),(16,'Chin Thiam Fatt','000308141234','J20033757','stevechin83@gmail.com','0128388813','0128388813','IICS','2022','CADP','Computer Science','degree'),(17,'','','','a','a','','','','','',''),(19,'She Kok Hau','000904100857','J18026324','kokhau000904@gmail.com','60122172333','','IICS','2022','CAPD','Software Engineering and Digital Security','degree'),(20,'John Smith','0001212141234','J20088123','stevechin83@gmail.com','60123455532','60123456258','IICS','2022','CADP','Software Engineering','degree'),(21,'Hugo Chin','000308141505','I180141234','Stevechin83@gmail.com','60128388812','60128388812','IICS','2022','CADP','Software Engineering','degree'),(22,'Hugo Chin','000308141505','I18014666','stevechin83@gmail.com','60128388813','60128388813','IICS','2022','CADP','Computer Science','degree');
/*!40000 ALTER TABLE `tbl_alumni` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_banner`
--

DROP TABLE IF EXISTS `tbl_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_banner` (
  `bannerId` int(11) NOT NULL AUTO_INCREMENT,
  `bannerImage` varchar(300) DEFAULT NULL,
  `startDate` varchar(20) DEFAULT NULL,
  `endDate` varchar(20) DEFAULT NULL,
  `sequence` varchar(80) DEFAULT NULL,
  `recordStatus` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`bannerId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_banner`
--

LOCK TABLES `tbl_banner` WRITE;
/*!40000 ALTER TABLE `tbl_banner` DISABLE KEYS */;
INSERT INTO `tbl_banner` VALUES (1,'https://www.hugoboss.com','12/12/2012','22/02/2022','apa ni idk','true'),(3,'https://www.shark.com','12/12/2012','22/02/2022','apa ni idk','true');
/*!40000 ALTER TABLE `tbl_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_comment`
--

DROP TABLE IF EXISTS `tbl_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_comment` (
  `commentId` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(5000) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  `status` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `postId` int(11) NOT NULL,
  PRIMARY KEY (`commentId`),
  KEY `postId` (`postId`),
  KEY `userId` (`userId`),
  CONSTRAINT `tbl_comment_ibfk_1` FOREIGN KEY (`postId`) REFERENCES `tbl_post` (`postId`),
  CONSTRAINT `tbl_comment_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `tbl_user` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_comment`
--

LOCK TABLES `tbl_comment` WRITE;
/*!40000 ALTER TABLE `tbl_comment` DISABLE KEYS */;
INSERT INTO `tbl_comment` VALUES (1,'this is a test comment','2022-06-14 09:27:12','2022-06-14 09:27:12',1,12,1),(2,'this is another test comment','2022-06-14 08:25:21','2022-06-14 08:25:21',1,1,1),(4,'hi','2022-06-22 01:38:13','2022-06-22 01:38:13',1,1,1),(5,'heelo','2022-06-22 01:42:41','2022-06-22 01:42:41',1,1,6),(6,'erferf','2022-06-22 01:44:27','2022-06-22 01:44:27',1,1,6),(7,'ded','2022-06-22 01:48:20','2022-06-22 01:48:20',1,1,1),(8,'hello','2022-06-22 01:55:19','2022-06-22 01:55:19',1,1,2),(9,'Hello','2022-06-22 06:08:00','2022-06-22 06:08:00',1,1,5),(10,'Fantastic!','2022-06-22 08:03:41','2022-06-22 08:03:41',1,19,2),(11,'a','2022-07-08 08:30:44','2022-07-08 08:30:44',1,1,1);
/*!40000 ALTER TABLE `tbl_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_event`
--

DROP TABLE IF EXISTS `tbl_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_event` (
  `eventId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `description` mediumtext CHARACTER SET utf8,
  `image` varchar(150) NOT NULL,
  `registerLink` varchar(150) NOT NULL,
  `startDate` datetime NOT NULL,
  `endDate` datetime NOT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`eventId`),
  KEY `statusId` (`status`),
  CONSTRAINT `tbl_event_ibfk_1` FOREIGN KEY (`status`) REFERENCES `tbl_status` (`statusId`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_event`
--

LOCK TABLES `tbl_event` WRITE;
/*!40000 ALTER TABLE `tbl_event` DISABLE KEYS */;
INSERT INTO `tbl_event` VALUES (13,'Network your Way up Digitally','NETWORK is your NETWORTH,\nWe are proud to have our special guest speaker Mr. Marcus Teoh, an INTI Alumnus from the Class of 2000, Bestselling Author, and an International Speaker to do his sharing with the alumni. He will be delivering an interesting and important topic, “Network your Way up Digitally”. Do not miss the chance to listen to his sharing and gain insightful knowledge through this session. You will also have the chance to network and exchange ideas with other participants during the networking session. See you at the event!','https://i.imgur.com/gDUewqY.jpg','https://tinyurl.com/intinetworking','2022-07-30 12:00:00','2022-08-01 16:00:00',1),(14,'Alumni Sharing Knowledge Session','Dear Alumni, \nWe are 2 days away from our Alumni Sharing Knowledge Session!\nJoin us in the first Alumni Sharing Knowledge Session in 2022 and this round, we are lucky to have our three alumni, Nur Zulaikha (currently working in Ezrilaw Firm), @⁨Mun Hong Teoh⁩ (currently working in Microsoft Malaysia) and Mohnish Patel (currently working in PWC) as the speakers for the session with the title “Expectations & Challenges From Your First Jobs.”','https://i.imgur.com/HoKVmH5.jpg','https://tinyurl.com/ASK2022','2022-07-14 17:00:00','2022-07-17 18:00:00',1),(24,'Sea The Change','CSR event ','https://i.imgur.com/Oa4MfMq.jpg','https://docs.google.com/forms/d/1QJcgBsYhvwz-Ygpg80Hrja6xXPHM4CdrIpkP0zFXg1c/edit#responses','2022-08-01 07:45:00','2022-08-31 11:30:00',1),(25,'Hello','Hello','https://i.imgur.com/ZmwvqU3.jpg','www.google.com','2022-06-25 16:48:00','2022-06-25 17:48:00',1);
/*!40000 ALTER TABLE `tbl_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_event_activity`
--

DROP TABLE IF EXISTS `tbl_event_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_event_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `eventId` int(11) NOT NULL,
  `eventType` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13501 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_event_activity`
--

LOCK TABLES `tbl_event_activity` WRITE;
/*!40000 ALTER TABLE `tbl_event_activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_event_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_event_strength`
--

DROP TABLE IF EXISTS `tbl_event_strength`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_event_strength` (
  `trainingId` int(11) NOT NULL AUTO_INCREMENT,
  `eventId` int(11) NOT NULL,
  `eventStrength` float NOT NULL,
  `createdDate` date DEFAULT NULL,
  PRIMARY KEY (`trainingId`),
  KEY `eventId` (`eventId`),
  CONSTRAINT `tbl_event_strength_ibfk_1` FOREIGN KEY (`eventId`) REFERENCES `tbl_event` (`eventId`)
) ENGINE=InnoDB AUTO_INCREMENT=1279 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_event_strength`
--

LOCK TABLES `tbl_event_strength` WRITE;
/*!40000 ALTER TABLE `tbl_event_strength` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_event_strength` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_faq`
--

DROP TABLE IF EXISTS `tbl_faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_faq` (
  `faqId` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(200) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL,
  `recordStatus` varchar(10) DEFAULT NULL,
  `faqCatId` int(11) DEFAULT NULL,
  PRIMARY KEY (`faqId`),
  KEY `faqCatId` (`faqCatId`),
  CONSTRAINT `tbl_faq_ibfk_1` FOREIGN KEY (`faqCatId`) REFERENCES `tbl_faq_category` (`faqCatId`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_faq`
--

LOCK TABLES `tbl_faq` WRITE;
/*!40000 ALTER TABLE `tbl_faq` DISABLE KEYS */;
INSERT INTO `tbl_faq` VALUES (13,'Question 1','Answer 1','true',16),(14,'Where is INTI','INTI is located at bottom of my heart','true',16),(15,'Question 2','Question ','true',17);
/*!40000 ALTER TABLE `tbl_faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_faq_category`
--

DROP TABLE IF EXISTS `tbl_faq_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_faq_category` (
  `faqCatId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `recordStatus` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`faqCatId`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_faq_category`
--

LOCK TABLES `tbl_faq_category` WRITE;
/*!40000 ALTER TABLE `tbl_faq_category` DISABLE KEYS */;
INSERT INTO `tbl_faq_category` VALUES (16,'General','true'),(17,'First','true');
/*!40000 ALTER TABLE `tbl_faq_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_like`
--

DROP TABLE IF EXISTS `tbl_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_like` (
  `postId` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`userId`,`postId`),
  KEY `postId` (`postId`),
  CONSTRAINT `tbl_like_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `tbl_user` (`userId`),
  CONSTRAINT `tbl_like_ibfk_2` FOREIGN KEY (`postId`) REFERENCES `tbl_post` (`postId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_like`
--

LOCK TABLES `tbl_like` WRITE;
/*!40000 ALTER TABLE `tbl_like` DISABLE KEYS */;
INSERT INTO `tbl_like` VALUES (1,1,0),(2,1,1),(6,1,1),(1,7,1),(2,7,NULL),(1,8,1),(2,10,NULL),(1,19,1),(2,19,1);
/*!40000 ALTER TABLE `tbl_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_merchant`
--

DROP TABLE IF EXISTS `tbl_merchant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_merchant` (
  `merchantId` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `logo` varchar(150) NOT NULL COMMENT 'logo image link url',
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`merchantId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_merchant`
--

LOCK TABLES `tbl_merchant` WRITE;
/*!40000 ALTER TABLE `tbl_merchant` DISABLE KEYS */;
INSERT INTO `tbl_merchant` VALUES (1,'Starbucks','https://chilamlol.pythonanywhere.com/static/1_Profile_20220622042656.jpg','2022-06-17 12:40:19','2022-06-17 12:40:19',1),(2,'Kenny Rogers Roasters','https://chilamlol.pythonanywhere.com/static/1_Profile_20220622043207.jpg','2022-06-17 12:40:19','2022-06-17 12:40:19',1);
/*!40000 ALTER TABLE `tbl_merchant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_notification`
--

DROP TABLE IF EXISTS `tbl_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_notification` (
  `notificationId` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `image` varchar(150) NOT NULL,
  `push` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`notificationId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_notification`
--

LOCK TABLES `tbl_notification` WRITE;
/*!40000 ALTER TABLE `tbl_notification` DISABLE KEYS */;
INSERT INTO `tbl_notification` VALUES (1,'t','ff','efw',1,'2022-06-17 16:47:15','2022-06-17 16:54:15',1),(2,'testadd','anything','',1,'2022-06-27 15:57:50','2022-06-28 05:57:01',1);
/*!40000 ALTER TABLE `tbl_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_otp`
--

DROP TABLE IF EXISTS `tbl_otp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_otp` (
  `otpId` int(11) NOT NULL AUTO_INCREMENT,
  `personalEmail` varchar(50) DEFAULT NULL,
  `otp` int(6) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`otpId`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_otp`
--

LOCK TABLES `tbl_otp` WRITE;
/*!40000 ALTER TABLE `tbl_otp` DISABLE KEYS */;
INSERT INTO `tbl_otp` VALUES (1,'chilamlol@hotmail.com',990687,'2021-12-16'),(2,'chilamlol@hotmail.com',599674,'2021-12-16'),(3,'stevechin83@gmail.com',726511,'2021-12-23'),(4,'stevechin83@gmail.com',656028,'2021-12-28'),(5,'stevechin83@gmail.com',458820,'2021-12-28'),(6,'stevechin83@gmail.com',676158,'2021-12-28'),(7,'stevechin83@gmail.com',52380,'2021-12-28'),(8,'stevechin83@gmail.com',25866,'2021-12-28'),(9,'stevechin83@gmail.com',473122,'2021-12-28'),(10,'stevechin83@gmail.com',578308,'2021-12-28'),(11,'stevechin83@gmail.com',224815,'2021-12-28'),(12,'stevechin83@gmail.com',931941,'2021-12-28'),(13,'stevechin83@gmail.com',76204,'2021-12-28'),(14,'stevechin83@gmail.com',845374,'2021-12-28'),(15,'stevechin83@gmail.com',923442,'2021-12-28'),(16,'stevechin83@gmail.com',629123,'2021-12-28'),(17,'stevechin83@gmail.com',901252,'2021-12-28'),(18,'larry@gmail.com',22803,'2021-12-30'),(19,'guanhong2@gmail.com',124434,'2021-12-30'),(20,'beff@jezos.com',521256,'2021-12-30'),(21,'guanhong2@gmail.com',681213,'2021-12-30'),(22,'syakirah.noorizam@newinti.edu.my',288634,'2022-01-03'),(23,'kokhau000904@gmail.com',489950,'2022-01-22'),(24,'kokhau000904@gmail.com',939545,'2022-03-15'),(25,'kokhau000904@gmail.com',581572,'2022-03-15'),(26,'kokhau000904@gmail.com',744943,'2022-03-15'),(27,'kokhau000904@gmail.com',759911,'2022-03-15'),(28,'stevechin83@gmail.com',312901,'2022-03-24'),(29,'kokhau000904@gmail.com',696905,'2022-03-24'),(30,'kokhau000904@gmail.com',780172,'2022-03-24'),(31,'stevechin83@gmail.com',767390,'2022-04-08'),(32,'stevechin83@gmail.com',773819,'2022-04-08'),(33,'stevechin83@gmail.com',775024,'2022-04-08'),(34,'stevechin83@gmail.com',222719,'2022-04-08'),(35,'stevechin83@gmail.com',38467,'2022-04-08'),(36,'stevechin83@gmail.com',881974,'2022-04-15'),(37,'stevechin83@gmail.com',653759,'2022-04-27'),(38,'syakirah.noorizam@newinti.edu.my',566979,'2022-04-29'),(39,'hugochin0803@gmail.com',597239,'2022-05-17'),(40,'hugochin0803@gmail.com',439867,'2022-05-17'),(41,'stevechin83@gmail.com',128377,'2022-05-17'),(42,'stevechin83@gmail.com',810724,'2022-05-17'),(43,'stevechin83@gmail.com',451378,'2022-05-17'),(44,'hugochin0803@gmail.com',438737,'2022-05-17'),(45,'stevechin83@gmail.com',870381,'2022-05-18'),(46,'stevechin83@gmail.com',923155,'2022-05-18'),(47,'stevechin83@gmail.com',27289,'2022-06-13'),(48,'stevechin83@gmail.com',178130,'2022-06-13'),(49,'stevechin83@gmail.com',997092,'2022-06-14'),(50,'stevechin83@gmail.com',407233,'2022-06-14'),(51,'stevechin83@gmail.com',545293,'2022-06-14'),(52,'stevechin83@gmail.com',138166,'2022-06-14'),(53,'stevechin83@gmail.com',138763,'2022-06-14'),(54,'stevechin83@gmail.com',149522,'2022-06-14'),(55,'stevechin83@gmail.com',961082,'2022-06-14'),(56,'stevechin83@gmail.com',943898,'2022-06-14'),(57,'stevechin83@gmail.com',717769,'2022-06-14'),(58,'stevechin83@gmail.com',97995,'2022-06-14'),(59,'stevechin83@gmail.com',432552,'2022-06-14'),(60,'stevechin83@gmail.com',577910,'2022-06-14'),(61,'stevechin83@gmail.com',394870,'2022-06-14'),(62,'stevechin83@gmail.com',748723,'2022-06-14'),(63,'stevechin83@gmail.com',56076,'2022-06-14'),(64,'stevechin83@gmail.com',782413,'2022-06-14'),(65,'stevechin83@gmail.com',107088,'2022-06-14'),(66,'stevechin83@gmail.com',571756,'2022-06-14'),(67,'stevechin83@gmail.com',982637,'2022-06-14'),(68,'stevechin83@gmail.com',232368,'2022-06-14'),(69,'stevechin83@gmail.com',762155,'2022-06-14'),(70,'stevechin83@gmail.com',747365,'2022-06-14'),(71,'stevechin83@gmail.com',721503,'2022-06-14'),(72,'stevechin83@gmail.com',340813,'2022-06-14'),(73,'stevechin83@gmail.com',751790,'2022-06-14'),(74,'stevechin83@gmail.com',839790,'2022-06-14'),(75,'stevechin83@gmail.com',463914,'2022-06-14'),(76,'stevechin83@gmail.com',523215,'2022-06-14'),(77,'stevechin83@gmail.com',NULL,'2022-06-14'),(78,'stevechin83@gmail.com',84313,'2022-06-14'),(79,'stevechin83@gmail.com',244420,'2022-06-14'),(80,'stevechin83@gmail.com',40496,'2022-06-14'),(81,'stevechin83@gmail.com',326586,'2022-06-14'),(82,'chilamlol@hotmail.com',282328,'2022-06-14'),(83,'j18027823@student.newinti.edu.my',462032,'2022-06-14'),(84,'j18027823@student.newinti.edu.my',762825,'2022-06-14'),(85,'test-aotaruzw4@srv1.mail-tester.com',445449,'2022-06-14'),(86,'j18027823@student.newinti.edu.my',332754,'2022-06-14'),(87,'stevechin83@gmail.com',813843,'2022-06-14'),(88,'stevechin83@gmail.com',62033,'2022-06-14'),(89,'stevechin83@gmail.com',460451,'2022-06-14'),(90,'stevechin83@gmail.com',848364,'2022-06-14'),(91,'stevechin83@gmail.com',20838,'2022-06-14'),(92,'Stevechin83@gmail.com',490822,'2022-06-14'),(93,'Stevechin83@gmail.com',450760,'2022-06-14'),(94,'Stevechin83@gmail.com',978805,'2022-06-14'),(95,'stevechin83@gmail.com',596840,'2022-06-14'),(96,'stevechin83@gmail.com',349403,'2022-06-16'),(97,'stevechin83@gmail.com',774874,'2022-06-19'),(98,'stevechin83@gmail.com',556526,'2022-06-19'),(99,'stevechin83@gmail.com',780700,'2022-06-19'),(100,'stevechin83@gmail.com',133533,'2022-06-19'),(101,'stevechin83@gmail.com',418073,'2022-06-19'),(102,'stevechin83@gmail.com',197358,'2022-06-19'),(103,'stevechin83@gmail.com',7511,'2022-06-19'),(104,'stevechin83@gmail.com',901935,'2022-06-19'),(105,'stevechin83@gmail.com',670797,'2022-06-19'),(106,'stevechin83@gmail.com',943469,'2022-06-19'),(107,'stevechin83@gmail.com',814111,'2022-06-19'),(108,'stevechin83@gmail.com',615320,'2022-06-19'),(109,'stevechin83@gmail.com',619155,'2022-06-19'),(110,'j20033757@student.newinti.edu.my',758622,'2022-06-19'),(111,'j20033757@student.newinti.edu.my',686246,'2022-06-19'),(112,'j20033757@student.newinti.edu.my',318421,'2022-06-19'),(113,'stevechin83@gmail.com',898314,'2022-06-20'),(114,'stevechin83@gmail.com',762768,'2022-06-20'),(115,'stevechin83@gmail.com',219929,'2022-06-20'),(116,'stevechin83@gmail.com',469275,'2022-06-20'),(117,'stevechin83@gmail.com',107647,'2022-06-20'),(118,'stevechin83@gmail.com',442604,'2022-06-20'),(119,'stevechin83@gmail.com',42831,'2022-06-20'),(120,'Stevechin83@gmail.com',137098,'2022-06-21'),(121,'stevechin83@gmail.com',4583,'2022-06-21'),(122,'stevechin83@gmail.com',626969,'2022-06-21'),(123,'stevechin83@gmail.com',279526,'2022-06-22'),(124,'Stevechin83@gmail.com',530580,'2022-06-22'),(125,'stevechin83@gmail.com',823288,'2022-06-27'),(126,'stevechin83@gmail.com',571774,'2022-06-28'),(127,'stevechin83@gmail.com',355076,'2022-06-28'),(128,'stevechin83@gmail.com',111198,'2022-07-03'),(129,'stevechin83@gmail.com',948258,'2022-07-08'),(130,'stevechin83@gmail.com',280685,'2022-07-08');
/*!40000 ALTER TABLE `tbl_otp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_post`
--

DROP TABLE IF EXISTS `tbl_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_post` (
  `postId` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(5000) NOT NULL,
  `file` varchar(500) NOT NULL,
  `image` varchar(500) NOT NULL,
  `approval` int(11) NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  `status` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  PRIMARY KEY (`postId`),
  KEY `userId` (`userId`),
  CONSTRAINT `tbl_post_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `tbl_user` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_post`
--

LOCK TABLES `tbl_post` WRITE;
/*!40000 ALTER TABLE `tbl_post` DISABLE KEYS */;
INSERT INTO `tbl_post` VALUES (1,'I love Pirates Movie','','',1,'2022-06-13 17:38:49','2022-06-29 07:39:17',1,13),(2,'Lets join badminton club','okok','no image',1,'2022-06-14 00:16:00','2022-06-14 00:16:00',1,1),(3,'I love INTI','f','i',1,'2022-06-17 16:06:00','2022-06-22 06:07:29',1,1),(4,'Today is good day','','',1,'2022-06-22 01:21:33','2022-06-27 12:44:44',0,1),(5,'ewqrrwqer\n','','',1,'2022-06-22 01:28:28','2022-06-22 06:09:51',0,1),(6,'INTIcredibles Mobile App is on fire','','',1,'2022-06-22 01:29:38','2022-07-03 08:43:21',0,1),(7,'Welcome to Inti!','','',1,'2022-06-22 06:06:04','2022-06-27 12:24:36',0,1),(8,'Hello\n','','',1,'2022-06-22 08:03:11','2022-06-28 05:47:55',0,19);
/*!40000 ALTER TABLE `tbl_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_status`
--

DROP TABLE IF EXISTS `tbl_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_status` (
  `statusId` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`statusId`),
  UNIQUE KEY `description` (`description`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_status`
--

LOCK TABLES `tbl_status` WRITE;
/*!40000 ALTER TABLE `tbl_status` DISABLE KEYS */;
INSERT INTO `tbl_status` VALUES (1,'active'),(0,'inactive');
/*!40000 ALTER TABLE `tbl_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `alumniId` int(11) DEFAULT NULL,
  `activationStatus` int(2) DEFAULT NULL,
  `GUID` varchar(255) DEFAULT NULL,
  `userRoleId` int(11) NOT NULL,
  `profilePicture` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `username` (`username`),
  KEY `alumniId` (`alumniId`),
  KEY `userRoleId` (`userRoleId`),
  CONSTRAINT `tbl_user_ibfk_1` FOREIGN KEY (`alumniId`) REFERENCES `tbl_alumni` (`alumniId`),
  CONSTRAINT `tbl_user_ibfk_2` FOREIGN KEY (`userRoleId`) REFERENCES `tbl_user_role` (`userRoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` VALUES (1,'I18014685','93878b51fd2aa308d82d7e4336ee4e63',1,30,'fecae7c7-3e59-4b0f-af22-517bb92cd80d',1,NULL),(7,'J180141111','ce274ef781289cde0ab7e8fd48ae3291',3,20,'ae1a97bf-4e14-4f45-80d9-7d728cf04606',1,NULL),(8,'J180142222','3a054defbb312ade5be2f911d19ca16a',4,30,'c2190ad5-d0fc-4298-a97b-6fce4fa94b0a',1,NULL),(9,'J9876543210','2d968226d46fe5bf9388291d6c42fa4f',6,30,'e8a2a05e-cc74-4246-83d0-7e97186c000a',1,NULL),(10,'J20020200','93878b51fd2aa308d82d7e4336ee4e63',9,30,'b9f15a0d-3039-4c64-b6d0-443772f9d5db',2,NULL),(11,'J20022200','testing',11,30,'1ad7e33c-8ee4-4545-8565-d917de34925b',1,NULL),(12,'J20023200','93878b51fd2aa308d82d7e4336ee4e63',12,30,'a42a696b-b2fb-45ee-ac44-41396829c314',1,NULL),(13,'firstlogin','7edd2495a82af766fcfd0a088ea973a7',15,30,'6ff64a29-7df5-4719-9726-e6263799905d',1,NULL),(19,'J20088123','93878b51fd2aa308d82d7e4336ee4e63',20,30,'479b572f-d942-42bd-9a4f-abc4daac0458',1,'https://chilamlol.pythonanywhere.com/static/19_Profile_20220622061940.jpg'),(20,'I180141234','a6b1e4788a36344a851b7743e38e5bca',21,20,'fe370548-d5e7-476b-98b9-1ef889fdd659',1,NULL),(21,'ok','ko',NULL,30,'41036357-eb42-4aa3-96b0-eb0956823242',3,NULL),(22,'I18014666','93878b51fd2aa308d82d7e4336ee4e63',22,30,'f60f9faf-04af-4404-9634-015dfe3c4fbf',1,''),(23,'admin1','93878b51fd2aa308d82d7e4336ee4e63',NULL,30,'4b62458a-fc20-4c4f-9652-ee4e81c4ed20',3,NULL),(24,'admin2','d41d8cd98f00b204e9800998ecf8427e',NULL,30,'eee65565-2bd8-422e-b1f3-ad19ab88c394',3,NULL),(25,'admin123','d41d8cd98f00b204e9800998ecf8427e',NULL,30,'cc559c5a-5e94-453a-bd84-5b1f84503bf7',3,NULL),(26,'newadmin','d41d8cd98f00b204e9800998ecf8427e',NULL,30,'4838123c-853d-439f-a54f-6e691616ee80',3,NULL),(27,'adminApiApi','admintest',NULL,30,'5a9800a5-2276-466e-9db1-91abc2555ab5',3,NULL),(29,'Apiadmin','freshnewpass',NULL,30,'f12f7ebd-65ed-4c49-b5de-3e2da24eddaf',3,NULL);
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_role`
--

DROP TABLE IF EXISTS `tbl_user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_role` (
  `userRoleId` int(11) NOT NULL AUTO_INCREMENT,
  `role` varchar(30) NOT NULL,
  PRIMARY KEY (`userRoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_role`
--

LOCK TABLES `tbl_user_role` WRITE;
/*!40000 ALTER TABLE `tbl_user_role` DISABLE KEYS */;
INSERT INTO `tbl_user_role` VALUES (1,'alumni'),(2,'superAdmin'),(3,'admin');
/*!40000 ALTER TABLE `tbl_user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_voucher`
--

DROP TABLE IF EXISTS `tbl_user_voucher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_voucher` (
  `userVoucherId` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) NOT NULL,
  `voucherId` int(11) NOT NULL,
  `redeemable` int(11) NOT NULL COMMENT '0 = false, cant redeem. 1 = true, still can redeem',
  `barcode` varchar(50) NOT NULL,
  `expiryDate` datetime NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime DEFAULT NULL,
  PRIMARY KEY (`userVoucherId`),
  KEY `userId` (`userId`),
  KEY `voucherId` (`voucherId`),
  CONSTRAINT `tbl_user_voucher_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `tbl_user` (`userId`),
  CONSTRAINT `tbl_user_voucher_ibfk_2` FOREIGN KEY (`voucherId`) REFERENCES `tbl_voucher` (`voucherId`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_voucher`
--

LOCK TABLES `tbl_user_voucher` WRITE;
/*!40000 ALTER TABLE `tbl_user_voucher` DISABLE KEYS */;
INSERT INTO `tbl_user_voucher` VALUES (31,1,5,1,'KR1000','2022-07-01 00:00:00','2022-06-27 13:27:48',NULL),(32,1,5,1,'KR1001','2022-07-01 00:00:00','2022-06-27 13:27:55',NULL),(33,1,5,1,'KR1002','2022-07-01 00:00:00','2022-06-27 13:28:00',NULL),(34,19,4,0,'SB1000','2023-06-28 00:00:00','2022-06-28 06:10:19','2022-06-28 07:51:43'),(35,19,4,1,'SB1001','2022-06-29 00:00:00','2022-06-29 05:41:14',NULL),(36,19,4,1,'SB1002','2022-06-29 00:00:00','2022-06-29 05:41:38',NULL),(37,19,4,1,'SB1003','2022-06-29 00:00:00','2022-06-29 05:49:02',NULL),(38,19,4,1,'SB1004','2022-06-29 00:00:00','2022-06-29 06:19:35',NULL),(39,19,4,1,'SB1005','2022-06-29 00:00:00','2022-06-29 06:20:00',NULL),(40,19,4,1,'SB1006','2022-06-29 00:00:00','2022-06-29 06:20:05',NULL),(41,19,4,1,'SB1007','2022-06-29 00:00:00','2022-06-29 08:26:13',NULL),(42,19,4,1,'SB1008','2022-06-29 00:00:00','2022-06-29 08:27:07',NULL),(43,19,4,1,'SB1009','2022-06-29 00:00:00','2022-06-29 08:27:08',NULL),(44,19,4,1,'SB1010','2022-06-29 00:00:00','2022-06-29 08:27:08',NULL),(45,19,4,1,'SB1011','2022-06-29 00:00:00','2022-06-29 08:27:08',NULL),(46,19,4,1,'SB1012','2022-06-29 00:00:00','2022-06-29 08:28:09',NULL),(47,19,4,1,'SB1012','2022-06-29 00:00:00','2022-06-29 08:28:09',NULL),(48,19,4,1,'SB1014','2022-06-29 00:00:00','2022-06-29 08:28:10',NULL),(49,19,4,1,'SB1015','2022-06-29 00:00:00','2022-06-29 08:28:10',NULL),(50,19,4,1,'SB1016','2022-06-29 00:00:00','2022-06-29 08:29:03',NULL),(51,19,4,1,'SB1017','2022-06-29 00:00:00','2022-06-29 08:29:59',NULL),(52,19,4,1,'SB1018','2022-06-29 00:00:00','2022-06-29 09:19:35',NULL),(53,19,4,1,'SB1019','2027-11-24 00:00:00','2022-07-03 12:50:39',NULL);
/*!40000 ALTER TABLE `tbl_user_voucher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_voucher`
--

DROP TABLE IF EXISTS `tbl_voucher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_voucher` (
  `voucherId` int(11) NOT NULL AUTO_INCREMENT,
  `merchantId` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `image` varchar(150) NOT NULL,
  `expiryType` int(1) NOT NULL COMMENT 'if 1 = specific date, 2= expiry days',
  `expiryDate` datetime DEFAULT NULL,
  `expiryDay` int(11) DEFAULT NULL,
  `voucherClaimableAmount` int(11) NOT NULL,
  `voucherLimit` int(11) NOT NULL,
  `startDate` datetime NOT NULL,
  `endDate` datetime NOT NULL,
  `createdDate` datetime NOT NULL,
  `modifiedDate` datetime NOT NULL,
  `status` int(11) NOT NULL,
  PRIMARY KEY (`voucherId`),
  KEY `merchantId` (`merchantId`),
  CONSTRAINT `tbl_voucher_ibfk_1` FOREIGN KEY (`merchantId`) REFERENCES `tbl_merchant` (`merchantId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_voucher`
--

LOCK TABLES `tbl_voucher` WRITE;
/*!40000 ALTER TABLE `tbl_voucher` DISABLE KEYS */;
INSERT INTO `tbl_voucher` VALUES (1,1,'STB','RM20 off on all beverage','INTI is the best','no image',1,'2022-06-17 12:41:55',0,3,200,'2022-06-17 12:41:55','2022-06-30 18:41:56','2022-06-17 12:41:55','2022-06-17 12:41:55',0),(2,1,'STB','RM20 off on all beverage','INTI is the best','no image',1,'2022-06-17 12:41:55',0,3,5000,'2022-06-17 12:41:55','2022-06-30 18:41:56','2022-06-17 12:41:55','2022-06-17 12:41:55',0),(3,1,'test','test','testtest','test',1,'2022-06-17 15:16:42',NULL,3,500,'2022-06-17 15:16:42','2022-06-17 15:16:42','2022-06-17 15:16:42','2022-06-17 15:16:42',1),(4,1,'SB1','Get FREE Frappuccino','ABOUT THE PRODUCT\n\n1)You will receieve 1 voucher for 1 FREE Frappuccino Blended Beverage (Mocha/Expresso/Caramel).\n2)Valid for Tall size(12oz) Frappuccino Blended Beverage (Mocha/Expresso/Caramel).','https://chilamlol.pythonanywhere.com/static/1_Profile_20220622044414.jpg',2,'1970-11-30 16:57:00',1970,20,500,'2022-06-17 16:47:15','2022-08-01 12:00:00','2022-06-21 20:46:16','2022-07-03 12:49:38',1),(5,2,'KR1','50% OFF for 2nd RED Hot Meal & Fizzy Rose with purchase of the same item at normal price!','50% OFF for 2nd RED Hot Meal & Fizzy Rose with purchase of the same item at normal price!','https://chilamlol.pythonanywhere.com/static/1_Profile_20220622045358.jpg',1,'2022-07-01 00:00:00',2022,3,100,'2022-06-17 16:47:15','2022-08-28 12:00:00','2022-06-21 20:55:29','2022-06-21 20:55:29',1);
/*!40000 ALTER TABLE `tbl_voucher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-08  8:31:24
