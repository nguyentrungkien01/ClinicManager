-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: clinicmanager
-- ------------------------------------------------------
-- Server version	8.0.27
-- create database ClinicManager;
use ClinicManager;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_model`
--

DROP TABLE IF EXISTS `account_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `account_model` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(40) NOT NULL,
  `avatar` text,
  `is_active` tinyint(1) DEFAULT NULL,
  `last_access` datetime DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`account_id`),
  UNIQUE KEY `username` (`username`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `account_model_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role_model` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_model`
--

LOCK TABLES `account_model` WRITE;
/*!40000 ALTER TABLE `account_model` DISABLE KEYS */;
INSERT INTO `account_model` VALUES (1,'username1','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',1),(2,'username2','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',2),(3,'username3','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',3),(4,'username4','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',3),(5,'thanhnam1','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',1),(6,'tester123','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',3),(7,'trucnhi16','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',2),(8,'haitrieu1','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',2),(9,'hoangnam3','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',3),(10,'nhokchibi','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',2),(11,'truclinh32','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',3),(12,'haihoang43','25d55ad283aa400af464c76d713c07ad',NULL,1,'2021-12-07 08:46:36',3),(13,'15570102741','7930791323dsadasd23easdasd4983',NULL,1,'2021-12-07 08:46:36',3),(14,'16570102852','7932dasdslkajfhjfdsfsdf279225',NULL,1,'2021-12-07 08:46:36',3),(15,'16570101483','7932279fsdfsdfdsfdsfdsfsdf34c243',NULL,1,'2021-12-07 08:46:36',3),(16,'16570103404','793226989cdsfgcgvsdg3',NULL,1,'2021-12-07 08:46:36',2),(17,'16550120335','772125ewfxffdgedgfregcx',NULL,1,'2021-12-07 08:46:36',3),(18,'16540200376','793228sgfdsgfdsgfdgfdgfd6761',NULL,1,'2021-12-07 08:46:36',3),(19,'16540400047','60204fdr3423454wrfewsfsdfg95173',NULL,1,'2021-12-07 08:46:36',3),(20,'16540403978','58200gfdgfd99080',NULL,1,'2021-12-07 08:46:36',2),(21,'16570500149','79322gfdgdfg83157',NULL,1,'2021-12-07 08:46:36',3),(22,'16570500111','79322gdfgdfgdfyt5erg6t83157',NULL,1,'2021-12-07 08:46:36',3),(23,'16530120028','123456624006839678',NULL,1,'2021-12-07 08:46:36',3),(24,'16510100830','12gregrgfds4532fgfdgfdg1678',NULL,1,'2021-12-07 08:46:36',3),(25,'17570100041','123regreg42135678',NULL,1,'2021-12-07 08:46:36',3),(26,'17570100058','121ergre2334521678',NULL,1,'2021-12-07 08:46:36',3),(27,'17570100260','12313rsg2345678',NULL,1,'2021-12-07 08:46:36',3),(28,'17570100176','123fsd21345678',NULL,1,'2021-12-07 08:46:36',3),(29,'17570101128','1233fh445678',NULL,1,'2021-12-07 08:46:36',2),(30,'20540325623','12dfghfsd345678',NULL,1,'2021-12-07 08:46:36',2),(31,'17570101183','12ln34nbvnn5h78',NULL,1,'2021-12-07 08:46:36',2),(32,'20570106706','123gcvbgf45678',NULL,1,'2021-12-07 08:46:36',2),(33,'20560512191','6721f124421',NULL,1,'2021-12-07 08:46:36',2),(34,'20510822079','143521fg82345678',NULL,1,'2021-12-07 08:46:36',2),(35,'20537050307','127683765678',NULL,1,'2021-12-07 08:46:36',2),(36,'20567051089','12768r3765678',NULL,1,'2021-12-07 08:46:36',2),(37,'25057058087','12768376435678',NULL,1,'2021-12-07 08:46:36',2),(38,'42057055087','12768g3765678',NULL,1,'2021-12-07 08:46:36',2),(39,'52057055088','127683765678',NULL,1,'2021-12-07 08:46:36',2),(40,'62057053084','1276ddffgdfg83765678',NULL,1,'2021-12-07 08:46:36',2);
/*!40000 ALTER TABLE `account_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_model`
--

DROP TABLE IF EXISTS `category_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `category_model` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_model`
--

LOCK TABLES `category_model` WRITE;
/*!40000 ALTER TABLE `category_model` DISABLE KEYS */;
INSERT INTO `category_model` VALUES (4,'Kho thuốc dạ dày'),(1,'Kho thuốc giảm đau, hạ sốt, kháng viêm'),(5,'Kho thuốc ho – long đờm'),(3,'Kho thuốc kháng histamin'),(2,'Kho thuốc kháng sinh');
/*!40000 ALTER TABLE `category_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_model`
--

DROP TABLE IF EXISTS `customer_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `customer_model` (
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `id_card` varchar(12) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL,
  `sex` enum('MALE','FEMALE') DEFAULT NULL,
  `customer_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `id_card` (`id_card`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_model`
--

LOCK TABLES `customer_model` WRITE;
/*!40000 ALTER TABLE `customer_model` DISABLE KEYS */;
INSERT INTO `customer_model` VALUES ('Thái Sơn','Hoàng','2021-12-07 00:00:00','01234567891','43/7 Cộng Hòa, P4, Quận Tân Bình','hanhmhoang@ptsc.com.vn','0938121979','MALE',1),('Tứ Xuyên','Trần','2021-12-07 00:00:00','01234567892','513/7B dien bien phu f3, q3','cuoithang3@yahoo.com','0908487452','MALE',2),('Thanh Tâm','Bùi','2021-12-07 00:00:00','01234567893','275/40z5 Bạch Đằng, P.15, Q. Bình Thạnh','tram.duong@mtgas.com.vn','0983866863','MALE',3),('Thanh Quang','Bùi','2021-12-07 00:00:00','01234567894','3-1b, Kp Mỹ An, Phú Mỹ Hưng, P. Tân Phong, Q7','hienlq@evsc.com.vn','0983091207','MALE',4),('Hồng Tiên','Nguyễn','2021-12-07 00:00:00','01234567895','Kí ốt 1, CT2B, KĐT mới Văn Quán, Phúc La, Hà Đông','ngocdiep.bach@jti.com','0985962425','FEMALE',5),('Thị Hiền','Nguyễn','2021-12-07 00:00:00','01234567896','A19/2, Ngo Tat To, P22, Binh Thanh','kieu_phuong@via.com.vn','0913887846','FEMALE',6),('Văn Duy','Hà','2021-12-07 00:00:00','01234567897','tổ 14, phường Quyết Thắng, thành phố Sơn La.','mylan@thanglongsc.com.vn','0904864762','MALE',7),('Văn Tố','Trần','2021-12-07 00:00:00','01234567898','54-56 Nguyễn Trãi, Quận 1','thaihang_le@hotmail.com','0904864762','MALE',8),('Chí Thiện','Nguyễn','2021-12-07 00:00:00','012345678991','207 lo A cc hà kiều, P5, Go Vap','thuyducnguyen@ptsc.com.vn','0854463753','MALE',9),('Hoàng Châu','Lê','2021-12-07 00:00:00','01234567819','49 Quốc Tử Giám, Đống Đa','le.huong@capitaland.com','0983216960','FEMALE',10),('Hoàng Mai','Nguyễn','2021-12-07 00:00:00','01234567829','5B Ton Duc Thang quan 1','xuanhuong@cdmvietnam.com','0913317577','MALE',11),('Tuấn Anh','Bùi','2021-12-07 00:00:00','01234567839','111 D5, phường 25, Bình Thạnh','trihuy@Ccgroupasian.com.vn','0903707410','FEMALE',12),('Bình Giang','Đỗ','2021-12-07 00:00:00','01234567849','120Hàng Trống, Hoàn Kiếm','p.v.nhat@china-airlines.com','0913353006','MALE',13),('Thanh Hải','Lê','2021-12-07 00:00:00','01234567859','35 Đường T4A, P.Tây Thạnh, Q.Tân Phú','tammi@dimen.sgionsedu.vn','0947137555','MALE',14),('Hữu Đỉnh','Lê','2021-12-07 00:00:00','01234567869','51/1 Phạm Văn Chiêu, phường 9, quận Gò Vấp','dshcm@dsavocats.com.vn','0439344625','MALE',15),('Ngọc Hải','Lê','2021-12-07 00:00:00','01234567879','Phòng 68, 171 Cao Thắng (nd), P.12, Q.10','thanhthuy_nguyen@gfkasia.com','0902398669','FEMALE',16),('Thanh Hà','Nguyễn','2021-12-07 00:00:00','012345678896','48 tăng bạt hổ - Hai bà Trưng','kauko.vn@hcm.fpt.vn','0838367618','MALE',17),('Hoàng Thiện','Võ','2021-12-07 00:00:00','01234567899','17  Ấp Bắc, P4, TP Mỹ Tho','kolon@vnn.vn','0919254582','MALE',18),('Thanh Tùng','Vương','2021-12-07 00:00:00','01234567189','92/29 Tập Đoàn 6B Phường Tân Tạo A, Quận Bình Tân','hong@kanematsu.vnn.vn','0903014016','MALE',19),('Tứ Long','Trần','2021-12-07 00:00:00','01234567289','513/1B dien bien phu f3, q3','cuoithang3@yahoo.com','0918487452','MALE',20),('Thanh Thanh','Bùi','2021-12-07 00:00:00','01234567389','271/40z5 Bạch Đằng, P.15, Q. Bình Thạnh','tram.duong@mtgas.com.vn','0983866863','MALE',21),('Thanh Quảng','Bùi','2021-12-07 00:00:00','01234567489','3-2b, Kp Mỹ An, Phú Mỹ Hưng, P. Tân Phong, Q7','hienlq@evsc.com.vn','0983091207','MALE',22),('Hồng Thuỷ','Nguyễn','2021-12-07 00:00:00','01234567589','Kí ốt 13, CT2B, KĐT mới Văn Quán, Phúc La, Hà Đông','ngocdiep.bach@jti.com','0985962425','FEMALE',23),('Thị Hiền','Nguyễn','2021-12-07 00:00:00','01234567689','A19/2, Ngo Tat To, P22, Binh Thanh','kieu_phuong@via.com.vn','0913887846','FEMALE',24),('Văn Đồng','Hà','2021-12-07 00:00:00','012345677893','tổ 1, phường Quyết Thắng, thành phố Sơn La.','mylan@thanglongsc.com.vn','0904864762','MALE',25),('Văn Thanh','Trần','2021-12-07 00:00:00','01234567889','Lầu 12 tòa nhà Zen Plaza 54-56 Nguyễn Trãi, Quận 1','thaihang_le@hotmail.com','0904864762','MALE',26),('Chí Thanh','Nguyễn','2021-12-07 00:00:00','01234567989','27 lo A cc hà kiều, P5, Go Vap','thuyducnguyen@ptsc.com.vn','0854463753','MALE',27),('Hoàng Chinh','Lê','2021-12-07 00:00:00','01234561789','43 Quốc Tử Giám, Đống Đa','le.huong@capitaland.com','0983216960','FEMALE',28),('Hoàng Mạnh','Nguyễn','2021-12-07 00:00:00','01234562789','51B Ton Duc Thang quan 1','xuanhuong@cdmvietnam.com','0913317577','MALE',29),('Tuấn Minh','Bùi','2021-12-07 00:00:00','01234563789','11 D5, phường 25, Bình Thạnh','trihuy@Ccgroupasian.com.vn','0903707410','FEMALE',30),('Bình Giao','Đỗ','2021-12-07 00:00:00','01234564789','10 Hàng Trống, Hoàn Kiếm','p.v.nhat@china-airlines.com','0913353006','MALE',31),('Thanh Hưng','Lê','2021-12-07 00:00:00','01234565789','315 Đường T4A, P.Tây Thạnh, Q.Tân Phú','tammi@dimen.sgionsedu.vn','0947137555','MALE',32),('Hữu Đinh','Lê','2021-12-07 00:00:00','012345667890','1/1 Phạm Văn Chiêu, phường 9, quận Gò Vấp','dshcm@dsavocats.com.vn','0439344625','MALE',33),('Ngọc Long','Lê','2021-12-07 00:00:00','01234567789','Phòng 68, 71 Cao Thắng (nd), P.12, Q.10','thanhthuy_nguyen@gfkasia.com','0902398669','FEMALE',34),('Thanh Hưng','Nguyễn','2021-12-07 00:00:00','01234568789','8 tăng bạt hổ - Hai bà Trưng','kauko.vn@hcm.fpt.vn','0838367618','MALE',35),('Hoàng Thanh','Võ','2021-12-07 00:00:00','01234569789','171  Ấp Bắc, P4, TP Mỹ Tho','kolon@vnn.vn','0919254582','MALE',36),('Thanh Hà','Vương','2021-12-07 00:00:00','0123451789','2/29 Tập Đoàn 6B Phường Tân Tạo A, Quận Bình Tân','hong@kanematsu.vnn.vn','0903014016','MALE',37),('Tứ','Trần','2021-12-07 00:00:00','01234526789','5/7B dien bien phu f3, q3','cuoithang3@yahoo.com','0908487452','MALE',38),('Thiện Tâm','Bùi','2021-12-07 00:00:00','01234536789','275/5 Bạch Đằng, P.15, Q. Bình Thạnh','tram.duong@mtgas.com.vn','0983866863','MALE',39),('Quang','Bùi','2021-12-07 00:00:00','01234546789','3, Kp Mỹ An, Phú Mỹ Hưng, P. Tân Phong, Q7','hienlq@evsc.com.vn','0983091207','MALE',40),('Hồng','Nguyễn','2021-12-07 00:00:00','012345567891','CT2B, KĐT mới Văn Quán, Phúc La, Hà Đông','ngocdiep.bach@jti.com','0985962425','FEMALE',41),('Hiền','Nguyễn','2021-12-07 00:00:00','01234566789','Ngo Tat To, P22, Binh Thanh','kieu_phuong@via.com.vn','0913887846','FEMALE',42),('Duy','Hà','2021-12-07 00:00:00','01234576789','pphường Quyết Thắng, thành phố Sơn La.','mylan@thanglongsc.com.vn','0904864762','MALE',43),('Tố','Trần','2021-12-07 00:00:00','01234586789','54-56 Nguyễn Trãi, Quận 1','thaihang_le@hotmail.com','0904864762','MALE',44),('Thiện','Nguyễn','2021-12-07 00:00:00','01234596789','207, P5, Go Vap','thuyducnguyen@ptsc.com.vn','0854463753','MALE',45),('Hoàng','Lê','2021-12-07 00:00:00','01234156789','490 Quốc Tử Giám, Đống Đa','le.huong@capitaland.com','0983216960','FEMALE',46),('Hoàng','Nguyễn','2021-12-07 00:00:00','01234256789','Ton Duc Thang quan 1','xuanhuong@cdmvietnam.com','0913317577','MALE',47),('Tuấn','Bùi','2021-12-07 00:00:00','01234356789','111, phường 25, Bình Thạnh','trihuy@Ccgroupasian.com.vn','0903707410','FEMALE',48),('Giang','Đỗ','2021-12-07 00:00:00','012344567892','Hàng Trống, Hoàn Kiếm','p.v.nhat@china-airlines.com','0913353006','MALE',49),('Thanh','Lê','2021-12-07 00:00:00','01234556789','Đường T4A, P.Tây Thạnh, Q.Tân Phú','tammi@dimen.sgionsedu.vn','0947137555','MALE',50),('Hữu','Lê','2021-12-07 00:00:00','01234656789','Phạm Văn Chiêu, phường 9, quận Gò Vấp','dshcm@dsavocats.com.vn','0439344625','MALE',51),('Hải','Lê','2021-12-07 00:00:00','01234756789','171 Cao Thắng (nd), P.12, Q.10','thanhthuy_nguyen@gfkasia.com','0902398669','FEMALE',52),('Hà','Nguyễn','2021-12-07 00:00:00','01234856789','55 tăng bạt hổ - Hai bà Trưng','kauko.vn@hcm.fpt.vn','0838367618','MALE',53),('Thiện','Võ','2021-12-07 00:00:00','01234956789','Ấp Bắc, P4, TP Mỹ Tho','kolon@vnn.vn','0919254582','MALE',54),('Tùng','Vương','2021-12-07 00:00:00','012314567899','Tập Đoàn 6B Phường Tân Tạo A, Quận Bình Tân','hong@kanematsu.vnn.vn','0903014016','MALE',55);
/*!40000 ALTER TABLE `customer_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department_manager_detail_model`
--

DROP TABLE IF EXISTS `department_manager_detail_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `department_manager_detail_model` (
  `department_id` int NOT NULL,
  `manager_id` int NOT NULL,
  `joined_date` datetime DEFAULT NULL,
  `leaved_date` datetime DEFAULT NULL,
  PRIMARY KEY (`department_id`,`manager_id`),
  KEY `manager_id` (`manager_id`),
  CONSTRAINT `department_manager_detail_model_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department_model` (`department_id`),
  CONSTRAINT `department_manager_detail_model_ibfk_2` FOREIGN KEY (`manager_id`) REFERENCES `doctor_model` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department_manager_detail_model`
--

LOCK TABLES `department_manager_detail_model` WRITE;
/*!40000 ALTER TABLE `department_manager_detail_model` DISABLE KEYS */;
INSERT INTO `department_manager_detail_model` VALUES (1,1,'2021-12-06 22:19:42','2021-12-06 22:19:42'),(2,2,'2021-12-06 22:19:42','2021-12-06 22:19:42');
/*!40000 ALTER TABLE `department_manager_detail_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department_model`
--

DROP TABLE IF EXISTS `department_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `department_model` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `description` text,
  `logo` text,
  PRIMARY KEY (`department_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department_model`
--

LOCK TABLES `department_model` WRITE;
/*!40000 ALTER TABLE `department_model` DISABLE KEYS */;
INSERT INTO `department_model` VALUES (1,'Khoa Nội tổng hợp',10,NULL,NULL),(2,'Khoa Nội Tim mạch',15,NULL,NULL),(3,'Khoa Bệnh lây đường máu',20,NULL,NULL),(4,'Khoa Nội hô hấp',20,NULL,NULL),(5,'Khoa Hóa trị',15,NULL,NULL),(6,'Khoa Da liễu',10,NULL,NULL),(7,'Khoa Nhi',15,NULL,NULL),(8,'Khoa Dị ứng',10,NULL,NULL),(9,'Khoa Nội tiết',10,NULL,NULL),(10,'Khoa Quốc tế',10,NULL,NULL);
/*!40000 ALTER TABLE `department_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_model`
--

DROP TABLE IF EXISTS `doctor_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `doctor_model` (
  `staff_id` int NOT NULL,
  `major_id` int DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  KEY `major_id` (`major_id`),
  CONSTRAINT `doctor_model_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff_model` (`staff_id`),
  CONSTRAINT `doctor_model_ibfk_2` FOREIGN KEY (`major_id`) REFERENCES `major_model` (`major_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_model`
--

LOCK TABLES `doctor_model` WRITE;
/*!40000 ALTER TABLE `doctor_model` DISABLE KEYS */;
INSERT INTO `doctor_model` VALUES (1,1),(6,1),(11,1),(2,2),(7,2),(12,2),(3,3),(8,3),(13,3),(4,4),(9,4),(14,4),(5,5),(10,5),(15,5),(16,6),(17,6),(18,6),(19,6),(20,6);
/*!40000 ALTER TABLE `doctor_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document_model`
--

DROP TABLE IF EXISTS `document_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `document_model` (
  `document_id` int NOT NULL AUTO_INCREMENT,
  `date_created` datetime DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  PRIMARY KEY (`document_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `document_model_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_model` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=331 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document_model`
--

LOCK TABLES `document_model` WRITE;
/*!40000 ALTER TABLE `document_model` DISABLE KEYS */;
INSERT INTO `document_model` VALUES (1,'2021-01-01 00:00:00','medical_examination',1),(2,'2021-01-01 00:00:00','medical_bill',1),(3,'2021-01-02 00:00:00','medical_examination',2),(4,'2021-01-02 00:00:00','medical_bill',2),(5,'2021-01-03 00:00:00','medical_examination',3),(6,'2021-01-03 00:00:00','medical_bill',3),(7,'2021-01-04 00:00:00','medical_examination',4),(8,'2021-01-04 00:00:00','medical_bill',4),(9,'2021-01-05 00:00:00','medical_examination',5),(10,'2021-01-05 00:00:00','medical_bill',5),(11,'2021-01-06 00:00:00','medical_examination',6),(12,'2021-01-06 00:00:00','medical_bill',6),(13,'2021-01-07 00:00:00','medical_examination',7),(14,'2021-01-07 00:00:00','medical_bill',7),(15,'2021-01-08 00:00:00','medical_examination',8),(16,'2021-01-08 00:00:00','medical_bill',8),(17,'2021-01-09 00:00:00','medical_examination',9),(18,'2021-01-09 00:00:00','medical_bill',9),(19,'2021-01-10 00:00:00','medical_examination',10),(20,'2021-01-10 00:00:00','medical_bill',10),(21,'2021-02-11 00:00:00','medical_examination',11),(22,'2021-02-11 00:00:00','medical_bill',11),(23,'2021-02-12 00:00:00','medical_examination',12),(24,'2021-02-12 00:00:00','medical_bill',12),(25,'2021-02-13 00:00:00','medical_examination',13),(26,'2021-02-13 00:00:00','medical_bill',13),(27,'2021-02-14 00:00:00','medical_examination',14),(28,'2021-02-14 00:00:00','medical_bill',14),(29,'2021-02-15 00:00:00','medical_examination',15),(30,'2021-02-15 00:00:00','medical_bill',15),(31,'2021-02-16 00:00:00','medical_examination',16),(32,'2021-02-16 00:00:00','medical_bill',16),(33,'2021-02-17 00:00:00','medical_examination',17),(34,'2021-02-17 00:00:00','medical_bill',17),(35,'2021-02-18 00:00:00','medical_examination',18),(36,'2021-02-18 00:00:00','medical_bill',18),(37,'2021-02-19 00:00:00','medical_examination',19),(38,'2021-02-19 00:00:00','medical_bill',19),(39,'2021-02-20 00:00:00','medical_examination',20),(40,'2021-02-20 00:00:00','medical_bill',20),(41,'2021-03-21 00:00:00','medical_examination',21),(42,'2021-03-21 00:00:00','medical_bill',21),(43,'2021-03-22 00:00:00','medical_examination',22),(44,'2021-03-22 00:00:00','medical_bill',22),(45,'2021-03-23 00:00:00','medical_examination',23),(46,'2021-03-23 00:00:00','medical_bill',23),(47,'2021-03-24 00:00:00','medical_examination',24),(48,'2021-03-24 00:00:00','medical_bill',24),(49,'2021-03-25 00:00:00','medical_examination',25),(50,'2021-03-25 00:00:00','medical_bill',25),(51,'2021-03-26 00:00:00','medical_examination',26),(52,'2021-03-26 00:00:00','medical_bill',26),(53,'2021-03-27 00:00:00','medical_examination',27),(54,'2021-03-27 00:00:00','medical_bill',27),(55,'2021-03-28 00:00:00','medical_examination',28),(56,'2021-03-28 00:00:00','medical_bill',28),(57,'2021-03-29 00:00:00','medical_examination',29),(58,'2021-03-29 00:00:00','medical_bill',29),(59,'2021-03-30 00:00:00','medical_examination',30),(60,'2021-03-30 00:00:00','medical_bill',30),(61,'2021-04-01 00:00:00','medical_examination',31),(62,'2021-04-01 00:00:00','medical_bill',31),(63,'2021-04-02 00:00:00','medical_examination',32),(64,'2021-04-02 00:00:00','medical_bill',32),(65,'2021-04-03 00:00:00','medical_examination',33),(66,'2021-04-03 00:00:00','medical_bill',33),(67,'2021-04-04 00:00:00','medical_examination',34),(68,'2021-04-04 00:00:00','medical_bill',34),(69,'2021-04-05 00:00:00','medical_examination',35),(70,'2021-04-05 00:00:00','medical_bill',35),(71,'2021-04-06 00:00:00','medical_examination',36),(72,'2021-04-06 00:00:00','medical_bill',36),(73,'2021-04-07 00:00:00','medical_examination',37),(74,'2021-04-07 00:00:00','medical_bill',37),(75,'2021-04-08 00:00:00','medical_examination',38),(76,'2021-04-08 00:00:00','medical_bill',38),(77,'2021-04-09 00:00:00','medical_examination',39),(78,'2021-04-09 00:00:00','medical_bill',39),(79,'2021-04-10 00:00:00','medical_examination',40),(80,'2021-04-10 00:00:00','medical_bill',40),(81,'2021-05-11 00:00:00','medical_examination',41),(82,'2021-05-11 00:00:00','medical_bill',41),(83,'2021-05-12 00:00:00','medical_examination',42),(84,'2021-05-12 00:00:00','medical_bill',42),(85,'2021-05-13 00:00:00','medical_examination',43),(86,'2021-05-13 00:00:00','medical_bill',43),(87,'2021-05-14 00:00:00','medical_examination',44),(88,'2021-05-14 00:00:00','medical_bill',44),(89,'2021-05-15 00:00:00','medical_examination',45),(90,'2021-05-15 00:00:00','medical_bill',45),(91,'2021-05-16 00:00:00','medical_examination',46),(92,'2021-05-16 00:00:00','medical_bill',46),(93,'2021-05-17 00:00:00','medical_examination',47),(94,'2021-05-17 00:00:00','medical_bill',47),(95,'2021-05-18 00:00:00','medical_examination',48),(96,'2021-05-18 00:00:00','medical_bill',48),(97,'2021-05-19 00:00:00','medical_examination',49),(98,'2021-05-19 00:00:00','medical_bill',49),(99,'2021-05-20 00:00:00','medical_examination',50),(100,'2021-05-20 00:00:00','medical_bill',50),(101,'2021-06-01 00:00:00','medical_examination',51),(102,'2021-06-01 00:00:00','medical_bill',51),(103,'2021-06-02 00:00:00','medical_examination',52),(104,'2021-06-02 00:00:00','medical_bill',52),(105,'2021-06-03 00:00:00','medical_examination',53),(106,'2021-06-03 00:00:00','medical_bill',53),(107,'2021-06-04 00:00:00','medical_examination',54),(108,'2021-06-04 00:00:00','medical_bill',54),(109,'2021-06-05 00:00:00','medical_examination',1),(110,'2021-06-05 00:00:00','medical_bill',1),(111,'2021-06-06 00:00:00','medical_examination',2),(112,'2021-06-06 00:00:00','medical_bill',2),(113,'2021-06-07 00:00:00','medical_examination',3),(114,'2021-06-07 00:00:00','medical_bill',3),(115,'2021-06-08 00:00:00','medical_examination',4),(116,'2021-06-08 00:00:00','medical_bill',4),(117,'2021-06-09 00:00:00','medical_examination',5),(118,'2021-06-09 00:00:00','medical_bill',5),(119,'2021-06-10 00:00:00','medical_examination',6),(120,'2021-06-10 00:00:00','medical_bill',6),(121,'2021-07-11 00:00:00','medical_examination',7),(122,'2021-07-11 00:00:00','medical_bill',7),(123,'2021-07-12 00:00:00','medical_examination',8),(124,'2021-07-12 00:00:00','medical_bill',8),(125,'2021-07-13 00:00:00','medical_examination',9),(126,'2021-07-13 00:00:00','medical_bill',9),(127,'2021-07-14 00:00:00','medical_examination',10),(128,'2021-07-14 00:00:00','medical_bill',10),(129,'2021-07-15 00:00:00','medical_examination',11),(130,'2021-07-15 00:00:00','medical_bill',11),(131,'2021-07-16 00:00:00','medical_examination',12),(132,'2021-07-16 00:00:00','medical_bill',12),(133,'2021-07-17 00:00:00','medical_examination',13),(134,'2021-07-17 00:00:00','medical_bill',13),(135,'2021-07-18 00:00:00','medical_examination',14),(136,'2021-07-18 00:00:00','medical_bill',14),(137,'2021-07-19 00:00:00','medical_examination',15),(138,'2021-07-19 00:00:00','medical_bill',15),(139,'2021-07-20 00:00:00','medical_examination',16),(140,'2021-07-20 00:00:00','medical_bill',16),(141,'2021-07-21 00:00:00','medical_examination',17),(142,'2021-07-21 00:00:00','medical_bill',17),(143,'2021-08-01 00:00:00','medical_examination',18),(144,'2021-08-01 00:00:00','medical_bill',18),(145,'2021-08-02 00:00:00','medical_examination',6),(146,'2021-08-02 00:00:00','medical_bill',6),(147,'2021-08-03 00:00:00','medical_examination',7),(148,'2021-08-03 00:00:00','medical_bill',7),(149,'2021-08-04 00:00:00','medical_examination',8),(150,'2021-08-04 00:00:00','medical_bill',8),(151,'2021-08-05 00:00:00','medical_examination',9),(152,'2021-08-05 00:00:00','medical_bill',9),(153,'2021-08-06 00:00:00','medical_examination',10),(154,'2021-08-06 00:00:00','medical_bill',10),(155,'2021-08-07 00:00:00','medical_examination',11),(156,'2021-08-07 00:00:00','medical_bill',11),(157,'2021-08-08 00:00:00','medical_examination',12),(158,'2021-08-08 00:00:00','medical_bill',12),(159,'2021-08-09 00:00:00','medical_examination',13),(160,'2021-08-09 00:00:00','medical_bill',13),(161,'2021-08-10 00:00:00','medical_examination',14),(162,'2021-08-10 00:00:00','medical_bill',14),(163,'2021-09-11 00:00:00','medical_examination',15),(164,'2021-09-11 00:00:00','medical_bill',15),(165,'2021-09-12 00:00:00','medical_examination',16),(166,'2021-09-12 00:00:00','medical_bill',16),(167,'2021-09-13 00:00:00','medical_examination',17),(168,'2021-09-13 00:00:00','medical_bill',17),(169,'2021-09-14 00:00:00','medical_examination',18),(170,'2021-09-14 00:00:00','medical_bill',18),(171,'2021-09-15 00:00:00','medical_examination',19),(172,'2021-09-15 00:00:00','medical_bill',19),(173,'2021-09-16 00:00:00','medical_examination',20),(174,'2021-09-16 00:00:00','medical_bill',20),(175,'2021-09-17 00:00:00','medical_examination',21),(176,'2021-09-17 00:00:00','medical_bill',21),(177,'2021-09-18 00:00:00','medical_examination',22),(178,'2021-09-18 00:00:00','medical_bill',22),(179,'2021-09-19 00:00:00','medical_examination',23),(180,'2021-09-19 00:00:00','medical_bill',23),(181,'2021-09-20 00:00:00','medical_examination',24),(182,'2021-09-20 00:00:00','medical_bill',24),(183,'2021-10-01 00:00:00','medical_examination',25),(184,'2021-10-01 00:00:00','medical_bill',25),(185,'2021-10-02 00:00:00','medical_examination',26),(186,'2021-10-02 00:00:00','medical_bill',26),(187,'2021-10-03 00:00:00','medical_examination',27),(188,'2021-10-03 00:00:00','medical_bill',27),(189,'2021-10-04 00:00:00','medical_examination',28),(190,'2021-10-04 00:00:00','medical_bill',28),(191,'2021-10-05 00:00:00','medical_examination',29),(192,'2021-10-05 00:00:00','medical_bill',29),(193,'2021-10-06 00:00:00','medical_examination',30),(194,'2021-10-06 00:00:00','medical_bill',30),(195,'2021-10-07 00:00:00','medical_examination',31),(196,'2021-10-07 00:00:00','medical_bill',31),(197,'2021-10-08 00:00:00','medical_examination',32),(198,'2021-10-08 00:00:00','medical_bill',32),(199,'2021-10-09 00:00:00','medical_examination',33),(200,'2021-10-09 00:00:00','medical_bill',33),(201,'2021-10-10 00:00:00','medical_examination',34),(202,'2021-10-10 00:00:00','medical_bill',34),(203,'2021-11-11 00:00:00','medical_examination',35),(204,'2021-11-11 00:00:00','medical_bill',35),(205,'2021-11-12 00:00:00','medical_examination',36),(206,'2021-11-12 00:00:00','medical_bill',36),(207,'2021-11-13 00:00:00','medical_examination',37),(208,'2021-11-13 00:00:00','medical_bill',37),(209,'2021-11-14 00:00:00','medical_examination',38),(210,'2021-11-14 00:00:00','medical_bill',38),(211,'2021-11-15 00:00:00','medical_examination',39),(212,'2021-11-15 00:00:00','medical_bill',39),(213,'2021-11-16 00:00:00','medical_examination',40),(214,'2021-11-16 00:00:00','medical_bill',40),(215,'2021-11-17 00:00:00','medical_examination',41),(216,'2021-11-17 00:00:00','medical_bill',41),(217,'2021-11-18 00:00:00','medical_examination',42),(218,'2021-11-18 00:00:00','medical_bill',42),(219,'2021-11-19 00:00:00','medical_examination',43),(220,'2021-11-19 00:00:00','medical_bill',43),(221,'2021-11-20 00:00:00','medical_examination',44),(222,'2021-11-20 00:00:00','medical_bill',44),(223,'2021-12-01 00:00:00','medical_examination',45),(224,'2021-12-01 00:00:00','medical_bill',45),(225,'2021-12-02 00:00:00','medical_examination',46),(226,'2021-12-02 00:00:00','medical_bill',46),(227,'2021-12-03 00:00:00','medical_examination',47),(228,'2021-12-03 00:00:00','medical_bill',47),(229,'2021-12-04 00:00:00','medical_examination',48),(230,'2021-12-04 00:00:00','medical_bill',48),(231,'2021-12-05 00:00:00','medical_examination',49),(232,'2021-12-05 00:00:00','medical_bill',49),(233,'2021-12-06 00:00:00','medical_examination',50),(234,'2021-12-06 00:00:00','medical_bill',50),(235,'2021-12-07 00:00:00','medical_examination',51),(236,'2021-12-07 00:00:00','medical_bill',51),(237,'2021-12-08 00:00:00','medical_examination',52),(238,'2021-12-08 00:00:00','medical_bill',52),(239,'2021-12-09 00:00:00','medical_examination',53),(240,'2021-12-09 00:00:00','medical_bill',53),(241,'2021-12-10 00:00:00','medical_examination',54),(242,'2021-12-10 00:00:00','medical_bill',54),(243,'2022-01-01 00:00:00','medical_examination',20),(244,'2022-01-01 00:00:00','medical_bill',20),(245,'2022-01-01 00:00:00','medical_examination',37),(246,'2022-01-01 00:00:00','medical_bill',37),(247,'2022-01-01 00:00:00','medical_examination',45),(248,'2022-01-01 00:00:00','medical_bill',45),(249,'2022-01-02 00:00:00','medical_examination',19),(250,'2022-01-02 00:00:00','medical_bill',19),(251,'2022-01-03 00:00:00','medical_examination',54),(252,'2022-01-03 00:00:00','medical_bill',54),(253,'2022-01-03 00:00:00','medical_examination',6),(254,'2022-01-03 00:00:00','medical_bill',6),(255,'2022-01-03 00:00:00','medical_examination',2),(256,'2022-01-03 00:00:00','medical_bill',2),(257,'2022-01-05 00:00:00','medical_examination',17),(258,'2022-01-05 00:00:00','medical_bill',17),(259,'2022-01-06 00:00:00','medical_examination',31),(260,'2022-01-06 00:00:00','medical_bill',31),(261,'2022-01-06 00:00:00','medical_examination',22),(262,'2022-01-06 00:00:00','medical_bill',22),(263,'2022-01-06 00:00:00','medical_examination',14),(264,'2022-01-06 00:00:00','medical_bill',14),(265,'2022-01-06 00:00:00','medical_examination',25),(266,'2022-01-06 00:00:00','medical_bill',25),(267,'2022-01-06 00:00:00','medical_examination',49),(268,'2022-01-06 00:00:00','medical_bill',49),(269,'2022-01-08 00:00:00','medical_examination',54),(270,'2022-01-08 00:00:00','medical_bill',54),(271,'2022-01-08 00:00:00','medical_examination',33),(272,'2022-01-08 00:00:00','medical_bill',33),(273,'2022-01-09 00:00:00','medical_examination',51),(274,'2022-01-09 00:00:00','medical_bill',51),(275,'2022-01-09 00:00:00','medical_examination',52),(276,'2022-01-09 00:00:00','medical_bill',52),(277,'2022-01-10 00:00:00','medical_examination',37),(278,'2022-01-10 00:00:00','medical_bill',37),(279,'2022-01-10 00:00:00','medical_examination',3),(280,'2022-01-10 00:00:00','medical_bill',3),(281,'2022-01-10 00:00:00','medical_examination',9),(282,'2022-01-10 00:00:00','medical_bill',9),(283,'2022-01-10 00:00:00','medical_examination',11),(284,'2022-01-10 00:00:00','medical_bill',11),(285,'2022-01-11 00:00:00','medical_examination',17),(286,'2022-01-11 00:00:00','medical_bill',17),(287,'2022-01-11 00:00:00','medical_examination',22),(288,'2022-01-11 00:00:00','medical_bill',22),(289,'2022-01-11 00:00:00','medical_examination',34),(290,'2022-01-11 00:00:00','medical_bill',34),(291,'2022-01-11 00:00:00','medical_examination',35),(292,'2022-01-11 00:00:00','medical_bill',35),(293,'2022-01-11 00:00:00','medical_examination',36),(294,'2022-01-11 00:00:00','medical_bill',36),(295,'2022-01-11 00:00:00','medical_examination',37),(296,'2022-01-11 00:00:00','medical_bill',37),(297,'2022-01-12 00:00:00','medical_examination',38),(298,'2022-01-12 00:00:00','medical_bill',38),(299,'2022-01-12 00:00:00','medical_examination',39),(300,'2022-01-12 00:00:00','medical_bill',39),(301,'2022-01-13 00:00:00','medical_examination',40),(302,'2022-01-13 00:00:00','medical_bill',40),(303,'2022-01-13 00:00:00','medical_examination',41),(304,'2022-01-13 00:00:00','medical_bill',41),(305,'2022-01-13 00:00:00','medical_examination',42),(306,'2022-01-13 00:00:00','medical_bill',42),(307,'2022-01-13 00:00:00','medical_examination',43),(308,'2022-01-13 00:00:00','medical_bill',43),(309,'2022-01-15 00:00:00','medical_examination',44),(310,'2022-01-15 00:00:00','medical_bill',44),(311,'2022-01-17 00:00:00','medical_examination',46),(312,'2022-01-17 00:00:00','medical_bill',46),(313,'2022-01-17 00:00:00','medical_examination',47),(314,'2022-01-17 00:00:00','medical_bill',47),(315,'2022-01-17 00:00:00','medical_examination',51),(316,'2022-01-17 00:00:00','medical_bill',51),(317,'2022-01-18 00:00:00','medical_examination',45),(318,'2022-01-18 00:00:00','medical_bill',45),(319,'2022-01-18 00:00:00','medical_examination',52),(320,'2022-01-18 00:00:00','medical_bill',52),(321,'2022-01-19 00:00:00','medical_examination',48),(322,'2022-01-19 00:00:00','medical_bill',48),(323,'2022-01-19 00:00:00','medical_examination',53),(324,'2022-01-19 00:00:00','medical_bill',53),(325,'2022-01-19 00:00:00','medical_examination',49),(326,'2022-01-19 00:00:00','medical_bill',49),(327,'2022-01-19 00:00:00','medical_examination',50),(328,'2022-01-19 00:00:00','medical_bill',50),(329,'2022-01-19 00:00:00','medical_examination',54),(330,'2022-01-19 00:00:00','medical_bill',54);
/*!40000 ALTER TABLE `document_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_model`
--

DROP TABLE IF EXISTS `feedback_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `feedback_model` (
  `feedback_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(200) DEFAULT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `content` text,
  `gmail` varchar(50) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_model`
--

LOCK TABLES `feedback_model` WRITE;
/*!40000 ALTER TABLE `feedback_model` DISABLE KEYS */;
INSERT INTO `feedback_model` VALUES (1,'đánh giá dịch vụ','Nguyễn Thành Nam','dịch vụ phòng khám rất tốt','nam@gmail.com','2022-01-18 09:52:16',0),(2,'Đánh giá nhân viên','Đình Phong','nhân viên phục vụ tốt, thái độ hoà nhã','phong@gmai.com','2022-01-18 09:52:16',0),(3,'Đánh giá bác sỹ','Trung Kiên','Bác sỹ có chuyên môn cao, tư vấn tận tình','kien@gmail.com','2022-01-18 09:52:16',0);
/*!40000 ALTER TABLE `feedback_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `major_model`
--

DROP TABLE IF EXISTS `major_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `major_model` (
  `major_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`major_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `major_model`
--

LOCK TABLES `major_model` WRITE;
/*!40000 ALTER TABLE `major_model` DISABLE KEYS */;
INSERT INTO `major_model` VALUES (6,'Bệnh lây đường Tiêu hóa'),(4,'Da liễu'),(3,'Hồi sức tích cực'),(1,'Huyết học lâm sàng'),(2,'Nội Tim mạch'),(5,'Ung thư tổng hợp');
/*!40000 ALTER TABLE `major_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_bill_model`
--

DROP TABLE IF EXISTS `medical_bill_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `medical_bill_model` (
  `document_id` int NOT NULL,
  `medical_price` decimal(10,0) DEFAULT NULL,
  `medical_examination_price` decimal(10,0) DEFAULT NULL,
  `total_price` decimal(10,0) DEFAULT NULL,
  `nurse_id` int DEFAULT NULL,
  `medical_examination_id` int DEFAULT NULL,
  PRIMARY KEY (`document_id`),
  KEY `nurse_id` (`nurse_id`),
  KEY `medical_examination_id` (`medical_examination_id`),
  CONSTRAINT `medical_bill_model_ibfk_1` FOREIGN KEY (`document_id`) REFERENCES `document_model` (`document_id`),
  CONSTRAINT `medical_bill_model_ibfk_2` FOREIGN KEY (`nurse_id`) REFERENCES `nurse_model` (`staff_id`),
  CONSTRAINT `medical_bill_model_ibfk_3` FOREIGN KEY (`medical_examination_id`) REFERENCES `medical_examination_model` (`document_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_bill_model`
--

LOCK TABLES `medical_bill_model` WRITE;
/*!40000 ALTER TABLE `medical_bill_model` DISABLE KEYS */;
INSERT INTO `medical_bill_model` VALUES (2,30000,100000,130000,21,1),(4,40000,100000,140000,22,3),(6,67000,100000,167000,23,5),(8,43000,100000,143000,24,7),(10,32000,100000,132000,25,9),(12,59000,100000,159000,26,11),(14,71000,100000,171000,27,13),(16,35000,100000,135000,28,15),(18,24000,100000,124000,29,17),(20,100000,100000,200000,30,19),(22,32000,100000,132000,31,21),(24,46000,100000,146000,32,23),(26,130000,100000,230000,33,25),(28,42000,100000,142000,34,27),(30,80000,100000,180000,35,29),(32,98000,100000,198000,36,31),(34,77000,100000,177000,37,33),(36,26000,100000,126000,38,35),(38,127000,100000,227000,39,37),(40,135000,100000,235000,40,39),(42,169000,100000,269000,21,41),(44,136000,100000,236000,22,43),(46,165000,100000,265000,23,45),(48,89000,100000,189000,24,47),(50,320000,100000,420000,25,49),(52,140000,100000,240000,26,51),(54,89000,100000,189000,27,53),(56,68000,100000,168000,28,55),(58,71000,100000,171000,29,57),(60,92000,100000,192000,30,59),(62,165000,100000,265000,31,61),(64,210000,100000,310000,32,63),(66,35000,100000,135000,33,65),(68,58000,100000,158000,34,67),(70,71000,100000,171000,35,69),(72,96000,100000,196000,36,71),(74,85000,100000,185000,37,73),(76,73000,100000,173000,38,75),(78,64000,100000,164000,39,77),(80,59000,100000,159000,40,79),(82,45000,100000,145000,21,81),(84,93000,100000,193000,22,83),(86,103000,100000,203000,23,85),(88,180000,100000,280000,24,87),(90,146000,100000,246000,25,89),(92,120000,100000,220000,26,91),(94,119000,100000,219000,27,93),(96,136000,100000,236000,28,95),(98,170000,100000,270000,29,97),(100,40000,100000,140000,30,99),(102,30000,100000,130000,31,101),(104,45000,100000,145000,32,103),(106,33000,100000,133000,33,105),(108,47000,100000,147000,34,107),(110,59000,100000,159000,35,109),(112,61000,100000,161000,36,111),(114,38000,100000,138000,37,113),(116,44000,100000,144000,38,115),(118,92000,100000,192000,39,117),(120,153000,100000,253000,40,119),(122,31000,100000,131000,21,121),(124,46000,100000,146000,22,123),(126,39000,100000,139000,23,125),(128,47000,100000,147000,24,127),(130,135000,100000,235000,25,129),(132,141000,100000,241000,26,131),(134,197000,100000,297000,27,133),(136,236000,100000,336000,28,135),(138,211000,100000,311000,29,137),(140,126000,100000,226000,30,139),(142,133000,100000,233000,31,141),(144,25000,100000,125000,32,143),(146,230000,100000,330000,33,145),(148,91000,100000,191000,34,147),(150,58000,100000,158000,35,149),(152,72000,100000,172000,36,151),(154,77000,100000,177000,37,153),(156,81000,100000,181000,38,155),(158,56000,100000,156000,39,157),(160,36000,100000,136000,40,159),(162,48000,100000,148000,21,161),(164,93000,100000,193000,22,163),(166,48000,100000,148000,23,165),(168,120000,100000,220000,24,167),(170,180000,100000,280000,25,169),(172,36000,100000,136000,26,171),(174,84000,100000,184000,27,173),(176,49000,100000,149000,28,175),(178,52000,100000,152000,29,177),(180,95000,100000,195000,30,179),(182,130000,100000,230000,31,181),(184,210000,100000,310000,32,183),(186,113000,100000,230000,33,185),(188,65000,100000,165000,34,187),(190,89000,100000,189000,35,189),(192,31000,100000,131000,36,191),(194,47000,100000,147000,37,193),(196,29000,100000,129000,38,195),(198,134000,100000,234000,39,197),(200,66000,100000,166000,40,199),(202,49000,100000,149000,21,201),(204,32000,100000,132000,22,203),(206,44000,100000,144000,23,205),(208,39000,100000,139000,24,207),(210,47000,100000,147000,25,209),(212,35000,100000,135000,26,211),(214,140000,100000,240000,27,213),(216,12000,100000,112000,28,215),(218,42000,100000,142000,29,217),(220,38000,100000,138000,30,219),(222,46000,100000,146000,31,221),(224,39000,100000,139000,32,223),(226,41000,100000,141000,33,225),(228,130000,100000,230000,34,227),(230,189000,100000,289000,35,229),(232,216000,100000,316000,36,231),(234,44000,100000,144000,37,233),(236,39000,100000,139000,38,235),(238,43000,100000,143000,39,237),(240,37000,100000,137000,40,239),(242,42000,100000,142000,21,241),(244,61000,100000,161000,22,243),(246,85000,100000,185000,23,245),(248,66000,100000,166000,24,247),(250,75000,100000,175000,25,249),(252,290000,100000,390000,26,251),(254,180000,100000,280000,27,253),(256,46000,100000,146000,28,255),(258,89000,100000,189000,29,257),(260,91000,100000,191000,30,259),(262,75000,100000,175000,31,261),(264,62000,100000,162000,32,263),(266,42000,100000,142000,33,265),(268,44000,100000,144000,34,267),(270,66000,100000,166000,35,269),(272,55000,100000,155000,36,271),(274,75000,100000,175000,37,273),(276,42000,100000,142000,38,275),(278,90000,100000,190000,39,277),(280,138000,100000,238000,40,279),(282,69000,100000,169000,21,281),(284,46000,100000,146000,22,283),(286,22000,100000,122000,23,285),(288,56000,100000,156000,24,287),(290,96000,100000,196000,25,289),(292,36000,100000,136000,26,291),(294,125000,100000,225000,27,293),(296,60000,100000,160000,28,295),(298,89000,100000,1898000,29,297),(300,77000,100000,177000,30,299),(302,55000,100000,155000,31,301),(304,49000,100000,149000,32,303),(306,32000,100000,132000,33,305),(308,99000,100000,199000,34,307),(310,110000,100000,210000,35,309),(312,150000,100000,250000,36,311),(314,63000,100000,163000,37,313),(316,17000,100000,117000,38,315),(318,36000,100000,136000,39,317),(320,94000,100000,194000,40,319),(322,55000,100000,155000,21,321),(324,89000,100000,189000,22,323),(326,82000,100000,182000,23,325),(328,122000,100000,222000,24,327),(330,66000,100000,166000,25,329);
/*!40000 ALTER TABLE `medical_bill_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_examination_model`
--

DROP TABLE IF EXISTS `medical_examination_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `medical_examination_model` (
  `document_id` int NOT NULL,
  `symptom` text,
  `predicted_disease` text,
  `doctor_id` int DEFAULT NULL,
  PRIMARY KEY (`document_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `medical_examination_model_ibfk_1` FOREIGN KEY (`document_id`) REFERENCES `document_model` (`document_id`),
  CONSTRAINT `medical_examination_model_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctor_model` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_examination_model`
--

LOCK TABLES `medical_examination_model` WRITE;
/*!40000 ALTER TABLE `medical_examination_model` DISABLE KEYS */;
INSERT INTO `medical_examination_model` VALUES (1,'ho','covid19',1),(3,'sốt','covid19',1),(5,'đau đầu','covid19',1),(7,'chóng mặt','covid19',1),(9,'buồn nôn','covid19',1),(11,'Sổ mũi, chảy mũi, nghẹt mũi','covid19',1),(13,'Khó thở','covid19',1),(15,'đau ngực, tức ngực','covid19',1),(17,'đau người, đau cơ','covid19',1),(19,'mất vị giác','covid19',1),(21,'mất khứu giác','covid19',1),(23,'đau bụng','covid19',1),(25,'tiêu chảy','viêm mũi dị ứng',2),(27,'cảm lạnh','viêm mũi dị ứng',2),(29,'nghẹt mũi','viêm mũi dị ứng',2),(31,'sốt','sởi',3),(33,'ho khan','sởi',3),(35,'sổ mũi','sởi',3),(37,'ăn không ngon','sởi',3),(39,'chảy máu cam','sởi',3),(41,'đau họng','sởi',3),(43,'viêm kết mạc','sởi',3),(45,'đốm koplik trắng nhỏ','sởi',3),(47,'đau khớp dữ dội','gout',4),(49,'đau âm ĩ kéo dài','gout',4),(51,'viêm và tấy đỏ','gout',4),(53,'giới hạn phạm vi hoạt động khớp','gout',4),(55,'mệt mỏi','gan nhiễm mỡ',5),(57,'chán ăn','gan nhiễm mỡ',5),(59,'gan to','gan nhiễm mỡ',5),(61,'vàng da','gan nhiễm mỡ',5),(63,'vàng mắt','gan nhiễm mỡ',5),(65,'các sao mạch xuất hiện','gan nhiễm mỡ',5),(67,'lòng bàn tay son','gan nhiễm mỡ',5),(69,'cổ trướng','gan nhiễm mỡ',5),(71,'lách to','gan nhiễm mỡ',5),(73,'rối loạn giấc ngủ','gan',6),(75,'chán ăn','gan',6),(77,'khó tiêu','gan',6),(79,'buồn nôn','gan',6),(81,'thường xuyên mệt mỏi','gan',6),(83,'nước tiểu sẫm màu','gan',6),(85,'vàng da','gan',6),(87,'ngứa da','gan',6),(89,'đau bụng','gan',6),(91,'mất phương hướng, đãng trí','gan',6),(93,'Đau vùng rốn','giun sán',7),(95,'người bệnh gầy yếu','giun sán',7),(97,'có thể nôn và đi ngoài ra giun','giun sán',7),(99,'Đau bụng do nhiễm giun thường tái đi tái lại nhiều lần','giun sán',7),(101,'Người bị nhiễm giun kim thường bị ngứa ở vùng hậu môn về đêm','giun sán',7),(103,'Rối loạn tiêu hóa','giun sán',7),(105,'phân lúc đặc, lúc lỏng','giun sán',7),(107,'giun kim xuất hiện ở hậu môn hoặc trong phân','giun sán',7),(109,'Trẻ nhiễm giun thường biếng ăn, khó chịu, hay quấy khóc và khó ngủ về đêm','giun sán',7),(111,'Có biểu hiện thiếu hụt vitamin và khoáng chất','giun sán',7),(113,'có biểu hiện thiếu máu, thở khò khè hoặc ho khan','giun sán',7),(115,'xương bị biến dạng tại vị trí tổn thương','gãy xương',8),(117,'Xuất hiện vết bầm tím ở khu vực chấn thương','gãy xương',8),(119,'sưng và đau xung quanh vùng chấn thương','gãy xương',8),(121,'mất chức năng ở vùng bị thương','gãy xương',8),(123,'gãy xương hở, xương đâm xuyên qua và nhô ra khỏi da','gãy xương',8),(125,'rối loạn kinh nguyệt','tiền mãn kinh',9),(127,'khó thụ thai','tiền mãn kinh',9),(129,'bốc hỏa','tiền mãn kinh',9),(131,'thay đổi tính tình','tiền mãn kinh',9),(133,'dễ tăng cân','tiền mãn kinh',9),(135,'đau nhức','tiền mãn kinh',9),(137,'thay đổi mức cholesterol','tiền mãn kinh',9),(139,'khô âm đạo','tiền mãn kinh',9),(141,'mật độ xương giảm','tiền mãn kinh',9),(143,'rối loạn giấc ngủ','tiền mãn kinh',9),(145,'ra nhiều máu trong kỳ kinh nguyệt','tiền mãn kinh',9),(147,'suy giảm trí nhớ','tiền mãn kinh',9),(149,'Hoa mắt','máu nhiễm mỡ',10),(151,'chóng mặt','máu nhiễm mỡ',10),(153,'đau đầu','máu nhiễm mỡ',10),(155,'thở gấp','máu nhiễm mỡ',10),(157,'tim đập nhanh','máu nhiễm mỡ',10),(159,'đau tức ngực','máu nhiễm mỡ',10),(161,'Đau tim','máu nhiễm mỡ',10),(163,'huyết áp cao','máu nhiễm mỡ',10),(165,'nhồi máu cơ tim','máu nhiễm mỡ',10),(167,'xơ vữa động mạch','máu nhiễm mỡ',10),(169,'Đau cổ họng','viêm amidan',11),(171,'Amidan sưng đỏ','viêm amidan',11),(173,'Xuất hiện lớp dịch phủ màu trắng hoặc vàng','viêm amidan',11),(175,'Xuất hiện vết phồng rộp hoặc vết loét đau rát trên cổ họng','viêm amidan',11),(177,'Đau đầu','viêm amidan',12),(179,'Ăn mất ngon','viêm amidan',12),(181,'Đau tai','viêm amidan',12),(183,'Khó nuốt','viêm amidan',12),(185,'Sưng hạch ở cổ hoặc hàm','viêm amidan ',12),(187,'Sốt và ớn lạnh','viêm amidan',13),(189,'Hôi miệng','viêm amidan',13),(191,'Giọng nói khó nghe hoặc nghẹt thở','viêm amidan',13),(193,'Cổ cứng','viêm amidan',13),(195,'Bụng khó chịu','viêm amidan',14),(197,'Nôn mửa','viêm amidan',14),(199,'Đau bụng','viêm amidan',14),(201,'Chảy nước dãi','viêm amidan',14),(203,'Biếng ăn','viêm amidan',15),(205,'Vệ sinh khoang miệng không sạch sẽ','viêm amidan',15),(207,'Có dị tật ở cổ họng hay amidan','viêm amidan',15),(209,'Môi trường ô nhiễm (khói bụi, vệ sinh không kỹ…)','viêm amidan',15),(211,'Sử dụng thực phẩm không đảm bảo vệ sinh, hoặc sản phẩm đông lạnh (như kem, đá…)','viêm amidan',16),(213,'Thời tiết thay đổi đột ngột','viêm amidan',16),(215,'Hắt xì','viêm mũi dị ứng',17),(217,'Ngứa mũi, ngứa mắt hoặc vòm miệng','viêm mũi dị ứng',17),(219,'Chảy nước mũi, nghẹt mũi','viêm mũi dị ứng',17),(221,'Chảy nước nước, đỏ hoặc sưng mắt (viêm kết mạc)','viêm mũi dị ứng',18),(223,'Ngứa trong miệng','dị ứng thực phẩm',18),(225,'Sưng môi, lưỡi, mặt hoặc cổ họng','dị ứng thực phẩm',18),(227,'Nổi mề đay','dị ứng thực phẩm',18),(229,'Sốc phản vệ','dị ứng thực phẩm',19),(231,'Nổi mề đay','dị ứng thuốc',19),(233,'Ngứa da','dị ứng thuốc',19),(235,'Phát ban','dị ứng thuốc',20),(237,'Sưng mặt','dị ứng thuốc',20),(239,'Thở khò khè','dị ứng thuốc',20),(241,'Sốc phản vệ','dị ứng thuốc',20),(243,'Nổi mề đay','dị ứng thuốc',1),(245,'Ngứa da','dị ứng thuốc',1),(247,'Phát ban','dị ứng thuốc',2),(249,'Sưng mặt','dị ứng thuốc',2),(251,'Thở khò khè','dị ứng thuốc',3),(253,'Sốc phản vệ','dị ứng thuốc',3),(255,'Nổi mề đay','dị ứng thuốc',4),(257,'Ngứa da','dị ứng thuốc',4),(259,'Phát ban','dị ứng thuốc',4),(261,'Sưng mặt','dị ứng thuốc',4),(263,'Thở khò khè','dị ứng thuốc',5),(265,'Sốc phản vệ','dị ứng thuốc',5),(267,'Nổi mề đay','dị ứng thuốc',5),(269,'Ngứa da','dị ứng thuốc',5),(271,'Phát ban','dị ứng thuốc',5),(273,'Sưng mặt','dị ứng thuốc',5),(275,'Thở khò khè','dị ứng thuốc',6),(277,'Sốc phản vệ','dị ứng thuốc',7),(279,'Nổi mề đay','dị ứng thuốc',7),(281,'Ngứa da','dị ứng thuốc',8),(283,'Phát ban','dị ứng thuốc',9),(285,'Sưng mặt','dị ứng thuốc',9),(287,'Thở khò khè','dị ứng thuốc',9),(289,'Sốc phản vệ','dị ứng thuốc',10),(291,'Nổi mề đay','dị ứng thuốc',10),(293,'Ngứa da','dị ứng thuốc',10),(295,'Phát ban','dị ứng thuốc',10),(297,'Sưng mặt','dị ứng thuốc',11),(299,'Thở khò khè','dị ứng thuốc',11),(301,'Sốc phản vệ','dị ứng thuốc',12),(303,'Nổi mề đay','dị ứng thuốc',12),(305,'Ngứa da','dị ứng thuốc',13),(307,'Phát ban','dị ứng thuốc',13),(309,'Sưng mặt','dị ứng thuốc',14),(311,'Thở khò khè','dị ứng thuốc',14),(313,'Sốc phản vệ','dị ứng thuốc',15),(315,'Nổi mề đay','dị ứng thuốc',16),(317,'Ngứa da','dị ứng thuốc',17),(319,'Phát ban','dị ứng thuốc',17),(321,'Sưng mặt','dị ứng thuốc',18),(323,'Thở khò khè','dị ứng thuốc',18),(325,'Sốc phản vệ','dị ứng thuốc',19),(327,'Sốc phản vệ','dị ứng thuốc',20),(329,'Sốc phản vệ','dị ứng thuốc',20);
/*!40000 ALTER TABLE `medical_examination_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine_examination_detail_model`
--

DROP TABLE IF EXISTS `medicine_examination_detail_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `medicine_examination_detail_model` (
  `medicine_id` int NOT NULL,
  `medical_examination_id` int NOT NULL,
  `amount` int DEFAULT NULL,
  `dosage` text,
  `using_method` text,
  PRIMARY KEY (`medicine_id`,`medical_examination_id`),
  KEY `medical_examination_id` (`medical_examination_id`),
  CONSTRAINT `medicine_examination_detail_model_ibfk_1` FOREIGN KEY (`medicine_id`) REFERENCES `medicine_model` (`medicine_id`),
  CONSTRAINT `medicine_examination_detail_model_ibfk_2` FOREIGN KEY (`medical_examination_id`) REFERENCES `medical_examination_model` (`document_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine_examination_detail_model`
--

LOCK TABLES `medicine_examination_detail_model` WRITE;
/*!40000 ALTER TABLE `medicine_examination_detail_model` DISABLE KEYS */;
INSERT INTO `medicine_examination_detail_model` VALUES (1,1,11,'Ngăn ngừa sổ mũi','3 lần /ngày'),(1,27,4,'giảm đau đầu','4 lần/ngày'),(1,59,3,'giải nhiệt cơ thể','2 lần/ ngày'),(1,77,11,'Ngăn ngừa sổ mũi','3 lần/ngày'),(1,79,7,'Ngăn ngừa sổ mũi','3 lần/ngày'),(1,81,5,'giảm đau đầu','1 lần/ ngày'),(1,85,3,'Ngăn ngừa sổ mũi','3 lần/ngày'),(1,87,9,'giảm đau đầu','1 lần/ ngày'),(1,99,2,'hạ sốt','3 lần/ngày'),(1,157,11,'hạ sốt','1 lần/ ngày'),(1,159,4,'giảm đau đầu','1 lần/ ngày'),(1,175,10,'giảm đau đầu','2 lần/ngày'),(1,217,10,'hạ sốt','4 lần/ngày'),(1,219,8,'Ngăn ngừa sổ mũi','4 lần/ngày'),(1,281,6,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(2,1,21,'giảm đau đầu','2 lần/ngày'),(2,17,8,'giảm đau đầu','4 lần/ngày'),(2,59,2,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(2,81,6,'Ngăn ngừa sổ mũi','3 lần/ngày'),(2,87,2,'hạ sốt','4 lần/ngày'),(2,143,5,'hạ sốt','1 lần/ ngày'),(2,157,9,'giảm đau đầu','2 lần/ ngày'),(2,161,9,'giảm đau đầu','4 lần/ngày'),(2,185,2,'giải nhiệt cơ thể','4 lần/ngày'),(2,217,10,'Ngăn ngừa sổ mũi','3 lần/ngày'),(2,241,3,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(2,261,13,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(2,281,3,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(2,305,7,'giải nhiệt cơ thể','3 lần/ngày'),(3,5,6,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(3,17,6,'hạ sốt','2 lần/ ngày'),(3,57,3,'hạ sốt','3 lần/ngày'),(3,61,7,'giảm đau đầu','4 lần/ngày'),(3,77,13,'hạ sốt','1 lần/ ngày'),(3,81,6,'hạ sốt','4 lần/ngày'),(3,89,8,'hạ sốt','3 lần/ngày'),(3,101,11,'giảm đau đầu','3 lần/ngày'),(3,105,11,'Ngăn ngừa sổ mũi','3 lần/ngày'),(3,143,5,'Ngăn ngừa sổ mũi','4 lần/ngày'),(3,149,8,'hạ sốt','3 lần/ngày'),(3,183,2,'hạ sốt','2 lần/ ngày'),(3,217,10,'giảm đau đầu','1 lần/ ngày'),(3,247,5,'giảm đau đầu','2 lần/ ngày'),(3,291,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(4,5,5,'giảm đau đầu','3 lần/ngày'),(4,27,15,'hạ sốt','3 lần/ngày'),(4,37,6,'hạ sốt','3 lần/ngày'),(4,53,11,'giảm đau đầu','3 lần/ngày'),(4,61,7,'hạ sốt','2 lần/ngày'),(4,73,6,'giải nhiệt cơ thể','3 lần/ngày'),(4,89,7,'giảm đau đầu','1 lần/ ngày'),(4,103,9,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(4,121,7,'giảm đau đầu','1 lần/ ngày'),(4,157,9,'Ngăn ngừa sổ mũi','4 lần/ngày'),(4,165,2,'Ngăn ngừa sổ mũi','2 lần/ngày'),(4,187,3,'giảm đau đầu','3 lần/ngày'),(4,199,9,'Ngăn ngừa sổ mũi','4 lần/ngày'),(4,241,6,'giảm đau đầu','2 lần/ ngày'),(4,271,6,'giảm đau đầu','2 lần/ ngày'),(4,301,6,'giảm đau đầu','2 lần/ ngày'),(5,1,21,'giải nhiệt cơ thể','4 lần/ngày'),(5,27,2,'Ngăn ngừa sổ mũi','3 lần/ngày'),(5,47,8,'hạ sốt','1 lần/ ngày'),(5,59,3,'giải nhiệt cơ thể','4 lần/ngày'),(5,77,13,'giảm đau đầu','4 lần/ngày'),(5,79,7,'giải nhiệt cơ thể','3 lần/ngày'),(5,101,10,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(5,127,7,'hạ sốt','1 lần/ ngày'),(5,159,4,'hạ sốt','2 lần/ ngày'),(5,161,2,'hạ sốt','1 lần/ ngày'),(5,181,8,'giảm đau đầu','1 lần/ ngày'),(5,215,9,'giảm đau đầu','2 lần/ ngày'),(5,249,13,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(5,271,7,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(6,1,16,'tăng cường trí nhớ','1 lần/ ngày'),(6,23,12,'hạ sốt','4 lần/ngày'),(6,63,8,'Ngăn ngừa sổ mũi','3 lần/ngày'),(6,79,7,'giảm đau đầu','1 lần/ ngày'),(6,89,6,'Ngăn ngừa sổ mũi','4 lần/ngày'),(6,131,9,'hạ sốt','3 lần/ngày'),(6,133,11,'giải nhiệt cơ thể','1 lần/ ngày'),(6,159,6,'giảm đau đầu','3 lần/ngày'),(6,187,2,'hạ sốt','1 lần/ ngày'),(6,219,8,'giảm đau đầu','3 lần/ngày'),(6,259,9,'giảm đau đầu','2 lần/ ngày'),(6,267,11,'giảm đau đầu','1 lần/ ngày'),(6,291,6,'giảm đau đầu','2 lần/ ngày'),(7,1,13,'hạ sốt','1 lần/ngày'),(7,19,5,'giải nhiệt cơ thể','3 lần/ngày'),(7,77,11,'hạ sốt','1 lần/ ngày'),(7,105,11,'hạ sốt','4 lần/ngày'),(7,123,6,'hạ sốt','2 lần/ ngày'),(7,143,5,'giảm đau đầu','3 lần/ngày'),(7,161,8,'hạ sốt','3 lần/ngày'),(7,177,8,'hạ sốt','3 lần/ngày'),(7,213,7,'giải nhiệt cơ thể','4 lần/ngày'),(7,241,6,'hạ sốt','4 lần/ngày'),(7,261,8,'hạ sốt','4 lần/ngày'),(7,267,11,'Ngăn ngừa sổ mũi','3 lần/ngày'),(7,281,5,'hạ sốt','4 lần/ngày'),(7,291,2,'hạ sốt','4 lần/ngày'),(7,301,4,'hạ sốt','4 lần/ngày'),(8,3,10,'ngăn ngừa sụn khớp','4 lần/ngày'),(8,11,5,'hạ sốt','3 lần/ngày'),(8,23,11,'giảm đau đầu','3 lần/ngày'),(8,63,8,'giảm đau đầu','1 lần/ ngày'),(8,143,5,'hạ sốt','2 lần/ ngày'),(8,157,5,'giải nhiệt cơ thể','2 lần/ngày'),(8,179,8,'Ngăn ngừa sổ mũi','4 lần/ngày'),(8,219,8,'hạ sốt','2 lần/ ngày'),(8,249,6,'hạ sốt','4 lần/ngày'),(8,311,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(9,3,3,'tăng cường sinh lực','4 lần/ngày'),(9,21,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(9,25,2,'giải nhiệt cơ thể','1 lần/ ngày'),(9,83,5,'hạ sốt','3 lần/ngày'),(9,89,9,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(9,91,5,'giảm đau đầu','1 lần/ ngày'),(9,105,12,'giảm đau đầu','1 lần/ ngày'),(9,133,13,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(9,159,6,'Ngăn ngừa sổ mũi','3 lần/ngày'),(9,161,2,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(9,185,3,'Ngăn ngừa sổ mũi','3 lần/ngày'),(9,213,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(9,237,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(9,241,6,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(9,245,11,'Ngăn ngừa sổ mũi','3 lần/ngày'),(9,249,13,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(9,269,3,'hạ sốt','2 lần/ ngày'),(9,271,7,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(9,307,13,'Ngăn ngừa sổ mũi','3 lần/ngày'),(10,3,7,'giảm đau','1 lần/ ngày'),(10,11,6,'giải nhiệt cơ thể','3 lần/ngày'),(10,47,9,'giải nhiệt cơ thể','4 lần/ngày'),(10,53,11,'hạ sốt','4 lần/ngày'),(10,65,8,'hạ sốt','4 lần/ngày'),(10,97,6,'giảm đau đầu','1 lần/ ngày'),(10,135,13,'giảm đau đầu','4 lần/ngày'),(10,157,4,'Ngăn ngừa sổ mũi','4 lần/ngày'),(10,201,9,'hạ sốt','2 lần/ ngày'),(10,267,4,'giảm đau đầu','2 lần/ ngày'),(10,277,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(10,287,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(10,291,4,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(11,67,9,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(11,73,7,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(11,97,9,'giảm đau đầu','3 lần/ngày'),(11,109,6,'giải nhiệt cơ thể','3 lần/ngày'),(11,163,6,'giải nhiệt cơ thể','1 lần/ ngày'),(11,165,7,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(11,189,11,'giải nhiệt cơ thể','2 lần/ ngày'),(11,213,8,'giảm đau đầu','2 lần/ ngày'),(11,233,9,'hạ sốt','2 lần/ ngày'),(11,255,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(11,261,11,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(11,267,9,'hạ sốt','4 lần/ngày'),(11,271,12,'hạ sốt','4 lần/ngày'),(11,281,9,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(11,287,6,'giảm đau đầu','2 lần/ ngày'),(11,291,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(11,313,5,'hạ sốt','2 lần/ ngày'),(11,317,13,'giảm đau đầu','2 lần/ ngày'),(11,323,12,'hạ sốt','2 lần/ ngày'),(11,327,3,'hạ sốt','4 lần/ngày'),(12,11,4,'hạ sốt','4 lần/ngày'),(12,43,6,'hạ sốt','2 lần/ ngày'),(12,65,9,'giải nhiệt cơ thể','3 lần/ngày'),(12,67,13,'giảm đau đầu','1 lần/ ngày'),(12,145,6,'Ngăn ngừa sổ mũi','3 lần/ngày'),(12,167,8,'hạ sốt','3 lần/ngày'),(12,195,6,'giải nhiệt cơ thể','2 lần/ ngày'),(12,203,3,'Ngăn ngừa sổ mũi','3 lần/ngày'),(12,251,8,'hạ sốt','2 lần/ ngày'),(12,271,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(12,285,9,'giải nhiệt cơ thể','3 lần/ngày'),(12,301,3,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(12,317,11,'Ngăn ngừa sổ mũi','3 lần/ngày'),(12,325,11,'giải nhiệt cơ thể','3 lần/ngày'),(12,327,8,'giảm đau đầu','1 lần/ ngày'),(13,121,7,'Ngăn ngừa sổ mũi','4 lần/ngày'),(13,143,6,'giải nhiệt cơ thể','1 lần/ ngày'),(13,231,7,'hạ sốt','2 lần/ ngày'),(13,243,8,'hạ sốt','2 lần/ ngày'),(13,325,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(14,9,2,'giảm đau đầu','3 lần/ngày'),(14,15,12,'hạ sốt','3 lần/ngày'),(14,29,15,'giảm đau đầu','4 lần/ngày'),(14,35,3,'giảm đau đầu','2 lần/ngày'),(14,39,6,'hạ sốt','4 lần/ngày'),(14,51,10,'Ngăn ngừa sổ mũi','3 lần/ngày'),(14,71,5,'giải nhiệt cơ thể','2 lần/ ngày'),(14,93,3,'hạ sốt','2 lần/ ngày'),(14,97,4,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(14,107,11,'giảm đau đầu','1 lần/ ngày'),(14,135,12,'hạ sốt','3 lần/ngày'),(14,145,8,'hạ sốt','2 lần/ ngày'),(14,171,10,'giảm đau đầu','1 lần/ ngày'),(14,175,10,'Ngăn ngừa sổ mũi','3 lần/ngày'),(14,191,13,'giảm đau đầu','1 lần/ ngày'),(14,195,7,'hạ sốt','1 lần/ ngày'),(14,207,6,'hạ sốt','3 lần/ngày'),(14,215,9,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(14,237,6,'giảm đau đầu','2 lần/ ngày'),(14,297,12,'giảm đau đầu','2 lần/ ngày'),(14,307,11,'giảm đau đầu','2 lần/ ngày'),(14,311,4,'giảm đau đầu','2 lần/ ngày'),(15,7,5,'hạ sốt','1 lần/ ngày'),(15,15,8,'giảm đau đầu','3 lần/ngày'),(15,31,3,'hạ sốt','3 lần/ngày'),(15,37,4,'Ngăn ngừa sổ mũi','3 lần/ngày'),(15,41,6,'Ngăn ngừa sổ mũi','3 lần/ngày'),(15,73,4,'hạ sốt','1 lần/ ngày'),(15,95,2,'Ngăn ngừa sổ mũi','3 lần/ngày'),(15,97,3,'giảm đau đầu','2 lần/ ngày'),(15,107,6,'hạ sốt','3 lần/ngày'),(15,193,12,'hạ sốt','4 lần/ngày'),(15,243,4,'giảm đau đầu','2 lần/ ngày'),(15,253,6,'giảm đau đầu','2 lần/ ngày'),(15,293,8,'hạ sốt','2 lần/ ngày'),(16,37,7,'hạ sốt','3 lần/ngày'),(16,39,8,'giảm đau đầu','2 lần/ ngày'),(16,41,8,'giảm đau đầu','1 lần/ ngày'),(16,51,15,'giảm đau đầu','1 lần/ ngày'),(16,137,11,'giảm đau đầu','4 lần/ngày'),(16,155,5,'hạ sốt','3 lần/ngày'),(16,167,3,'giảm đau đầu','2 lần/ ngày'),(16,263,2,'hạ sốt','2 lần/ ngày'),(16,329,4,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(17,11,3,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(17,39,15,'hạ sốt','3 lần/ngày'),(17,147,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(17,193,11,'giải nhiệt cơ thể','2 lần/ ngày'),(17,241,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(17,259,2,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(17,301,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(17,311,2,'hạ sốt','4 lần/ngày'),(17,321,3,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(18,75,4,'giải nhiệt cơ thể','3 lần/ngày'),(18,83,5,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(18,171,11,'giải nhiệt cơ thể','4 lần/ngày'),(18,247,7,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(18,303,5,'hạ sốt','2 lần/ ngày'),(18,327,4,'giảm đau đầu','2 lần/ ngày'),(19,7,5,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(19,31,4,'giải nhiệt cơ thể','2 lần/ ngày'),(19,51,5,'hạ sốt','2 lần/ngày'),(19,127,6,'giải nhiệt cơ thể','2 lần/ ngày'),(19,149,2,'giải nhiệt cơ thể','3 lần/ngày'),(19,151,7,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(19,237,3,'giảm đau đầu','1 lần/ ngày'),(19,273,9,'hạ sốt','2 lần/ ngày'),(19,283,11,'hạ sốt','2 lần/ ngày'),(19,287,3,'giảm đau đầu','1 lần/ ngày'),(19,297,13,'giảm đau đầu','1 lần/ ngày'),(19,301,2,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(19,307,12,'giảm đau đầu','1 lần/ ngày'),(19,311,12,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(19,317,9,'giảm đau đầu','1 lần/ ngày'),(19,327,2,'Ngăn ngừa sổ mũi','3 lần/ngày'),(20,47,8,'giảm đau đầu','3 lần/ngày'),(20,49,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(20,53,5,'giải nhiệt cơ thể','3 lần/ngày'),(20,97,5,'hạ sốt','4 lần/ngày'),(20,115,8,'hạ sốt','1 lần/ ngày'),(20,167,7,'giải nhiệt cơ thể','3 lần/ngày'),(20,197,5,'hạ sốt','3 lần/ngày'),(20,243,6,'giải nhiệt cơ thể','3 lần/ngày'),(20,245,13,'giảm đau đầu','1 lần/ ngày'),(20,275,5,'giải nhiệt cơ thể','3 lần/ngày'),(21,3,2,'bổ mắt','3 lần/ngày'),(21,7,6,'giảm đau đầu','3 lần/ngày'),(21,11,2,'hạ sốt','1 lần/ ngày'),(21,41,5,'hạ sốt','3 lần/ngày'),(21,51,6,'hạ sốt','4 lần/ngày'),(21,97,6,'hạ sốt','3 lần/ngày'),(21,113,8,'giảm đau đầu','4 lần/ngày'),(21,119,5,'hạ sốt','3 lần/ngày'),(21,141,9,'giảm đau đầu','2 lần/ ngày'),(21,191,10,'giải nhiệt cơ thể','4 lần/ngày'),(21,205,2,'giải nhiệt cơ thể','4 lần/ngày'),(21,255,7,'giảm đau đầu','1 lần/ ngày'),(21,281,6,'giảm đau đầu','2 lần/ ngày'),(21,297,15,'Ngăn ngừa sổ mũi','3 lần/ngày'),(21,321,14,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(21,329,7,'hạ sốt','2 lần/ ngày'),(22,33,5,'hạ sốt','1 lần/ ngày'),(22,39,12,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(22,57,6,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(22,69,1,'hạ sốt','4 lần/ngày'),(22,73,7,'giảm đau đầu','4 lần/ngày'),(22,111,8,'giải nhiệt cơ thể','1 lần/ ngày'),(22,115,9,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(22,119,5,'giải nhiệt cơ thể','3 lần/ngày'),(22,165,5,'giảm đau đầu','4 lần/ngày'),(22,167,9,'hạ sốt','4 lần/ngày'),(22,193,7,'Ngăn ngừa sổ mũi','3 lần/ngày'),(22,235,9,'giải nhiệt cơ thể','3 lần/ngày'),(22,295,9,'giải nhiệt cơ thể','3 lần/ngày'),(22,299,10,'giải nhiệt cơ thể','4 lần/ngày'),(22,311,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(23,9,9,'hạ sốt','3 lần/ngày'),(23,29,4,'Ngăn ngừa sổ mũi','3 lần/ngày'),(23,39,2,'hạ sốt','4 lần/ngày'),(23,45,7,'giải nhiệt cơ thể','4 lần/ngày'),(23,129,9,'Ngăn ngừa sổ mũi','4 lần/ngày'),(23,173,11,'giải nhiệt cơ thể','3 lần/ngày'),(23,203,3,'giảm đau đầu','3 lần/ngày'),(23,251,10,'giải nhiệt cơ thể','3 lần/ngày'),(23,299,11,'hạ sốt','2 lần/ ngày'),(23,305,9,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(24,39,11,'giảm đau đầu','3 lần/ngày'),(24,127,7,'giảm đau đầu','3 lần/ngày'),(24,203,2,'hạ sốt','1 lần/ ngày'),(24,231,7,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(24,315,4,'giải nhiệt cơ thể','3 lần/ngày'),(24,321,10,'giảm đau đầu','2 lần/ ngày'),(25,51,5,'giảm đau đầu','3 lần/ngày'),(25,125,6,'giải nhiệt cơ thể','4 lần/ngày'),(25,137,12,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(25,151,7,'giảm đau đầu','2 lần/ ngày'),(25,165,8,'giảm đau đầu','1 lần/ ngày'),(25,201,9,'giảm đau đầu','1 lần/ ngày'),(25,205,6,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(25,231,7,'giảm đau đầu','4 lần/ngày'),(25,279,7,'giải nhiệt cơ thể','4 lần/ngày'),(25,289,3,'giải nhiệt cơ thể','4 lần/ngày'),(26,11,11,'giảm đau đầu','2 lần/ ngày'),(26,15,3,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(26,29,6,'hạ sốt','1 lần/ ngày'),(26,153,7,'hạ sốt','4 lần/ngày'),(26,171,12,'hạ sốt','2 lần/ ngày'),(27,13,7,'Ngăn ngừa sổ mũi','4 lần/ ngày'),(27,37,7,'Ngăn ngừa sổ mũi','4 lần/ngày'),(27,167,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(27,321,8,'hạ sốt','4 lần/ngày'),(27,329,6,'giải nhiệt cơ thể','4 lần/ngày'),(28,7,1,'hạ sốt','3 lần/ngày'),(28,75,9,'Ngăn ngừa sổ mũi','4 lần/ngày'),(28,147,8,'giảm đau đầu','4 lần/ngày'),(28,239,3,'giải nhiệt cơ thể','4 lần/ngày'),(28,269,9,'giải nhiệt cơ thể','4 lần/ngày'),(28,309,6,'giải nhiệt cơ thể','4 lần/ngày'),(28,319,5,'giải nhiệt cơ thể','4 lần/ngày'),(29,155,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(29,239,3,'hạ sốt','2 lần/ ngày'),(29,247,9,'giải nhiệt cơ thể','4 lần/ngày'),(29,277,2,'giảm đau đầu','1 lần/ ngày'),(29,289,7,'hạ sốt','2 lần/ ngày'),(29,309,10,'hạ sốt','2 lần/ ngày'),(29,319,7,'hạ sốt','2 lần/ ngày'),(29,321,6,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(30,45,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(30,49,7,'hạ sốt','2 lần/ ngày'),(30,53,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(30,75,9,'giảm đau đầu','2 lần/ ngày'),(30,97,5,'giải nhiệt cơ thể','2 lần/ ngày'),(30,145,6,'giảm đau đầu','3 lần/ngày'),(30,157,4,'giải nhiệt cơ thể','3 lần/ngày'),(30,173,10,'giải nhiệt cơ thể','1 lần/ ngày'),(30,199,5,'giải nhiệt cơ thể','3 lần/ngày'),(30,245,8,'hạ sốt','2 lần/ ngày'),(30,257,3,'giải nhiệt cơ thể','4 lần/ngày'),(30,279,6,'hạ sốt','2 lần/ ngày'),(31,13,5,'giảm đau đầu','4 lần/ngày'),(31,29,6,'hạ sốt','3 lần/ngày'),(31,43,5,'giải nhiệt cơ thể','3 lần/ngày'),(31,51,9,'giải nhiệt cơ thể','2 lần/ ngày'),(31,69,5,'giải nhiệt cơ thể','3 lần/ngày'),(31,97,4,'giải nhiệt cơ thể','1 lần/ ngày'),(31,139,9,'giải nhiệt cơ thể','1 lần/ ngày'),(31,157,9,'giảm đau đầu','1 lần/ ngày'),(31,169,7,'Ngăn ngừa sổ mũi','3 lần/ngày'),(31,209,10,'Ngăn ngừa sổ mũi','3 lần/ngày'),(31,243,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(31,257,9,'hạ sốt','2 lần/ ngày'),(31,275,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(32,13,9,'hạ sốt','2 lần/ ngày'),(32,29,8,'giải nhiệt cơ thể','1 lần/ ngày'),(32,39,10,'giảm đau đầu','1 lần/ ngày'),(32,57,5,'giảm đau đầu','1 lần/ ngày'),(32,139,11,'hạ sốt','2 lần/ ngày'),(32,155,5,'giảm đau đầu','3 lần/ngày'),(32,191,13,'Ngăn ngừa sổ mũi','3 lần/ngày'),(32,211,11,'giảm đau đầu','1 lần/ ngày'),(32,235,6,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(32,265,9,'giải nhiệt cơ thể','3 lần/ngày'),(32,295,10,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(32,317,12,'hạ sốt','4 lần/ngày'),(33,29,7,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(33,73,6,'hạ sốt','3 lần/ngày'),(33,111,8,'Ngăn ngừa sổ mũi','2 lần/ ngày'),(33,115,7,'giảm đau đầu','4 lần/ngày'),(33,131,9,'giảm đau đầu','3 lần/ngày'),(33,153,8,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(33,167,6,'giải nhiệt cơ thể','4 lần/ngày'),(33,193,8,'giảm đau đầu','4 lần/ngày'),(33,213,13,'hạ sốt','2 lần/ ngày'),(33,215,8,'hạ sốt','3 lần/ngày'),(33,245,7,'hạ sốt','4 lần/ngày'),(33,285,13,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(33,297,14,'hạ sốt','4 lần/ngày'),(34,13,8,'giải nhiệt cơ thể','1 lần/ ngày'),(34,29,8,'giảm đau đầu','3 lần/ngày'),(34,39,9,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(34,43,4,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(34,51,4,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(34,79,7,'giải nhiệt cơ thể','2 lần/ ngày'),(34,97,6,'Ngăn ngừa sổ mũi','4 lần/ngày'),(34,117,9,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(34,141,9,'Ngăn ngừa sổ mũi','3 lần/ngày'),(34,237,5,'hạ sốt','4 lần/ngày'),(34,251,11,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(34,277,5,'hạ sốt','4 lần/ngày'),(34,287,9,'hạ sốt','4 lần/ngày'),(34,307,15,'hạ sốt','4 lần/ngày'),(35,7,3,'Ngăn ngừa sổ mũi','4 lần/ngày'),(35,9,7,'Ngăn ngừa sổ mũi','4 lần/ngày'),(35,33,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(35,37,5,'giảm đau đầu','1 lần/ ngày'),(35,85,3,'giảm đau đầu','1 lần/ ngày'),(35,117,5,'giảm đau đầu','2 lần/ ngày'),(35,125,5,'Ngăn ngừa sổ mũi','3 lần/ngày'),(35,165,5,'hạ sốt','3 lần/ngày'),(35,205,6,'giảm đau đầu','1 lần/ ngày'),(35,207,10,'giải nhiệt cơ thể','2 lần/ngày'),(35,253,5,'hạ sốt','4 lần/ngày'),(35,265,5,'Ngăn ngừa sổ mũi','1 lần/ ngày'),(35,277,9,'giảm đau đầu','2 lần/ ngày'),(35,315,6,'Ngăn ngừa sổ mũi','1 lần/ ngày');
/*!40000 ALTER TABLE `medicine_examination_detail_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine_model`
--

DROP TABLE IF EXISTS `medicine_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `medicine_model` (
  `medicine_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `amount` int DEFAULT NULL,
  `unit_price` decimal(10,0) DEFAULT NULL,
  `import_date` datetime DEFAULT NULL,
  `expiration_date` datetime DEFAULT NULL,
  `dosage` varchar(200) DEFAULT NULL,
  `manufacturer` varchar(100) DEFAULT NULL,
  `description` text,
  `category_id` int DEFAULT NULL,
  `medicine_unit_id` int DEFAULT NULL,
  PRIMARY KEY (`medicine_id`),
  UNIQUE KEY `name` (`name`),
  KEY `category_id` (`category_id`),
  KEY `medicine_unit_id` (`medicine_unit_id`),
  CONSTRAINT `medicine_model_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category_model` (`category_id`),
  CONSTRAINT `medicine_model_ibfk_2` FOREIGN KEY (`medicine_unit_id`) REFERENCES `medicine_unit_model` (`medicine_unit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine_model`
--

LOCK TABLES `medicine_model` WRITE;
/*!40000 ALTER TABLE `medicine_model` DISABLE KEYS */;
INSERT INTO `medicine_model` VALUES (1,'Paracetamol',100,1000,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',1,1),(2,'Alphachymotrylsilh',100,3000,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',2,1),(3,'Meloxicam',100,1500,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',3,1),(4,'Celecoxib',100,500,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',4,2),(5,'Piroxicam',100,700,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',1,1),(6,'Prednisolon',100,1200,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',2,1),(7,'Methylprednisolon',100,900,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',3,1),(8,'Alphachymotrylsil',100,400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc giảm đau, hạ sốt, kháng viêm',4,1),(9,'Amoxicillin',100,2400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',1,1),(10,'Ampicillin',100,4300,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',2,1),(11,'Cefixime',100,1500,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',3,2),(12,'Cefpodoxime',100,900,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',4,1),(13,'Cefuroxime',100,2400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',1,1),(14,'Cephalexin',100,2600,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',2,1),(15,'Cefnidir',100,4300,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',3,2),(16,'Klamentin',100,2300,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',4,1),(17,'Azithromycin',100,3400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Việt Nam','thuốc kháng sinh',1,2),(18,'Docxycyclin',100,6400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',2,1),(19,'Ciprofloxacin',100,1400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',3,2),(20,'Levofloxacin',100,400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Việt Nam','thuốc kháng sinh',4,1),(21,'Metronidazol',100,2400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','US','thuốc kháng sinh',1,2),(22,'Chlorpheniramin',100,200,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Việt Nam','thuốc kháng histamin',2,1),(23,'Alimemazin',100,400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ampharco ','thuốc kháng histamin',3,1),(24,'Loratadin',100,500,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ampharco ','thuốc kháng histamin',4,1),(25,'Fexofenadin',100,800,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ampharco ','thuốc kháng histamin',1,1),(26,'Cetirizine',100,900,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ampharco ','thuốc kháng histamin',2,1),(27,'Omeprazol',100,1200,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ấn','thuốc dạ dày',3,1),(28,'Esomeprazol',100,1400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ấn','thuốc dạ dày',4,2),(29,'Pantoprazol',100,4100,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ấn','thuốc dạ dày',1,1),(30,'Lansoprazol',100,2300,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ấn','thuốc dạ dày',2,2),(31,'Rabeprazol',100,2400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ấn','thuốc dạ dày',3,1),(32,'Domperidol',100,2500,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Ấn','thuốc dạ dày',4,2),(33,'Acetylcystein',100,2900,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Muscosolvan','thuốc ho – long đờm',1,1),(34,'Bromhexin',100,3200,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Muscosolvan','thuốc ho – long đờm',2,1),(35,'Ambroxol',100,1400,'2021-12-06 22:19:41','2021-12-06 22:19:41','liều 1','Muscosolvan','thuốc ho – long đờm',3,1);
/*!40000 ALTER TABLE `medicine_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine_unit_model`
--

DROP TABLE IF EXISTS `medicine_unit_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `medicine_unit_model` (
  `medicine_unit_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`medicine_unit_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine_unit_model`
--

LOCK TABLES `medicine_unit_model` WRITE;
/*!40000 ALTER TABLE `medicine_unit_model` DISABLE KEYS */;
INSERT INTO `medicine_unit_model` VALUES (2,'chai'),(1,'viên');
/*!40000 ALTER TABLE `medicine_unit_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nurse_model`
--

DROP TABLE IF EXISTS `nurse_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `nurse_model` (
  `staff_id` int NOT NULL,
  PRIMARY KEY (`staff_id`),
  CONSTRAINT `nurse_model_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff_model` (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nurse_model`
--

LOCK TABLES `nurse_model` WRITE;
/*!40000 ALTER TABLE `nurse_model` DISABLE KEYS */;
INSERT INTO `nurse_model` VALUES (21),(22),(23),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(36),(37),(38),(39),(40);
/*!40000 ALTER TABLE `nurse_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_model`
--

DROP TABLE IF EXISTS `role_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `role_model` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_model`
--

LOCK TABLES `role_model` WRITE;
/*!40000 ALTER TABLE `role_model` DISABLE KEYS */;
INSERT INTO `role_model` VALUES (2,'bác sĩ'),(1,'quản trị viên'),(3,'y tá');
/*!40000 ALTER TABLE `role_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rule_model`
--

DROP TABLE IF EXISTS `rule_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `rule_model` (
  `rule_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`rule_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rule_model`
--

LOCK TABLES `rule_model` WRITE;
/*!40000 ALTER TABLE `rule_model` DISABLE KEYS */;
INSERT INTO `rule_model` VALUES (1,'số lượng',30),(2,'tiền khám bệnh',100000);
/*!40000 ALTER TABLE `rule_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_model`
--

DROP TABLE IF EXISTS `staff_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `staff_model` (
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `id_card` varchar(12) DEFAULT NULL,
  `address` varchar(150) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(10) DEFAULT NULL,
  `sex` enum('MALE','FEMALE') DEFAULT NULL,
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `date_of_work` datetime DEFAULT NULL,
  `exp_year` float DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `avatar` varchar(200) DEFAULT NULL,
  `facebook_link` varchar(130) DEFAULT NULL,
  `twitter_link` varchar(130) DEFAULT NULL,
  `contained_department_id` int DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  `account_id` int DEFAULT NULL,
  PRIMARY KEY (`staff_id`),
  UNIQUE KEY `id_card` (`id_card`),
  KEY `contained_department_id` (`contained_department_id`),
  KEY `manager_id` (`manager_id`),
  KEY `account_id` (`account_id`),
  CONSTRAINT `staff_model_ibfk_1` FOREIGN KEY (`contained_department_id`) REFERENCES `department_model` (`department_id`),
  CONSTRAINT `staff_model_ibfk_2` FOREIGN KEY (`manager_id`) REFERENCES `staff_model` (`staff_id`),
  CONSTRAINT `staff_model_ibfk_3` FOREIGN KEY (`account_id`) REFERENCES `account_model` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_model`
--

LOCK TABLES `staff_model` WRITE;
/*!40000 ALTER TABLE `staff_model` DISABLE KEYS */;
INSERT INTO `staff_model` VALUES ('Vũ An','Nguyễn','2021-12-06 22:19:41','01239456789','47/12 Bùi Đình Tuý f24 Q.Bình Thạnh',NULL,'0123456789','MALE',1,'2021-12-06 22:19:41',1,'doctor',NULL,NULL,NULL,1,NULL,1),('Quốc Thịnh','Võ','2021-12-06 22:19:41','0123856789','268 Tô Hiến Thành - p.15 - Q.10',NULL,'0123456788','MALE',2,'2021-12-06 22:19:41',2,'doctor',NULL,NULL,NULL,2,1,2),('Văn Quang','Đinh','2021-12-06 22:19:41','01237456789','260/24 nguyễn thái bình - f12 -  tân bình',NULL,'0123456789','MALE',3,'2021-12-06 22:19:41',3,'doctor',NULL,NULL,NULL,3,1,4),('Tuấn Anh','Nguyễn','2021-12-06 22:19:41','01236456789','số nhà 46 Ngõ 6 Phố Bà Triệu- Phường Nguyễn Trãi- Quận Hà Đông',NULL,'0123456789','MALE',4,'2021-12-06 22:19:41',4,'doctor',NULL,NULL,NULL,4,2,5),('Đức Chính','Bùi','2021-12-06 22:19:41','01235456789','182/25 Lê Văn Sỹ P10 Q Phú Nhuận',NULL,'0123456788','MALE',5,'2021-12-06 22:19:41',2.5,'doctor',NULL,NULL,NULL,5,2,6),('Minh Quang','Nguyễn','2021-12-06 22:19:41','01234456789','53 Nguyễn Đình Chiểu, P.6, Q.3',NULL,'0123456788','MALE',6,'2021-12-06 22:19:41',1,'doctor',NULL,NULL,NULL,6,2,7),('Quốc Hùng','Phạm','2021-12-06 22:19:41','012334567890','14/28 Văn Chung P13 Tân Bình',NULL,'0123456788','MALE',7,'2021-12-06 22:19:41',2,'doctor',NULL,NULL,NULL,7,2,8),('Thị Như Thuỷ','Trần','2021-12-06 22:19:41','01232456789','014 Chung cư H1, Vĩnh Khánh, Phường 6, Quận 4',NULL,'0123456788','FEMALE',8,'2021-12-06 22:19:41',3,'doctor',NULL,NULL,NULL,9,2,9),('Đình Tiến','Nguyễn','2021-12-06 22:19:41','01231456789','12G1 Ngô Đức Kế,Phường7, TP Vũng Tàu',NULL,'0123456788','MALE',9,'2021-12-06 22:19:41',2,'doctor',NULL,NULL,NULL,8,2,10),('Khắc Chính','Nguyễn','2021-12-06 22:19:41','01293456789','Số 1 - Kim Ngoc - Ngô Quyền - Vĩnh Yên',NULL,'0123456788','MALE',10,'2021-12-06 22:19:41',3,'doctor',NULL,NULL,NULL,4,2,11),('Khánh Hoàn','Trần','2021-12-06 22:19:41','01283456789','83 Lê Lợi P6 TP Sóc Trăng',NULL,'0123456788','MALE',11,'2021-12-06 22:19:41',1,'doctor',NULL,NULL,NULL,5,2,12),('Công Trung','Huỳnh','2021-12-06 22:19:41','01273456789','323 Lý Tự Trọng, phường Bến Thành, quận 1',NULL,'0123456788','MALE',12,'2021-12-06 22:19:41',2,'doctor',NULL,NULL,NULL,6,2,13),('Thị Hồng Na','Vũ','2021-12-06 22:19:41','01263456789','Số 3 Ngõ 20 Hàng Vôi',NULL,'0123456788','FEMALE',13,'2021-12-06 22:19:41',3,'doctor',NULL,NULL,NULL,10,2,14),('Thị Hồng Loan','Vũ','2021-12-06 22:19:41','01253456789','Số 9 Ngõ 12 Đường Phan Văn Trường, Cầu Giấy',NULL,'0123456788','FEMALE',14,'2021-12-06 22:19:41',2,'doctor',NULL,NULL,NULL,2,2,15),('Linh','Nguyễn','2021-12-06 22:19:41','01243456789','E27, Cư Xá 304-307, D1, P.25, Q. Bình Thạnh',NULL,'0123456788','FEMALE',15,'2021-12-06 22:19:41',1,'doctor',NULL,NULL,NULL,3,2,16),('Ngọc','Hoàng','2021-12-06 22:19:41','01233456789','Tổ 8, Khu 5, P. Hồng Hải, Tp. Hạ Long',NULL,'0123456788','MALE',16,'2021-12-06 22:19:41',4,'doctor',NULL,NULL,NULL,4,2,17),('Linh Nhi','Nguyễn','2021-12-06 22:19:41','012234567892','Đội 1, Xuân Vinh, Xuân Trường, Nam Định',NULL,'0123456788','FEMALE',17,'2021-12-06 22:19:41',2,'doctor',NULL,NULL,NULL,5,2,18),('Thuỳ Linh','Trịnh','2021-12-06 22:19:41','01213456789','Xã Phú Hội, Tx. Phú Thọ',NULL,'0123456788','FEMALE',18,'2021-12-06 22:19:41',6,'doctor',NULL,NULL,NULL,6,2,19),('Gia Bảo','Hồ','2021-12-06 22:19:41','01923456789','Sn 27, Ngõ 111 Cù Chính Lan, Thanh Xuân',NULL,'0123456788','MALE',19,'2021-12-06 22:19:41',4,'doctor',NULL,NULL,NULL,7,2,20),('Trúc Nhi','Nguyễn','2021-12-06 22:19:41','01823456789','Số 4 Láng Hạ, Ba Đình',NULL,'0123456788','MALE',20,'2021-12-06 22:19:41',7,'doctor',NULL,NULL,NULL,8,3,21),('Hoàng Ái Ly','Nguyễn','2021-12-06 22:19:41','01723456789','375b Tổ 31 Phường Kỳ Bá',NULL,'0123456788','FEMALE',21,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,9,3,3),('Ngọc','Nguyễn','2021-12-06 22:19:41','01623456789','66d Phan Đăng Lưu, P.5, Q. Phú Nhuận',NULL,'0123456788','FEMALE',22,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,10,3,22),('Linh Chi','Nguyễn','2021-12-06 22:19:41','01523456789','5a Thi Sách, Q. Hai Bà Trưng',NULL,'0123456788','FEMALE',23,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,9,3,23),('Trường Thọ','Nguyễn','2021-12-06 22:19:41','01423456789','378 Nguyễn Văn Cừ, Lộc Phát, Bảo Lộc',NULL,'0123456788','MALE',24,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,8,3,24),('Tấn Trường','Nguyễn','2021-12-06 22:19:41','01323456789','101b  u Cơ, Tây Hồ',NULL,'0123456788','MALE',25,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,7,3,25),('Hoàng','Nguyễn','2021-12-06 22:19:41','01223456789','Sn 14, Ngõ 486/14/8 Ngô Gia Tự, Tổ 17a, P. Đức Giang, Q. Long Biên',NULL,'0123456788','FEMALE',26,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,6,3,26),('Ái Ly','Trương','2021-12-06 22:19:41','011234567896','105 Ql51 Ấp Thiền Đức, Phước Thái, Long Thành',NULL,'0123456788','FEMALE',27,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,5,3,27),('Ngọc Chi','Hoàng','2021-12-06 22:19:41','09123456789','Khu Cn Phú Tài, Tp. Quy Nhơn',NULL,'0123456788','FEMALE',28,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,4,3,28),('Ngọc','Lý','2021-12-06 22:19:41','08123456789','125 Nguyễn Văn Cừ, Móng Cái',NULL,'0123456788','FEMALE',29,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,3,3,29),('Thành Nam','Nguyễn','2021-12-06 22:19:41','07123456789','269/4 Nguyễn Trãi, Q. 1',NULL,'0123456788','MALE',30,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,6,3,30),('Đình Phong','Nguyễn','2021-12-06 22:19:41','06123456789','Số 8, Khu B5, Đô Thị Mới Đại Kim, Q. Hoàng Mai',NULL,'0123456788','MALE',31,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,1,3,31),('Nhật','Nguyễn','2021-12-06 22:19:41','05123456789','84a/44 Trần Hữu Trang, P10, Q. Phú Nhuận',NULL,'0123456788','MALE',32,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,2,3,32),('Trung Hiếu','La','2021-12-06 22:19:41','04123456789','84a/44 Trần Hữu Trang, P10, Q. Phú Nhuận',NULL,'0123456788','MALE',33,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,3,3,33),('Tấn Đạt','Trương','2021-12-06 22:19:41','03123456789','Đường Mẹ Suốt, Chợ Đồng Hới',NULL,'0123456788','MALE',34,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,4,3,34),('Thanh Định','Nguyễn','2021-12-06 22:19:41','02123456789','339/29 Tô Hiến Thành, P13, Q10',NULL,'0123456788','MALE',35,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,5,3,35),('Hồng Ngọc','Nguyễn','2021-12-06 22:19:41','01123456789','Đường Lê Lợi, Tổ 13, Châu Quế 2, Phường B, Tx. Châu Đốc',NULL,'0123456788','FEMALE',36,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,6,3,36),('Lý','Nguyễn','2021-12-06 22:19:41','90123456789','60 Tôn Thất Tùng, P. Bến Thành, Q.1',NULL,'0123456788','MALE',37,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,1,3,37),('Hoàng Yến','Nguyễn','2021-12-06 22:19:41','80123456789','Số 10, Nguyễn Quyền, Hoàn Kiếm',NULL,'0123456788','FEMALE',38,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,2,3,38),('Yến Nhi','Nguyễn','2021-12-06 22:19:41','70123456789','Cầu Dứa, Đường 23/10 Nha Trang',NULL,'0123456788','FEMALE',39,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,3,3,39),('Nguyên','Nguyễn','2021-12-06 22:19:41','60123456789','801/75 Xô Viết Nghệ Tĩnh, P. 26, Q. Bình Thạnh',NULL,'0123456788','MALE',40,'2021-12-06 22:19:41',0,'nurse',NULL,NULL,NULL,10,3,40);
/*!40000 ALTER TABLE `staff_model` ENABLE KEYS */;
UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-18 10:06:08
