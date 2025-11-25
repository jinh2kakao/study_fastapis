CREATE TABLE IF NOT EXISTS todos (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    item VARCHAR(255) NOT NULL
);

INSERT INTO todos (item)
VALUES 
    ('Learn SQL3');

SELECT id, item FROM todos;

UPDATE todos
SET item = 'Learn Advanced SQL'
WHERE id = '8d76c476-33b1-4d84-bff0-a1f7a89ab72c';

DELETE FROM todos
WHERE id = '8d76c476-33b1-4d84-bff0-a1f7a89ab72c';