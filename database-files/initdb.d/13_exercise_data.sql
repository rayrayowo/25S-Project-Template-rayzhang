DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE ExerciseData (
    record_id INT PRIMARY KEY,
    pet_id INT NOT NULL,
    date DATE,
    duration_minutes INT,
    activity_type VARCHAR(50),
    notes TEXT
);

INSERT INTO ExerciseData VALUES
(1, 1, '2025-04-10', 45, 'Walking', 'Very active and responsive'),
(2, 2, '2025-04-11', 30, 'Fetch', 'Short bursts, good stamina');
