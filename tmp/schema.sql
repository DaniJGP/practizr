/*-- TODO: User registration info
CREATE TABLE IF NOT EXISTS user (
    id INTEGER NOT NULL,
    username TEXT UNIQUE NOT NULL,
    pwd_hash TEXT NOT NULL,
    email TEXT NOT NULL)

-- User templates
CREATE TABLE IF NOT EXISTS template (
    temp_id INTEGER NOT NULL,
    temp_name TEXT,
    temp_duration INTEGER NOT NULL,
    item_n INTEGER NOT NULL,
    items_json TEXT NOT NULL,
    PRIMARY KEY (temp_id)
)*/

-- User custom items
CREATE TABLE IF NOT EXISTS item (
--    user_id INTEGER NOT NULL,
    area TEXT NOT NULL,
    item TEXT NOT NULL,
    note TEXT)
