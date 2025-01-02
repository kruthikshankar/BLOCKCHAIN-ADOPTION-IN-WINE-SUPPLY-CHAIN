/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - bcc
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`bcc` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bcc`;

/*Table structure for table `consumer` */

DROP TABLE IF EXISTS `consumer`;

CREATE TABLE `consumer` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `consumer` */

insert  into `consumer`(`id`,`username`,`password`,`email`,`address`) values (1,'munna','munna','munna@gmail.com','hyd');

/*Table structure for table `distb` */

DROP TABLE IF EXISTS `distb`;

CREATE TABLE `distb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `distb` */

insert  into `distb`(`id`,`username`,`password`,`email`,`address`) values (1,'chintu','chintu','chintu@gmail.com','hyd');

/*Table structure for table `owner` */

DROP TABLE IF EXISTS `owner`;

CREATE TABLE `owner` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `owner` */

insert  into `owner`(`id`,`username`,`password`,`email`,`address`) values (1,'chotu','chotu','moulalicce225@gmail.com','hyd');

/*Table structure for table `producer` */

DROP TABLE IF EXISTS `producer`;

CREATE TABLE `producer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `producer` */

insert  into `producer`(`id`,`username`,`password`,`email`,`address`) values (1,'chinni','chinni','chinni@gmail.com','hyd');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `pid` varchar(100) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `producer` varchar(100) DEFAULT NULL,
  `bc` varchar(100) DEFAULT NULL,
  `distb` varchar(100) DEFAULT NULL,
  `bc1` varchar(100) DEFAULT NULL,
  `re` varchar(100) DEFAULT NULL,
  `bc2` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`pid`,`pname`,`price`,`image`,`producer`,`bc`,`distb`,`bc1`,`re`,`bc2`) values ('100','samsung','10000','ss.jpg','chinni','d091fd30ee4e8a3151d1f15c36fd6725a1532f209fcf423a36d8b812b9ce60e2','chintu','af068051fc6aca139fbdba04c758b3fc87d27025607e488f5eb708da9d2dd4b1','chinna','ad1f48aac65c771124734451deb1735937845a6b4fc208ffb08052270d8b272c');

/*Table structure for table `purchase` */

DROP TABLE IF EXISTS `purchase`;

CREATE TABLE `purchase` (
  `pid` varchar(100) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `key2` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `purchase` */

insert  into `purchase`(`pid`,`pname`,`price`,`image`,`username`,`key2`) values ('100','samsung','10000','ss.jpg','munna','ad2ad478720768fe3ad0b147097ef857fd917b06bf9bcca3687b4df1532ab4a8');

/*Table structure for table `re` */

DROP TABLE IF EXISTS `re`;

CREATE TABLE `re` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `re` */

insert  into `re`(`id`,`username`,`password`,`email`,`address`) values (1,'chinna','chinna','chinn@gmail.com','hyd');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
