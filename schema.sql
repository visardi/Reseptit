CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);



CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    cooking_time INTEGER,
    ingredients TEXT,
    instructions TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    value TEXT 
);


CREATE TABLE item_classes (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    title TEXT,
    value TEXT
);