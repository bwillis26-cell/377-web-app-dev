-- Finds Criminal 

SELECT p.name, bank.person_id, p.license_plate, i.transcript, atm.transaction_type, c.year, c.month, c.day, atm.amount
FROM crime_scene_reports c JOIN interviews i ON c.year = i.year
AND c.month = i.month
AND c.day = i.day
JOIN atm_transactions atm ON atm.year = c.year
AND atm.month = c.month
AND atm.day = c.day
JOIN bank_accounts bank ON bank.account_number = atm.account_number
JOIN bakery_security_logs bsl ON bsl.year = c.year
AND bsl.month = c.month
AND bsl.day = c.day
JOIN people p ON p.license_plate = bsl.license_plate
AND p.id = bank.person_id
JOIN phone_calls phone ON phone.caller = p.phone_number
JOIN flights fly ON fly.day = 29
JOIN passengers pass ON fly.id = pass.flight_id
AND pass.passport_number = p.passport_number
WHERE description LIKE '%CS50%'
AND i.transcript LIKE '%bakery%'
AND fly.id = 36
AND atm_location = 'Leggett Street'
AND atm.transaction_type = 'withdraw'
AND bsl.hour = 10
AND bsl.minute BETWEEN 15 AND 25
AND bsl.activity = 'exit'
AND phone.duration < 60
-- ORDER BY fly.hour
;
-- Finds all transactions on the leggett street atm
SELECT *
FROM atm_transactions
WHERE atm_location = 'Leggett Street'
;
-- Finds all cars who left between the time
SELECT *
FROM bakery_security_logs bake JOIN people p ON bake.license_plate = p.license_plate
WHERE bake.day = 28
AND bake.hour = 10
AND bake.minute BETWEEN 15 AND 25;

SELECT *
FROM flights
WHERE day = 29
ORDER BY hour
;

SELECT *
FROM bakery_security_logs

;

SELECT *
FROM people;

-- Also finds bruce
SELECT * 
FROM people p JOIN passengers pass ON pass.passport_number = p.passport_number
JOIN flights fly ON pass.flight_id = fly.id
WHERE pass.passport_number = 5773159633
;
-- Finds list of passengers on the flight
SELECT *
FROM flights
JOIN passengers ON id = flight_id
WHERE day = 29
AND id = 36
ORDER BY hour
;
-- Finds accomplice
SELECT *
FROM phone_calls JOIN people ON receiver = phone_number
WHERE caller = '(367) 555-5533'
AND duration < 60
AND day = 28;
-- Finds city
SELECT * 
FROM airports
WHERE id = 4;

-- 686048	Bruce	(367) 555-5533	5773159633	94KL13X Original Criminal
-- 864400	Robin	(375) 555-8161	        	4V16VO0 Accomplice
-- New York City
