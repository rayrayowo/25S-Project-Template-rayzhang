DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE PetEvent (
    event_id INT PRIMARY KEY,
    pet_id INT NOT NULL,
    event_type VARCHAR(50),
    description TEXT,
    event_date DATE
);

INSERT INTO PetEvent VALUES
(1, 1, 'Birthday', '3rd birthday celebration', '2025-03-16'),
(2, 2, 'Adoption Anniversary', '2nd year adopted', '2025-01-12');
