CREATE DATABASE IF NOT EXISTS epytodo;

USE epytodo

CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (user_id)
)
