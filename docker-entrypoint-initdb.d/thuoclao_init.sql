-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: mping
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

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
-- Table structure for table `accounts_userprofile`
--

DROP TABLE IF EXISTS `accounts_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(1024) NOT NULL,
  `city` varchar(100) NOT NULL,
  `website` varchar(200) NOT NULL,
  `phone` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `accounts_userprofile_user_id_92240672_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userprofile`
--

LOCK TABLES `accounts_userprofile` WRITE;
/*!40000 ALTER TABLE `accounts_userprofile` DISABLE KEYS */;
INSERT INTO `accounts_userprofile` VALUES (1,'','','',0,'profile_image/user.png',1),(4,'','','',0,'profile_image/user.png',4);
/*!40000 ALTER TABLE `accounts_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add host_attribute',7,'add_host_attribute'),(20,'Can change host_attribute',7,'change_host_attribute'),(21,'Can delete host_attribute',7,'delete_host_attribute'),(22,'Can add group',8,'add_group'),(23,'Can change group',8,'change_group'),(24,'Can delete group',8,'delete_group'),(25,'Can add group_attribute',9,'add_group_attribute'),(26,'Can change group_attribute',9,'change_group_attribute'),(27,'Can delete group_attribute',9,'delete_group_attribute'),(28,'Can add service',10,'add_service'),(29,'Can change service',10,'change_service'),(30,'Can delete service',10,'delete_service'),(31,'Can add host',11,'add_host'),(32,'Can change host',11,'change_host'),(33,'Can delete host',11,'delete_host'),(34,'Can add alert',12,'add_alert'),(35,'Can change alert',12,'change_alert'),(36,'Can delete alert',12,'delete_alert'),(37,'Can add user profile',13,'add_userprofile'),(38,'Can change user profile',13,'change_userprofile'),(39,'Can delete user profile',13,'delete_userprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$FW3LXXtKyvgN$VglQPoaN6vk4zgbbBWgug07PnyHjxevvHvbGV1olKqE=','2018-07-23 03:55:40.035077',1,'admin','','','',1,1,'2018-07-20 02:16:45.286976'),(4,'pbkdf2_sha256$100000$HaTMvyCrwUyK$5xPmBvudVvcpJxr88KaCxOUz4/YMnTm83VQwfeSvfP0=','2018-07-23 03:55:24.378591',0,'user2','','','',0,1,'2018-07-23 03:55:03.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_alert`
--

DROP TABLE IF EXISTS `check_alert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `check_alert` (
  `user_id` int(11) NOT NULL,
  `email_alert` varchar(100) NOT NULL,
  `telegram_id` varchar(10) NOT NULL,
  `webhook` varchar(200) NOT NULL,
  `delay_check` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `check_alert_user_id_167e5719_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_alert`
--

LOCK TABLES `check_alert` WRITE;
/*!40000 ALTER TABLE `check_alert` DISABLE KEYS */;
/*!40000 ALTER TABLE `check_alert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_group`
--

DROP TABLE IF EXISTS `check_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `check_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(45) NOT NULL,
  `description` longtext,
  `ok` int(11) DEFAULT NULL,
  `warning` int(11) DEFAULT NULL,
  `critical` int(11) DEFAULT NULL,
  `service_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `check_group_service_id_544b3777_fk_check_service_id` (`service_id`),
  KEY `check_group_user_id_f5f190b2_fk_auth_user_id` (`user_id`),
  CONSTRAINT `check_group_service_id_544b3777_fk_check_service_id` FOREIGN KEY (`service_id`) REFERENCES `check_service` (`id`),
  CONSTRAINT `check_group_user_id_f5f190b2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_group`
--

LOCK TABLES `check_group` WRITE;
/*!40000 ALTER TABLE `check_group` DISABLE KEYS */;
INSERT INTO `check_group` VALUES (5,'Ping Default','',10,40,100,1,4),(6,'HTTP Default','',NULL,NULL,NULL,2,4),(7,'Ping Default','',10,40,100,1,1),(8,'HTTP Default','',NULL,NULL,NULL,2,1);
/*!40000 ALTER TABLE `check_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_group_attribute`
--

DROP TABLE IF EXISTS `check_group_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `check_group_attribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attribute_name` varchar(45) NOT NULL,
  `value` varchar(100) NOT NULL,
  `type_value` int(11) DEFAULT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `check_group_attribute_group_id_02843754_fk_check_group_id` (`group_id`),
  CONSTRAINT `check_group_attribute_group_id_02843754_fk_check_group_id` FOREIGN KEY (`group_id`) REFERENCES `check_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_group_attribute`
--

LOCK TABLES `check_group_attribute` WRITE;
/*!40000 ALTER TABLE `check_group_attribute` DISABLE KEYS */;
INSERT INTO `check_group_attribute` VALUES (7,'interval_ping','20',0,5),(8,'number_packet','20',0,5),(9,'interval_check','20',0,6),(10,'interval_ping','20',0,7),(11,'number_packet','20',0,7),(12,'interval_check','20',0,8);
/*!40000 ALTER TABLE `check_group_attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_host`
--

DROP TABLE IF EXISTS `check_host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `check_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(45) NOT NULL,
  `description` longtext,
  `status` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `check_host_group_id_89f04e14_fk_check_group_id` (`group_id`),
  CONSTRAINT `check_host_group_id_89f04e14_fk_check_group_id` FOREIGN KEY (`group_id`) REFERENCES `check_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_host`
--

LOCK TABLES `check_host` WRITE;
/*!40000 ALTER TABLE `check_host` DISABLE KEYS */;
/*!40000 ALTER TABLE `check_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_host_attribute`
--

DROP TABLE IF EXISTS `check_host_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `check_host_attribute` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attribute_name` varchar(45) NOT NULL,
  `value` varchar(100) NOT NULL,
  `type_value` int(11) DEFAULT NULL,
  `host_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `check_host_attribute_host_id_e2260eb2_fk_check_host_id` (`host_id`),
  CONSTRAINT `check_host_attribute_host_id_e2260eb2_fk_check_host_id` FOREIGN KEY (`host_id`) REFERENCES `check_host` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_host_attribute`
--

LOCK TABLES `check_host_attribute` WRITE;
/*!40000 ALTER TABLE `check_host_attribute` DISABLE KEYS */;
/*!40000 ALTER TABLE `check_host_attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_service`
--

DROP TABLE IF EXISTS `check_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `check_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_service`
--

LOCK TABLES `check_service` WRITE;
/*!40000 ALTER TABLE `check_service` DISABLE KEYS */;
INSERT INTO `check_service` VALUES (1,'ping'),(2,'http');
/*!40000 ALTER TABLE `check_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-07-20 02:18:54.148180','1','ping',1,'[{\"added\": {}}]',10,1),(2,'2018-07-20 02:19:00.303827','2','http',1,'[{\"added\": {}}]',10,1),(3,'2018-07-23 02:02:59.351661','2','user1',1,'[{\"added\": {}}]',4,1),(4,'2018-07-23 02:03:05.685878','2','user1',2,'[]',4,1),(5,'2018-07-23 02:04:22.617266','2','user1',3,'',4,1),(6,'2018-07-23 03:01:44.040581','3','user1',1,'[{\"added\": {}}]',4,1),(7,'2018-07-23 03:01:47.183580','3','user1',2,'[]',4,1),(8,'2018-07-23 03:54:38.690064','3','user1',3,'',4,1),(9,'2018-07-23 03:55:04.369764','4','user2',1,'[{\"added\": {}}]',4,1),(10,'2018-07-23 03:55:07.947902','4','user2',2,'[]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (13,'accounts','userprofile'),(1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(12,'check','alert'),(8,'check','group'),(9,'check','group_attribute'),(11,'check','host'),(7,'check','host_attribute'),(10,'check','service'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-07-20 02:13:38.945292'),(2,'auth','0001_initial','2018-07-20 02:13:53.075117'),(3,'accounts','0001_initial','2018-07-20 02:13:55.218784'),(4,'admin','0001_initial','2018-07-20 02:13:58.388828'),(5,'admin','0002_logentry_remove_auto_add','2018-07-20 02:13:58.478740'),(6,'contenttypes','0002_remove_content_type_name','2018-07-20 02:14:00.438737'),(7,'auth','0002_alter_permission_name_max_length','2018-07-20 02:14:00.707310'),(8,'auth','0003_alter_user_email_max_length','2018-07-20 02:14:00.910740'),(9,'auth','0004_alter_user_username_opts','2018-07-20 02:14:01.005624'),(10,'auth','0005_alter_user_last_login_null','2018-07-20 02:14:01.826695'),(11,'auth','0006_require_contenttypes_0002','2018-07-20 02:14:01.889526'),(12,'auth','0007_alter_validators_add_error_messages','2018-07-20 02:14:01.966736'),(13,'auth','0008_alter_user_username_max_length','2018-07-20 02:14:05.553033'),(14,'auth','0009_alter_user_last_name_max_length','2018-07-20 02:14:05.809239'),(15,'check','0001_initial','2018-07-20 02:14:19.171306'),(16,'sessions','0001_initial','2018-07-20 02:14:20.297232');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('cqnjf0gacl7rr88rkg9p62nsq7bdqwz7','NzIyYTE0NzQwM2JjYjA4MmJmMWIzNDNkNmEwM2M1NGJmYmIyNWJlNzp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ4N2ViM2JlNTI2ODFjMDdiNzc5Y2MxMGNhZTBiM2I4NjUwMDE2ZTMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2018-08-06 03:55:40.438028'),('cz4hewpffek72vl3dfdvwfzqo8ox9euv','YWUwYWZkMDIxMTI5MjIxYjU4ZmM5N2E1NjkyNTJjNTM5NmI0YWZmNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkODdlYjNiZTUyNjgxYzA3Yjc3OWNjMTBjYWUwYjNiODY1MDAxNmUzIn0=','2018-08-05 04:20:37.335105'),('o0c6s4jf0jsefrfuwzpfdcbkyafb7i09','YWUwYWZkMDIxMTI5MjIxYjU4ZmM5N2E1NjkyNTJjNTM5NmI0YWZmNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkODdlYjNiZTUyNjgxYzA3Yjc3OWNjMTBjYWUwYjNiODY1MDAxNmUzIn0=','2018-08-06 02:10:56.192988'),('vp4eopj2p3qbcgnxx3k7mwhmr8pj3c8y','MmQ1ZDkyOGZlYTY5MzFmYzZkNTYyNTJiNTE1ZmNiMTdlNjA0MzQ1Yzp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ4N2ViM2JlNTI2ODFjMDdiNzc5Y2MxMGNhZTBiM2I4NjUwMDE2ZTMiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2018-08-03 02:17:14.629623');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-23 11:00:47
