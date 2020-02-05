CREATE SEQUENCE users_name_id_seq;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer NOT NULL DEFAULT nextval('users_name_id_seq')
  username Varchar NOT NULL,
  password Varchar NOT NULL
);
ALTER SEQUENCE users_name_id_seq
OWNED BY users.id;
INSERT INTO users(id, username, password) VALUES(1, 'oplog', 'oplog');
INSERT INTO users(id, username, password) VALUES(2, 'agit', 'agit');