DROP TABLE IF EXISTS simulations;
DROP TABLE IF EXISTS simulation_histories;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS situations;

CREATE TABLE categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE simulations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT UNIQUE NOT NULL,
  name TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL,
  category_id INTEGER NOT NULL,
  value FLOAT NOT NULL,
  min_value FLOAT NOT NULL,
  max_value FLOAT NOT NULL,
  FOREIGN KEY (category_id) REFERENCES categories (id)
);

CREATE TABLE simulation_histories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  simulation_id INTEGER NOT NULL,
  value FLOAT NOT NULL,
  FOREIGN KEY (simulation_id) REFERENCES simulation (id)
);

CREATE TABLE situations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT UNIQUE NOT NULL,
  name TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL
);
