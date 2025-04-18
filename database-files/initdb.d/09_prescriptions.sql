DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE Prescription (
    prescription_id INT PRIMARY KEY,
    checkup_id INT NOT NULL,
    medication_id INT NOT NULL,
    dosage TEXT,
    instructions TEXT
);

INSERT INTO Prescription (prescription_id, checkup_id, medication_id, dosage, instructions) VALUES
(1, 1, 1, '1 tablet daily', 'Administer with food at morning meal');
