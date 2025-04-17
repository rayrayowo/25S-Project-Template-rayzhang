DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

DROP TABLE IF EXISTS PetGroomer;

CREATE TABLE PetGroomer (
    groomer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    salon_name VARCHAR(100)
);

INSERT INTO PetGroomer VALUES (1, 'Sally Groom', 'sally@example.com', '111-222-3333', 'Happy Pets Salon');
