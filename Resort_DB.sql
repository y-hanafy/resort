-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- ------------------------------------------------------
-- Server version	5.6.50-log

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
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `Feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `First_name` varchar(255) NOT NULL,
  `Last_name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Feedback` varchar(10000) NOT NULL,
  PRIMARY KEY (`Feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */
;
INSERT INTO `feedback`
VALUES (
    21,
    5,
    'Jessica',
    'Green',
    'ddgdsg@wf.com',
    '5 stars all around! The checkin staff were wonderful and informative. After much research,we decided to stay at this hotel as it was perfect access to NY and the VIEWS sold me!\r\nWe arrived before check in and the staff checked us in. They offered us a map of how to get to NYC. The staff was helpful and explained how to navigate thru NY. I appreciated the time they took to help us.\r\nThe hotel is perfectly located across the Hudson River and the Manhattan sky line was gorgeous. Our room had a perfect view and we enjoyed the balcony views. \r\nThis hotel is located next to the ferry which leaves you near the Twin Tower memorial. The subway is close by and there are shops close by.\r\nSince we drove, we did have an overnight fee but it was worth it since they have your car ready if you are running in and out of hotel. The valet staff were great. We also drove into NY and the drive was quick and very accessible from the hotel. \r\nI enjoyed the location of this hotel as it was close to a mall and lots of restaurants both driving and walking distance in Jersey City. \r\nWe will definitely be back. So glad we stayed here. We felt safe during our stay. Rooms and hotel were clean.'
  ),
(
    22,
    5,
    'Melissa',
    'Garcia',
    'trhdfhd@efe.com',
    'I was not a guest so my review will not outline anything regarding a hotel stay.\r\nMy experience was with regards to the rooftop bar.\r\nIn a nutshell, if you can squeeze in a visit while the good weather is still here----do it.\r\n\r\nIt was suggested we check it out and upon getting off the elevator, I saw a huge indoor seating area and the bar from afar, but was anxious to hit the outside section.\r\n\r\nCocktails were very reasonable at $13 with clever creations such as The Path to My Heart. This hotel is a 5 minute walk from Exchange Place stop on the Path train (just one stop from WTC Path ).\r\n\r\nThe outside space had some nice seating configurations and included a fire pit (allowing it to feel hotter than the already sizzling 90 degree temperature).\r\n\r\nBut it was the waterfront, rooftop view that stole my heart. Looking at the beautiful Manhattan skyline from a different perspective was well worth the trip.\r\n\r\nI actually felt like a hotel guest on this visit.\r\nDo check it out.'
  ),
(
    23,
    5,
    'Mary',
    ' Smith',
    'fdgf@ef.com',
    'I was part of a conference that was being held here. The rooms were nice and comfortable.  They did not have microwaves and there was no room service menu in my room. The meeting rooms were nice as were the food choice offerings. The view of NYC is amazing. The boardwalk area surrounding the hotel is also nice. The PATH is right next door and you are at the Freedom Tower in less than 20 minutes. I will be staying here again'
  ),
(
    24,
    5,
    'Robert',
    'Johnson',
    'dsrgsd@efef.com',
    'Checked in yesterday for a night. Amazing hotel right on the Hudson. Gorgeous clean rooms. The staff was amazing as well. A special thank you to Amentari at the front desk for making sure our room was prepared early and making sure that everything was perfect for our stay.'
  ),
(
    25,
    15,
    'John',
    'Smith',
    'js@js.com',
    'I was part of a conference that was being held here. The rooms were nice and comfortable. They did not have microwaves and there was no room service menu in my room. The meeting rooms were nice as were the food choice offerings. The view of NYC is amazing. The boardwalk area surrounding the hotel is also nice. The PATH is right next door and you are at the Freedom Tower in less than 20 minutes. I will be staying here again'
  ),
(
    26,
    15,
    'John',
    'Smith',
    'js@js.com',
    'Checked in yesterday for a night. Amazing hotel right on the Hudson. Gorgeous clean rooms. The staff was amazing as well. A special thank you to Amentari at the front desk for making sure our room was prepared early and making sure that everything was perfect for our stay.'
  );
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */
;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations` (
  `Reservation_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `First_name` varchar(255) NOT NULL,
  `Last_name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Room_type` varchar(255) NOT NULL,
  `Room_id` int(11) NOT NULL,
  `Check_in_date` date NOT NULL,
  `Check_out_date` date NOT NULL,
  `Guests` int(11) NOT NULL,
  `Reservation_date` date NOT NULL,
  `Room_price` int(11) NOT NULL,
  `Reservation_price` int(11) NOT NULL,
  PRIMARY KEY (`Reservation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=314 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Role` varchar(255) NOT NULL,
  `First_name` varchar(255) NOT NULL,
  `Last_name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin','admin','admin@admin.com', '$2a$10$aA5es6va7kmAYYW787rLDuy4xtOV/p1PL5RZkkAG/8qWzct.n0RFe');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-23 16:37:23
