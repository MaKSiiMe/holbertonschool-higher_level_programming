-- 7. First add
-- inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

INSERT INTO first_table (id, name) VALUES (89, 'Best School');
