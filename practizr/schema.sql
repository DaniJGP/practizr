     DROP TABLE IF EXISTS user;

   CREATE TABLE user (
          id INTEGER PRIMARY KEY,
          username TEXT UNIQUE NOT NULL,
          password_hash TEXT NOT NULL
          );

     DROP TABLE IF EXISTS template;

   CREATE TABLE routine (
          id INTEGER PRIMARY KEY,
          temp_name TEXT,
          user_id INTEGER NOT NULL,
          FOREIGN KEY (user_id) REFERENCES user (id)
          );

   CREATE TABLE routine_item (
          id INTEGER PRIMARY KEY,
          routine_id INTEGER,
          duration INTEGER,
          area TEXT NOT NULL,
          item TEXT NOT NULL,
          note TEXT,
          )
     DROP TABLE IF EXISTS area_item;

   CREATE TABLE area_item (
          id INTEGER PRIMARY KEY,
          area TEXT NOT NULL,
          item TEXT NOT NULL
          );