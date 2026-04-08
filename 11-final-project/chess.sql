CREATE DATABASE `chess` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `chess`.`games` (
  `gam_id` INT NOT NULL AUTO_INCREMENT,
  `gam_board` VARCHAR(200) NOT NULL,
  `gam_p1_time` INT NULL,
  `gam_p2_time` INT NULL,
  `gam_turn` INT NOT NULL,
  `gam_start_time` INT NOT NULL,
  PRIMARY KEY (`gam_id`));