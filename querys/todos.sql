CREATE TABLE IF NOT EXISTS todos (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    item VARCHAR(255) NOT NULL
);

INSERT INTO todos (item)
VALUES 
    ('Learn SQL3');

SELECT id, item FROM todos WHERE id = 'ff060e83-2db2-4566-b367-adac7998251b';

UPDATE todos
SET item = 'Learn Advanced SQL'
WHERE id = '8d76c476-33b1-4d84-bff0-a1f7a89ab72c';

DELETE FROM todos
WHERE id = '8d76c476-33b1-4d84-bff0-a1f7a89ab72c';

-- 1. 생성일시(created_at) 컬럼 추가 (기본값: 현재시간)
ALTER TABLE todos 
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- 2. 수정일시(updated_at) 컬럼 추가 (기본값: 현재시간)
ALTER TABLE todos 
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;


CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
   -- 1. 수정일시는 현재 시간으로 갱신
   NEW.updated_at = CURRENT_TIMESTAMP;
   
   -- 2. [핵심] 생성일시는 기존(OLD) 값을 그대로 덮어씌워 변경 방지
   NEW.created_at = OLD.created_at;
   
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;