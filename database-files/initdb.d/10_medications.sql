DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE Medication (
    medication_id INT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

INSERT INTO Medication (medication_id, name, description) VALUES
(1, 'Amoxicillin', 'Antibiotic used to treat bacterial infections');
