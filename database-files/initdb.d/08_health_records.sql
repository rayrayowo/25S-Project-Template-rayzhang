DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE HealthRecord (
    record_id INT PRIMARY KEY,
    profile_id INT NOT NULL,
    date DATE,
    weight DECIMAL(5,2),
    diet TEXT,
    notes TEXT
);

INSERT INTO HealthRecord (record_id, profile_id, date, weight, diet, notes) VALUES
(1, 1, '2025-04-01', 22.5, 'Grain-free kibble', 'Maintaining healthy weight');
