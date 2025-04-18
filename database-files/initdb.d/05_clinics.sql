DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE IF NOT EXISTS Clinic (
    clinic_id INT PRIMARY KEY,
    name VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100)
);

INSERT INTO Clinic VALUES
(1, 'Happy Paws Clinic', '789 Animal Rd', '555-9999', 'info@happypaws.com');