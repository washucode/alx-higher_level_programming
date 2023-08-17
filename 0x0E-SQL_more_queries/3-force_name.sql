-- Write a script that creates the table 
-- force_name on your MySQL server.
CREATE  table IF NOT EXISTS force_name(
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);