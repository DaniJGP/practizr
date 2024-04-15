DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

DROP TABLE IF EXISTS template;

CREATE TABLE template (
    id INTEGER PRIMARY KEY,
    temp_name TEXT,
    temp_duration INTEGER NOT NULL,
    item_n INTEGER NOT NULL,
    items_json TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
);

DROP TABLE IF EXISTS item;

CREATE TABLE item (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    area TEXT NOT NULL,
    item TEXT NOT NULL,
    note TEXT,
    FOREIGN KEY (user_id) REFERENCES user (id)
);
