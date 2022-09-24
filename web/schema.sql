DROP TABLE IF EXISTS simulations;
DROP TABLE IF EXISTS simulation_histories;
DROP TABLE IF EXISTS situations;
DROP TABLE IF EXISTS situation_histories;

CREATE TABLE simulations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT UNIQUE NOT NULL,
  value FLOAT NOT NULL
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
  is_active BOOL NOT NULL
);

CREATE TABLE situation_histories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  situation_id INTEGER NOT NULL,
  value FLOAT NOT NULL,
  FOREIGN KEY (situation_id) REFERENCES situation (id)
);