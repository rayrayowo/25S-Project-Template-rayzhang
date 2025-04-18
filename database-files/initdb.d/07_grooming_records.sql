DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE GroomingRecord (
    record_id INT PRIMARY KEY,
    appointment_id INT NOT NULL,
    groomer_id INT,
    services TEXT,
    notes TEXT
);

INSERT INTO GroomingRecord (record_id, appointment_id, groomer_id, services, notes) VALUES
(1, 2, 1, 'Bath and nail trimming', 'Mild skin irritation observed');
