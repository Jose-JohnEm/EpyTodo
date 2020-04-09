CREATE DATABASE IF NOT EXISTS epytodo;

USE epytodo

CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (user_id)
) AUTO_INCREMENT=1;

CREATE TABLE task (
    task_id INT NOT NULL AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    begin varchar(255) DEFAULT CURRENT_DATE(),
    end varchar(255) DEFAULT '',
    status INT DEFAULT 1,
    PRIMARY KEY (task_id)
) AUTO_INCREMENT=1;

CREATE TABLE user_has_task (
    fk_user_id INT NOT NULL,
    fk_task_id INT NOT NULL
);
