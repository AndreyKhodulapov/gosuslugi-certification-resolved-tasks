**Существует структура базы данных. Какая команда на месте [...] позволит создать новую запись в таблице role?**

1 -- структура базы данных
2 CREATE TYPE permission AS ENUM (
3 'read',
4 'write',
5 'execute'
6 );
7
8 CREATE TABLE role (
9 permissions permission[]
10 );
11
12 -- запрос
13 INSERT INTO role (...) VALUES (... [...]);

V **array['read']::permission[]**
(permission.read)
"read"
('read') AS permission[]
array['read']


**Какое утверждение относительно генерируемых колонок является ложью?**

Значение генерируемой колонки нельзя установить вручную через INSERT или UPDATE
Генерируемые колонки бывают двух типов: stored и virtual
V **Генерируемые колонки могут ссылаться на другие генерируемые колонки.**
Выражение для вычисления генерируемой колонки не может содержать ссылки на большинство системных таблиц
Для stored генерируемых колонок значение сохраняется в таблице и не пересчитывается при каждом обращении


**Имеется следующая структура, представленная на изображении. Было решено во все существующие записи в таблице role добавить пермиссию 'read' так, чтобы не было дубликатов. Как этого достичь?**

1 CREATE TYPE permission AS ENUM ('read', 'write', 'execute', 'transfer', 'download');
2
3 CREATE TABLE role (
4 permissions permission[]
5 );

UPDATE role SET permissions = array_append(permissions, 'demoMode') WHERE permissions -> 'demoMode'
V **UPDATE role SET permissions = array_append(permissions, 'read') WHERE array_position(permissions, 'read') IS NULL**
UPDATE role SET permissions = array_append(permissions, "read") WHERE array_position(permissions, "read")
UPDATE TABLE role ALTER COLUMN permissions array_append(permissions, 'read')
UPDATE TABLE role ALTER COLUMN permissions distinct(array_append(permissions, "read"))


**Вы создаёте временную таблицу temp_data, объединяя результаты двух запросов с несовместимыми типами данных (например, integer и text).**

Таблица должна:

Автоматически принимать структуру первого запроса.
Сохранять дублирующиеся строки.
Какой подход нужно использовать?

1 CREATE TEMPORARY TABLE temp_data AS
2 <оператор> SELECT id, data FROM source1
3 <оператор> SELECT id, info FROM source2;

Использовать UNION, чтобы исключить дубликаты и автоматически привести типы данных
V **Использовать UNION ALL, чтобы сохранить дубликаты и автоматически привести типы данных**
Использовать UNION ALL, но предварительно создать временную таблицу с заданными типами данных
Использовать UNION, но предварительно привести типы данных в запросах
Использовать INTERSECT, чтобы сохранить только общие строки из обоих запросов


**У вас есть две связанные таблицы, где t2 использует значение из последовательности по умолчанию при обновлении ссылочной записи. Какие проблемы могут возникнуть при удалении записей из t1?**

1 CREATE SEQUENCE seq START WITH 1 INCREMENT BY 1;
2 CREATE TABLE t1 (
3 id SERIAL PRIMARY KEY
4 );
5 CREATE TABLE t2 (
6 id INTEGER DEFAULT nextval('seq') REFERENCES t1(id) ON DELETE SET DEFAULT
7 );

Операция удаления возможна только при явном использовании CASCADE, даже если задано ON DELETE SET DEFAULT
Удаление завершится успешно, но строки в t2, ссылающиеся на удалённые записи, станут недействительными, требуя дополнительной проверки
Транзакция с операцией удаления завершится с ошибкой, если в таблице t2 есть строки, ссылающиеся на удаляемую запись в t1
Удаление записи из t1 приведёт к изменению ссылающихся записей в t2 на значение по умолчанию из последовательности, что может нарушить логику приложения
V **Если nextval('seq') возвращает значение, отсутствующее в t1, операция удаления завершится с ошибкой**


**В таблице some_table содержится 1 миллион записей. На колонке id создан индекс B-Tree, а на колонке name — индекс GIN для полнотекстового поиска. Какой запрос оптимально использует индекс, если выборка данных составляет менее 0.1% от общего объёма?**

1 CREATE TABLE some_table (
2 id SERIAL,
3 name VARCHAR(30),
4 description TEXT
5 );
6 CREATE INDEX some_table_id_index ON some_table USING btree(id);
7 CREATE INDEX some_table_name_gin_index ON some_table USING gin(to_tsvector('english', name));

SELECT * FROM some_table WHERE to_tsvector('english', name) @@ to_tsquery('example');
SELECT * FROM some_table WHERE description ILIKE '%example%';
SELECT * FROM some_table WHERE id > 500000 AND id < 500010;
SELECT * FROM some_table WHERE name LIKE 'A%';
V **SELECT * FROM some_table WHERE id = 1000;**


**Таблица logs содержит миллиарды записей и используется для анализа активности. Наиболее частый запрос к таблице выбирает записи по колонке user_id и фильтрует их по диапазону значений в колонке event_time. Какой индекс лучше всего подходит для ускорения выполнения этого запроса?**

1 CREATE TABLE logs (
2 id SERIAL PRIMARY KEY,
3 user_id INTEGER NOT NULL,
4 event_time TIMESTAMP NOT NULL,
5 action TEXT
6 );
7 -- Часто используемый запрос
8 SELECT * FROM logs
9 WHERE user_id = 12345 AND event_time BETWEEN '2024-01-01' AND '2024-01-31';

V **CREATE INDEX logs_user_event_index ON logs(user_id, event_time);**
CREATE INDEX logs_event_index ON logs(event_time);
CREATE INDEX logs_event_user_index ON logs(event_time, user_id);
CREATE INDEX logs_user_event_hash ON logs USING hash(user_id, event_time);
CREATE INDEX logs_user_index ON logs(user_id);