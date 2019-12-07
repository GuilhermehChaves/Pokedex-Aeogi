CREATE DATABASE pokedex;

USE pokedex;

CREATE TABLE `pokemon` (
  `pokedex_number` int PRIMARY KEY,
  `name` varchar(30),
  `attack` int,
  `classfication` varchar(50),
  `defense` int,
  `height_m` float,
  `hp` int,
  `speed` int,
  `weight_kg` float,
  `is_legendary` tinyint,
  `generation` tinyint
);

CREATE TABLE `type` (
  `id` int PRIMARY KEY AUTO_INCREMENT ,
  `name` varchar(30) UNIQUE
);

CREATE TABLE `pokemon_type` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `pokemon_number` int,
  `type_id` int,
  FOREIGN KEY (`pokemon_number`) REFERENCES `pokemon`(`pokedex_number`),
  FOREIGN KEY (`type_id`) REFERENCES `type`(`id`)
);

CREATE TABLE `abilities` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(30)
);

CREATE TABLE `pokemon_ability` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `pokemon_number` int,
  `ability_id` int,
  FOREIGN KEY (`pokemon_number`) REFERENCES `pokemon`(`pokedex_number`),
  FOREIGN KEY (`ability_id`) REFERENCES `abilities`(`id`)
);
