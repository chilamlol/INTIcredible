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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_alumni`
--

LOCK TABLES `tbl_alumni` WRITE;
/*!40000 ALTER TABLE `tbl_alumni` DISABLE KEYS */;
INSERT INTO `tbl_alumni` VALUES (1,'Chin Thiam Fatt','000308141505','I18014685','stevechin83@gmail.com','60128388813','60128388813','IU','2019','DITN','Diploma in IT','diploma'),(3,'Syakirah Noorizam','A1273845','J180141111','test@com.com','911','911','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(4,'Larry King','991221141234','J180142222','guanhong2@gmail.com','60123456789','60123456789','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(5,'Hugh Jackman','721212121212','J180143333','Jackman@gmail.com','0123456789','60123456789','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(6,'Beff Jezos','001122345678','J9876543210','guanhong2@gmail.com','60123456789','60123456789','IICS','2022','DITN','Diploma in IT','diploma'),(7,'steady','123456121234','J123456789','syakirah.noorizam@newinti.edu.my','0123853230','0123853230','iics','2022','CSIT','Computer Science','Degree'),(9,'Thiam Fatt CHIN','991212141212','J20020200','stevechin83@gmail.com','0128388813','0128388813','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(11,'Chin Thiam Fatt','991212151212','J20022200','stevechin83@gmail.com','60128388813','60128388813','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(12,'Chin Thiam Fatt','991212141212','J20023200','stevechin83@gmail.com','60128388813','0128388813','IICS','2019','Diploma In IT','Diploma In IT','diploma'),(13,'a','a','a','a','11111111111,,,','1234567890','a','a','a','e','diploma'),(15,'firstlogin','000000100000','firstlogin','kokhau000904@gmail.com','0122172333','123456789-','iics','2022','csit','computer science','degree'),(16,'Chin Thiam Fatt','000308141234','J20033757','stevechin83@gmail.com','0128388813','0128388813','IICS','2022','CADP','Computer Science','degree'),(17,'','','','a','a','','','','','',''),(19,'She Kok Hau','000904100857','J18026324','kokhau000904@gmail.com','60122172333','','IICS','2022','CAPD','Software Engineering and Digital Security','degree');
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
  `status` int(1) NOT NULL,
  PRIMARY KEY (`eventId`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_event`
--

LOCK TABLES `tbl_event` WRITE;
/*!40000 ALTER TABLE `tbl_event` DISABLE KEYS */;
INSERT INTO `tbl_event` VALUES (9,'test','test','https://i.imgur.com/F8gZHLt.jpg','test','2022-04-06 15:00:00','2022-04-22 16:00:00',1),(12,'test5','test5','https://chilamlol.pythonanywhere.com/static/a.jpg','www.google.com','2022-04-05 15:00:00','2022-04-05 19:00:00',1),(13,'Network your Way up Digitally','NETWORK is your NETWORTH,\nWe are proud to have our special guest speaker Mr. Marcus Teoh, an INTI Alumnus from the Class of 2000, Bestselling Author, and an International Speaker to do his sharing with the alumni. He will be delivering an interesting and important topic, “Network your Way up Digitally”. Do not miss the chance to listen to his sharing and gain insightful knowledge through this session. You will also have the chance to network and exchange ideas with other participants during the networking session. See you at the event!','https://i.imgur.com/gDUewqY.jpg','https://tinyurl.com/intinetworking','2022-04-22 12:10:00','2022-04-23 13:10:00',1),(14,'Alumni Sharing Knowledge Session','Dear Alumni, \nWe are 2 days away from our Alumni Sharing Knowledge Session!\nJoin us in the first Alumni Sharing Knowledge Session in 2022 and this round, we are lucky to have our three alumni, Nur Zulaikha (currently working in Ezrilaw Firm), @⁨Mun Hong Teoh⁩ (currently working in Microsoft Malaysia) and Mohnish Patel (currently working in PWC) as the speakers for the session with the title “Expectations & Challenges From Your First Jobs.”','https://i.imgur.com/HoKVmH5.jpg','https://tinyurl.com/ASK2022','2022-07-04 00:00:00','2022-04-22 00:00:00',1),(20,'test','testing update','','a','2022-04-18 12:15:34','2022-04-18 18:45:34',0),(23,'Test 2','wefwefwefwe','https://i.imgur.com/j6wH6CD.jpg','www.google.com','2022-05-04 11:40:33','2022-05-04 12:40:33',1),(24,'Sea The Change','CSR event ','https://i.imgur.com/Oa4MfMq.jpg','https://docs.google.com/forms/d/1QJcgBsYhvwz-Ygpg80Hrja6xXPHM4CdrIpkP0zFXg1c/edit#responses','2022-06-29 07:45:00','2022-06-29 11:30:00',1);
/*!40000 ALTER TABLE `tbl_event` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_otp`
--

LOCK TABLES `tbl_otp` WRITE;
/*!40000 ALTER TABLE `tbl_otp` DISABLE KEYS */;
INSERT INTO `tbl_otp` VALUES (1,'chilamlol@hotmail.com',990687,'2021-12-16'),(2,'chilamlol@hotmail.com',599674,'2021-12-16'),(3,'stevechin83@gmail.com',726511,'2021-12-23'),(4,'stevechin83@gmail.com',656028,'2021-12-28'),(5,'stevechin83@gmail.com',458820,'2021-12-28'),(6,'stevechin83@gmail.com',676158,'2021-12-28'),(7,'stevechin83@gmail.com',52380,'2021-12-28'),(8,'stevechin83@gmail.com',25866,'2021-12-28'),(9,'stevechin83@gmail.com',473122,'2021-12-28'),(10,'stevechin83@gmail.com',578308,'2021-12-28'),(11,'stevechin83@gmail.com',224815,'2021-12-28'),(12,'stevechin83@gmail.com',931941,'2021-12-28'),(13,'stevechin83@gmail.com',76204,'2021-12-28'),(14,'stevechin83@gmail.com',845374,'2021-12-28'),(15,'stevechin83@gmail.com',923442,'2021-12-28'),(16,'stevechin83@gmail.com',629123,'2021-12-28'),(17,'stevechin83@gmail.com',901252,'2021-12-28'),(18,'larry@gmail.com',22803,'2021-12-30'),(19,'guanhong2@gmail.com',124434,'2021-12-30'),(20,'beff@jezos.com',521256,'2021-12-30'),(21,'guanhong2@gmail.com',681213,'2021-12-30'),(22,'syakirah.noorizam@newinti.edu.my',288634,'2022-01-03'),(23,'kokhau000904@gmail.com',489950,'2022-01-22'),(24,'kokhau000904@gmail.com',939545,'2022-03-15'),(25,'kokhau000904@gmail.com',581572,'2022-03-15'),(26,'kokhau000904@gmail.com',744943,'2022-03-15'),(27,'kokhau000904@gmail.com',759911,'2022-03-15'),(28,'stevechin83@gmail.com',312901,'2022-03-24'),(29,'kokhau000904@gmail.com',696905,'2022-03-24'),(30,'kokhau000904@gmail.com',780172,'2022-03-24'),(31,'stevechin83@gmail.com',767390,'2022-04-08'),(32,'stevechin83@gmail.com',773819,'2022-04-08'),(33,'stevechin83@gmail.com',775024,'2022-04-08'),(34,'stevechin83@gmail.com',222719,'2022-04-08'),(35,'stevechin83@gmail.com',38467,'2022-04-08'),(36,'stevechin83@gmail.com',881974,'2022-04-15'),(37,'stevechin83@gmail.com',653759,'2022-04-27'),(38,'syakirah.noorizam@newinti.edu.my',566979,'2022-04-29'),(39,'hugochin0803@gmail.com',597239,'2022-05-17'),(40,'hugochin0803@gmail.com',439867,'2022-05-17'),(41,'stevechin83@gmail.com',128377,'2022-05-17'),(42,'stevechin83@gmail.com',810724,'2022-05-17'),(43,'stevechin83@gmail.com',451378,'2022-05-17'),(44,'hugochin0803@gmail.com',438737,'2022-05-17'),(45,'stevechin83@gmail.com',870381,'2022-05-18'),(46,'stevechin83@gmail.com',923155,'2022-05-18');
/*!40000 ALTER TABLE `tbl_otp` ENABLE KEYS */;
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
  `alumniId` int(11) NOT NULL,
  `activationStatus` int(2) DEFAULT NULL,
  `GUID` varchar(255) DEFAULT NULL,
  `userRoleId` int(11) NOT NULL,
  `profilePicture` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`userId`),
  KEY `alumniId` (`alumniId`),
  KEY `userRoleId` (`userRoleId`),
  CONSTRAINT `tbl_user_ibfk_1` FOREIGN KEY (`alumniId`) REFERENCES `tbl_alumni` (`alumniId`),
  CONSTRAINT `tbl_user_ibfk_2` FOREIGN KEY (`userRoleId`) REFERENCES `tbl_user_role` (`userRoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` VALUES (1,'I18014685','93878b51fd2aa308d82d7e4336ee4e63',1,30,'fecae7c7-3e59-4b0f-af22-517bb92cd80d',1,'https://chilamlol.pythonanywhere.com/static/1_Profile_20220607155356.jpg'),(7,'J180141111','ce274ef781289cde0ab7e8fd48ae3291',3,20,'ae1a97bf-4e14-4f45-80d9-7d728cf04606',1,NULL),(8,'J180142222','3a054defbb312ade5be2f911d19ca16a',4,30,'c2190ad5-d0fc-4298-a97b-6fce4fa94b0a',1,NULL),(9,'J9876543210','2d968226d46fe5bf9388291d6c42fa4f',6,30,'e8a2a05e-cc74-4246-83d0-7e97186c000a',1,NULL),(10,'J20020200','93878b51fd2aa308d82d7e4336ee4e63',9,30,'b9f15a0d-3039-4c64-b6d0-443772f9d5db',2,NULL),(11,'J20022200','testing',11,30,'1ad7e33c-8ee4-4545-8565-d917de34925b',1,NULL),(12,'J20023200','93878b51fd2aa308d82d7e4336ee4e63',12,30,'a42a696b-b2fb-45ee-ac44-41396829c314',1,NULL),(13,'firstlogin','7edd2495a82af766fcfd0a088ea973a7',15,30,'6ff64a29-7df5-4719-9726-e6263799905d',1,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_role`
--

LOCK TABLES `tbl_user_role` WRITE;
/*!40000 ALTER TABLE `tbl_user_role` DISABLE KEYS */;
INSERT INTO `tbl_user_role` VALUES (1,'alumni'),(2,'superAdmin');
/*!40000 ALTER TABLE `tbl_user_role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-11  7:17:41
