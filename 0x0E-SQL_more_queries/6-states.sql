-- Creates the database hbtn_0d_usa and the table states
-- CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--
-- USE hbtn_0d_usa;
--
-- CREATE TABLE IF NOT EXISTS states (
--     id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
--     name VARCHAR(256) NOT NULL,
-- );

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256));
