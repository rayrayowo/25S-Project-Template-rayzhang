DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

CREATE TABLE IF NOT EXISTS Appointment (
    appointment_id INT PRIMARY KEY,
    pet_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    appointment_type VARCHAR(50),
    status VARCHAR(20),
    created_at TIMESTAMP,
    FOREIGN KEY (pet_id) REFERENCES Pet(pet_id)
);

INSERT INTO Appointment VALUES
(1, 1, '2025-04-20', '10:00:00', 'Vet Checkup', 'Scheduled', '2025-04-10 09:00:00'),
(2, 2, '2025-04-22', '14:30:00', 'Grooming', 'Scheduled', '2025-04-11 10:00:00');