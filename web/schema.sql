DROP TABLE IF EXISTS simulations;
DROP TABLE IF EXISTS simulation_histories;
DROP TABLE IF EXISTS situations;
DROP TABLE IF EXISTS situation_histories;
DROP TABLE IF EXISTS policies;
DROP TABLE IF EXISTS policy_histories;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS group_histories;

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

CREATE TABLE policies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT UNIQUE NOT NULL,
  is_active BOOL NOT NULL,
  slider_value TEXT NOT NULL,
  value FLOAT NOT NULL
);

CREATE TABLE policy_histories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  policy_id INTEGER NOT NULL,
  value FLOAT NOT NULL,
  FOREIGN KEY (policy_id) REFERENCES policies (id)
);

CREATE TABLE groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT UNIQUE NOT NULL
);

CREATE TABLE group_histories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_id INTEGER NOT NULL,
  mood_value FLOAT NOT NULL,
  freq_value FLOAT NOT NULL,
  FOREIGN KEY (group_id) REFERENCES groups (id)
);