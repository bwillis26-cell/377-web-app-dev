CREATE TABLE `salty_canvas`.`reviews` (
  `rev_id` INT NOT NULL AUTO_INCREMENT,
  `rev_first_name` VARCHAR(100) NOT NULL,
  `rev_last_name` VARCHAR(100) NOT NULL,
  `rev_email` VARCHAR(100) NOT NULL,
  `rev_phone_number` VARCHAR(20) NOT NULL,
  `rev_type` VARCHAR(100) NOT NULL,
  `rev_time` INT NOT NULL,
  `rev_date` VARCHAR(100) NOT NULL,
  `rev_description` VARCHAR(100) NOT NULL,
  `rev_rating` INT NOT NULL,
  PRIMARY KEY (`rev_id`));
