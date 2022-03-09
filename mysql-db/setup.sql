create database audio_service;
use audio_service;

CREATE TABLE song
(
id INTEGER AUTO_INCREMENT,
title TEXT,
song MEDIUMBLOB
PRIMARY KEY (id)
) COMMENT='this is the table storign the songs';