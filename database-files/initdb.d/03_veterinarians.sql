DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

DROP TABLE IF EXISTS Veterinarian;

CREATE TABLE Veterinarian (
    vet_id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    email VARCHAR(100),
    phone VARCHAR(20),
    graduate_school VARCHAR(100),
    working_hours VARCHAR(100),
    clinic_id INT
);

INSERT INTO Veterinarian VALUES (1, 'Dr. Max Vet', 'Male', 'max@example.com', '555-666-7777', 'Harvard Vet School', '9AM-5PM', 1);
