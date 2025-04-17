DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;


CREATE TABLE Community (
    post_id INT PRIMARY KEY,
    pet_id INT,
    content TEXT,
    post_date DATE,
    likes INT
);

INSERT INTO Community VALUES
(1, 1, 'Buddy learned a new trick today!', '2025-04-08', 23),
(2, 2, 'Milo just had her first grooming session!', '2025-04-09', 15);
