--  a script that creates the table unique_id
CREATE  table IF NOT EXISTS unique_id(
    id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
