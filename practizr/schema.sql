     DROP TABLE IF EXISTS user;

   CREATE TABLE user (
          id INTEGER PRIMARY KEY,
          username TEXT UNIQUE NOT NULL,
          password_hash TEXT NOT NULL
          );

     DROP TABLE IF EXISTS routine;

   CREATE TABLE routine (
          id INTEGER PRIMARY KEY,
          temp_name TEXT,
          user_id INTEGER NOT NULL,
          FOREIGN KEY (user_id) REFERENCES user (id)
          );

     DROP TABLE IF EXISTS routine_item;

   CREATE TABLE routine_item (
          id INTEGER PRIMARY KEY,
          routine_id INTEGER,
          duration INTEGER,
          area TEXT NOT NULL,
          item TEXT NOT NULL,
          note TEXT
          );

     DROP TABLE IF EXISTS area;

   CREATE TABLE area (
          id INTEGER PRIMARY KEY,
          area_name TEXT UNIQUE NOT NULL
          );

   INSERT INTO area (area_name)
   VALUES ("Technique"),
          ("Music Theory"),
          ("Repertoire"),
          ("Transcription"),
          ("Ear Training"),
          ("Improvisation"),
          ("Other");