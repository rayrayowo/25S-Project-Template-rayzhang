DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE Checkup (
    checkup_id INT PRIMARY KEY,
    appointment_id INT NOT NULL,
    vet_id INT,
    diagnosis TEXT
);

INSERT INTO Checkup (checkup_id, appointment_id, vet_id, diagnosis) VALUES
(1, 1, 1, 'Healthy with slight gingivitis');
