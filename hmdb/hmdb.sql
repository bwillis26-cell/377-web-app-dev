-- The hMBD Schema
CREATE TABLE `hmdb`.`movie` (
  `mov_id` INT NOT NULL AUTO_INCREMENT,
  `mov_title` VARCHAR(100) NOT NULL,
  `mov_genre` VARCHAR(100) NOT NULL,
  `mov_rating` INT NULL,
  `mov_mpaa` VARCHAR(5) NULL,
  `mov_duration` INT NOT NULL,
  `mov_release_year` INT NULL,
  PRIMARY KEY (`mov_id`));
  
  DROP TABLE movie;
CREATE TABLE `hmdb`.`movie` (
  `mov_id` INT NOT NULL AUTO_INCREMENT,
  `mov_title` VARCHAR(100) NOT NULL,
  `mov_genre` VARCHAR(100) NULL,
  `mov_rating` DECIMAL(3,1) NULL,
  `mov_mpaa` VARCHAR(5) NULL,
  `mov_duration` INT NOT NULL,
  `mov_release_year` INT NULL,
  PRIMARY KEY (`mov_id`));
  
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Devil in Ohio',2022,356,5.9);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Blonde',2022,100,6.2);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('End of the Road,(II)', 2022,89,4.7);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Glass Onion: A Knives Out Mystery',2022,139,8.1);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Do Revenge',2022,118,6.4);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('I Came By',2022,110,6.1);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('No Limit',2022,118,5.8);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('The Lord of the Rings: The Fellowship of the Ring',2001,178,8.8);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Echoes',2022,132,5.9);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('The Gray Man',2022,122,6.5);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Me Time',2022,101,5);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Love in the Villa',2022,114,5.3);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Day Shift',2022,113,6.1);
INSERT INTO movie (mov_title, mov_release_year, mov_duration, mov_rating) VALUES ('Guillermo del Toro''s Pinocchio',2022,114,1.0);

select * from movie;
  

CREATE TABLE `hmdb`.`actor` (
  `act_id` INT NOT NULL AUTO_INCREMENT,
  `act_first_name` VARCHAR(100) NULL,
  `act_last_name` VARCHAR(100) NULL,
  `act_dob` DATETIME NULL,
  PRIMARY KEY (`act_id`));

CREATE TABLE `hmdb`.`movie_role` (
  `maj_id` INT NOT NULL AUTO_INCREMENT,
  `maj_mov_id` INT NOT NULL,
  `maj_act_id` INT NOT NULL,
  `maj_character` VARCHAR(200) NULL,
  PRIMARY KEY (`maj_id`));

-- Adding data to the hMDB schema
Truncate TABLE movie;

INSERT INTO movie (mov_title, mov_duration) VALUES ('Sinners', 120);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Wicked Part 2', 180);
INSERT INTO movie (mov_title, mov_duration) VALUES ('White Chicks', 140);
INSERT INTO movie (mov_title, mov_duration) VALUES ('A Glass Onion - Knives Out', 110);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Grown Ups', 135);
INSERT INTO movie (mov_title, mov_duration) VALUES ('Good Will Hunting', 114);

SELECT *
FROM movie;

Truncate TABLE actor;

INSERT INTO actor (act_first_name, act_last_name) VALUES ('Michael B.', 'Jordan');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Adam', 'Sandler');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Ariana', 'Grande');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Terry', 'Cruz');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Ben', 'Affleck');
INSERT INTO actor (act_first_name, act_last_name) VALUES ('Matt', 'Damon');

SELECT *
FROM actor;

Truncate TABLE movie_role;

INSERT INTO movie_role (maj_act_id, maj_mov_id, maj_character) VALUES (4, 3, 'Latrell Spencer');
INSERT INTO movie_role (maj_act_id, maj_mov_id, maj_character) VALUES (3, 2, 'Glinda');
INSERT INTO movie_role (maj_act_id, maj_mov_id, maj_character) VALUES (2, 5, 'Lenny Feder');

SELECT mov_title, maj_character
FROM movie_role JOIN movie ON maj_mov_id = mov_id
;

-- Update data within hMBD schema
SELECT *
FROM movie
;

-- Updates a single record
UPDATE movie
SET mov_mpaa = 'R', mov_release = '2004-6-23'
WHERE mov_id = 3;

-- Updates all records by omitting the WHERE clause
UPDATE movie
SET mov_rating = 0;

-- Update all records that don't have a value

UPDATE movie
SET mov_mpaa = 'N/a'
WHERE mov_mpaa IS NULL;

-- Delete data in hMDB schema

DELETE FROM movie
WHERE mov_id = 1
;

SELECT * FROM movie;

-- Delete doesn't reset ID, Truncate does reset ID