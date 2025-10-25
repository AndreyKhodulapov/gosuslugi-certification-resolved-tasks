25.10 2025 HIT RATE = 50% SCORE = 11 из 15 - НЕЗАЧЕТ =(

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


**Существует таблица some_table.**

class	value
1	10
1	20
1	100
2	200
Запускаются две транзакции Т1 и Т2. Какой вид изолированности транзакции НЕ позволит исполнить commit?

1 -- T1
2 SELECT SUM(value) FROM mytab WHERE class = 1;
3 INSERT INTO some_table(class, value) VALUES (2, 30);
4 COMMIT;
5 -- T2
6 SELECT SUM(value) FROM mytab WHERE class = 2;
7 INSERT INTO some_table(class, value) VALUES (1, 300);
8 COMMIT;

read committed
V **serializable**
repeatable read
read uncommitted
snapshot


**В PostgreSQL вы создаёте индекс в транзакции над таблицей users. Во время выполнения этой транзакции другая транзакция пытается выполнить одну из следующих команд над той же таблицей. Какая команда выполнится без конфликтов?**

1 -- Первая транзакция
2 BEGIN;
3 CREATE INDEX idx_users_name ON users(name);
4 -- Вторая транзакция
5 <выбранная команда>;

VACUUM users;
SELECT * FROM users WHERE id = 1000 FOR UPDATE;
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
V **SELECT * FROM users;**
INSERT INTO users (name) VALUES ('Alice');


Какие утверждения о следующем запросе правдивы?

**1 CREATE MATERIALIZED VIEW some_view AS SELECT * FROM some_table ORDER BY id DESC WITH NO DATA;**

Возможна операция вставки в представление some_view
Чтение возможно сразу после создания представления some_view
V **Возможна операция REFRESH MATERIALIZED VIEW CONCURRENTLY some_view**
V **Так как использовалось выражение SELECT *, при модификации таблицы some_table изменятся и колонки в представлении some_view**
V **Для представления some_view можно создать индекс**


**У вас есть рабочая база данных с высокой нагрузкой и её копия. Вы хотите проанализировать производительность запроса, чтобы исключить влияние нагрузки на результаты анализа.**
**Какую команду следует использовать для тестирования на копии базы данных?**

Выполнить запрос несколько раз и взять среднее время выполнения.
pgbench для эмуляции нагрузки и затем использовать explain analyze
explain
V **explain analyze**
explain (analyze, buffers)


**В таблице orders содержится 1 миллион записей. На колонке customer_id есть индекс B-Tree. Вы выполняете следующий запрос с фильтрацией по customer_id и выбираете 90 % строк. Какой тип сканирования таблицы будет использован планировщиком PostgreSQL?**

1 CREATE TABLE orders (
2 order_id SERIAL PRIMARY KEY,
3 customer_id INTEGER NOT NULL,
4 order_date DATE,
5 total_amount NUMERIC
6 );
7 -- Индекс
8 CREATE INDEX idx_orders_customer_id ON orders (customer_id);
9 -- запрос
10 EXPLAIN SELECT * FROM orders WHERE customer_id < 900000;

V **seq scan**
index only scan
bitmap heap scan
bitmap index scan
index scan


**Существует таблица, представленная на изображении. В эту таблицу сохраняются данные, журналирующие некоторые действия. После очередного релиза частота вставки записей, где action = 'login', возросла в десять раз. Оперативно релиз починить не удается, но есть доступ к базе данных. Было решено временно не вставлять данные, где action = 'login', сохранив уже существующие записи.**

Как этого достичь?

1 CREATE TABLE action_log (
2 id SERIAL,
3 action VARCHAR,
4 description TEXT
5 );

Создать instead of trigger, запрещающий 'login'
Создать after insert trigger, удаляющий вставленную строку
Создать constraint на колонку action, запрещающий 'login'
Создать представление с условием: where action != 'login'
V **Создать before insert trigger, запрещающий 'login'**


**В PostgreSQL пользователь manuel должен получить полный доступ к таблице kinds.**

**Следующая команда выполнена другим пользователем. Какой будет результат выполнения команды, если исполняющий пользователь не является суперпользователем и не является владельцем таблицы?**

1 GRANT ALL PRIVILEGES ON kinds TO manuel;

manuel получит полный доступ к таблице kinds, включая возможность передавать права другим пользователям
V **Команда завершится ошибкой, так как исполнитель команды не является владельцем таблицы**
manuel получит все права, которые есть у исполнителя команды на таблицу kinds
Права на таблицу kinds будут изменены только для схемы, в которой она находится, но manuel доступ не получит
manuel получит доступ только на чтение таблицы kinds, если исполнитель команды обладает таким правом


**По мере продвижения бизнеса росло количество запросов к базе данных, а именно возросло в несколько раз количество запросов на запись при том же уровне запросов на чтение и повысилось требование к отказоустойчивости.**

**Какими методиками можно воспользоваться для поддержания работоспособности сервиса с учетом того, что запросов по ключу большинство?**

Репликация вместе с вертикальным шардированием
**Репликация вместе с горизонтальным шардированием**
Репликация
Вертикальное шардирование
Горизонтальное шардирование


**Выберите корректный вывод по следующему запросу:**

select date_trunc('quarter', created_at), avg(sales) 
from revenue 
group by 1

Группировка по дате покупки
Ошибка: нет ORDER BY
Только продажи после 1 января
Ошибка округления дат
V **Группировка по кварталам**


**В таблице customers есть поле interests типа text[]. В некоторых строках уже есть значения вроде '{music, travel}'. Вам нужно добавить тег 'sports' только тем клиентам, у кого его нет. Ваш коллега предложил код:**

update customers
set interests = interests || 'sports'
where not 'sports' = any(interests);

Какой из вариантов корректнее и безопаснее реализует задачу?

V **update customers set interests = array_append(interests, 'sports') where not 'sports' = any(interests)**
update customers set interests = array_prepend('sports', interests)
update customers set interests = interests || array['sports'] where interests != 'sports'
update customers set interests = 'sports' where interests @> array['sports']
update customers set interests = interests || 'sports' where interests is null


**Почему этот запрос может работать медленно?**

select id 
from orders 
where customer_id in (select id from blacklisted_customers)

SELECT нельзя использовать в подзапросе
V **Подзапрос не индексирован**
Нужно заменить на JOIN
WHERE нельзя использовать с IN
IN не работает с подзапросами


**Какое влияние окажет добавление индекса на поле created_at в следующем запросе?**
select * from logs where created_at >= now() - interval '1 day'

Уменьшит размер таблицы
Увеличит количество операций записи
Увеличит количество возвращаемых строк
V **Ускорит выборку при большом объеме данных**
Приведет к ошибке времени


**Дана транзакция T1:**

BEGIN;
SELECT balance FROM accounts WHERE id = 42;
-- здесь пауза, в это время другая транзакция обновляет balance
SELECT balance FROM accounts WHERE id = 42;
COMMIT;

Вторая транзакция в это время выполнила UPDATE accounts SET balance = 200 WHERE id = 42; и зафиксировала изменения между двумя SELECT.
Что увидит транзакция T1 при уровне изоляции Read Committed?


Запрос заблокируется до конца второй транзакции
Одно и то же значение balance
Ошибку сериализации
Только новое значение balance
V **Разные значения balance в двух SELECT**


**Что может быть проблемой при сравнении чисел типа float?**

select * from results where score = 0.1

float — устаревший тип
score нельзя сравнивать
PostgreSQL не поддерживает float
V **0.1 может быть представлен неточно в памяти**
= работает только с целыми


**Выберите верное утверждение о запросе:**

create materialized view some_view as select * from some_table order by id desc with no data

Чтение возможно сразу после создания представления some_view
Так как использовалось выражение select *, при модификации таблицы some_table изменятся и колонки в преставлении some_view
Возможна операция refresh materialized view concurrently some_view
V **Для представления some_view можно создать индекс**
Возможна операция вставки в представление some_view


**В системе при удалении пользователя:**
delete from users where id = 123;
наблюдается задержка. В таблице orders задано: foreign key (user_id) references users(id) on delete cascade
Какой способ поможет оценить влияние каскадного удаления на производительность?


Перевести таблицу orders в UNLOGGED
Использовать VACUUM FULL на обеих таблицах
Добавить ON DELETE SET NULL вместо CASCADE
V **Выполнить EXPLAIN ANALYZE delete from users where id = 123**
Временно удалить каскадный внешний ключ


**Вы хотите запретить изменение зарплаты сотрудника, если новое значение меньше текущего. Создан следующий триггер:**

create or replace function prevent_salary_drop() returns trigger as $$
begin
  if NEW.salary < OLD.salary then
    raise exception 'Salary cannot be decreased';
  end if;
  return NEW;
end;
\$$ language plpgsql;
create trigger trg_no_salary_drop
before update on employees
for each row
execute function prevent_salary_drop;

Как убедиться, что триггер сработает корректно?
Использовать VACUUM на таблице employees
Посмотреть в pg_stat_activity
Проверить, изменился ли тип поля salary
Выполнить EXPLAIN UPDATE
V **Попробовать обновить зарплату на меньшее значение и проверить, вызвана ли ошибка**


**Пользователь app_user выполняет запрос:**
select * from orders;
Но получает ошибку:
ERROR: permission denied for relation orders
Почему возникает ошибка, если orders — это представление, и права на неё явно выданы?


Пользователю не выдали роль pg_read_all_data
Ошибка вызвана отсутствием индексов
V **У пользователя нет прав на таблицы, используемые внутри представления**
Представления не требуют дополнительных прав
Представление создано без указания SECURITY DEFINER


**Вы хотите разделить таблицу users на два шарда по регионам. Какой шаг необходим при использовании PostgreSQL с Citus?**

Переместить все таблицы в новую базу
Настроить шард-каталог вручную
V **Выполнить select create_distributed_table('users', 'region')**
Установить расширение citus
Создать индекс по колонке region


**Вы работаете над аналитическим отчётом. Нужно сгруппировать данные по категориям товаров и посчитать среднюю цену в каждой категории. Ваш коллега предложил следующий код:**

1 select product, avg(price)
2 from goods
3 group by category

Однако этот код не выполняется. Какую доработку следует внести, чтобы получить корректный результат?

○ select product, avg(price) from goods

V **select category, avg(price) from goods group by category**

○ select category, avg(price) from goods group by price

○ select product, price from goods group by category

○ select avg(price) from goods group by price


**Почему данный запрос может вернуть NULL в поле email?**

1 select u.id, e.email  
2 from users u  
3 left join emails e on u.id = e.user_id

V **Не все пользователи имеют записи в emails**

○ LEFT JOIN не работает без подзапроса

○ Связь должна быть один к одному

○ Нельзя использовать JOIN без GROUP BY

○ Поле email не существует


**Почему в PostgreSQL по умолчанию индекс по полю deleted_at не помогает ускорить запрос:**

select * from users where deleted_at is null

○ IS NULL нельзя использовать в WHERE

○ Индекс работает только с числовыми полями

○ deleted_at нужно делать PRIMARY KEY

V **B-Tree индекс не включает NULL-значения**

○ NULL в PostgreSQL обрабатывается как 0


**Вы проектируете процедуру issue_payment(user_id_int, amount numeric(5,2)), которая вносит запись в таблицу payouts(amount numeric(5,2)).**

При высоких нагрузках в журнале стали появляться ошибки: numeric field overflow. Анализ показал, что иногда в amount передаётся 998,999.

Какая доработка обеспечит устойчивое поведение при сохранении точности и отказоустойчивости?

○ Разрешить округление через set extra_float_digits = 0

○ Перед вызовом процедуры фильтровать значения на клиенте

○ Добавить в процедуру amount := round(test(amount, 999,99), 2) и логировать изменения

○ Обернуть INSERT в BEGIN ... EXCEPTION WHEN OTHERS THEN RAISE NOTICE

V **Изменить тип поля в таблице на numeric(7,4)**


**Что произойдёт при попытке вставить данные в представление?**

insert into view_active_users (name, email) values ('Anna', 'a@example.com');


○ Произойдёт дублирование записей

○ Представление перезапишется

○ Запрос выполнится и обновит базовую таблицу

V I**NSERT будет транслирован в базу через RULE**

○ Ошибка: представление только для чтения


**Какой риск возникает, если пользователь создаёт выраженный индекс на поле, к которому у него нет прав?**

CREATE INDEX idx_lower_email ON users (lower(email));

○ Индекс создается, но выдаст ошибку при обращении

○ PostgreSQL создаст индекс без проверки прав

○ Индекс будет создан, но использоваться не сможет

○ Индекс создается, но выдаст ошибку при использовании функции

V **Запрос завершится ошибкой из-за отсутствия доступа к полю**


**Какой параметр нужно включить в postgresql.conf на реплике, чтобы разрешить подключение в режиме только чтения?**

V **hot_standby = on**

○ slave_read = enable

○ standby_node = on

○ read_only = true

○ stream_only = true