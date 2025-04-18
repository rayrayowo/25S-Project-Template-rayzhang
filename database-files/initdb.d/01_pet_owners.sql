DROP DATABASE IF EXISTS pethub;
CREATE DATABASE pethub;
use pethub;

-- Drop tables if they exist
DROP TABLE IF EXISTS PetProfile;
DROP TABLE IF EXISTS Pet;
DROP TABLE IF EXISTS PetOwner;

-- PetOwner table
CREATE TABLE PetOwner (
    owner_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(100),
    address TEXT
);

-- Pet table
CREATE TABLE Pet (
    pet_id INT PRIMARY KEY,
    owner_id INT NOT NULL,
    name VARCHAR(100),
    species VARCHAR(100),
    breed VARCHAR(50),
    age DECIMAL(5,2),
    gender VARCHAR(10),
    FOREIGN KEY (owner_id) REFERENCES PetOwner(owner_id)
);

-- PetProfile table
CREATE TABLE PetProfile (
    profile_id INT PRIMARY KEY,
    pet_id INT NOT NULL,
    notes TEXT,
    last_checkup_date DATE,
    FOREIGN KEY (pet_id) REFERENCES Pet(pet_id)
);

-- Insert sample owners
INSERT INTO PetOwner VALUES (1, 'Alice', 'alice@example.com', '123-456-7890', '123 Main St');
INSERT INTO PetOwner VALUES (2, 'Bob', 'bob@example.com', '987-654-3210', '456 Elm St');

-- Insert sample pets
INSERT INTO Pet VALUES (1, 1, 'Buddy', 'Dog', 'Golden Retriever', 3, 'Male');
INSERT INTO Pet VALUES (2, 2, 'Milo', 'Cat', 'Siamese', 2, 'Female');

-- Insert sample profiles
INSERT INTO PetProfile VALUES (1, 1, 'Healthy', '2025-03-10');
INSERT INTO PetProfile VALUES (2, 2, 'Needs more exercise', '2025-01-20');
