4.10 2025 HIT RATE = 20% SCORE = 11 из 15

**Что произойдет, если при использовании GROUP BY указаны колонки, но не указаны агрегирующие функции?**

запрос вернет уникальные значения по всем колонкам, которые прописаны в GROUP BY, а остальные колонки проигнорирует
запрос вернет уникальные значения по всем колонкам, которые прописаны в SELECT, а остальные колонки проигнорирует
запрос вернет уникальные значения по колонкам, которые прописаны и в GROUP BY, и в SELECT
V **запрос вернет ошибку.**
запрос вернет уникальные значения по всем колонкам из таблицы


**Что произойдет, если при использовании GROUP BY применить агрегирующую функцию MAX к колонке, содержащей строковые значения?**

для каждого уникального значения в GROUP BY вернется NULL
V **для каждого уникального значения в GROUP BY вернется последняя строка по алфавиту**
для каждого уникального значения в GROUP BY вернется самая длинная строка
для каждого уникального значения в GROUP BY вернется первая строка по алфавиту
ошибка


**Есть две таблицы из одной колонки, в них содержатся NULL-значения. В левой таблице пять значений NULL, в правой семь. Сколько строк вернется с NULL при выполнении различных типов соединений, если соединение происходит по единственной колонке, содержащей NULL?**

V **INNER-0 , LEFT-5 , RIGHT-7 , FULL-12**
INNER-5 , LEFT-5 , RIGHT-7 , FULL-7
INNER-5 , LEFT-5 , RIGHT-7 , FULL-12
INNER-0 , LEFT-5 , RIGHT-5 , FULL-7
INNER-5 , LEFT-35 , RIGHT-35 , FULL-27


**Какой будет результат, если значение в колонке таблицы подходит под несколько условий в CASE?**

вернется NULL
вернутся все значения THEN, подходящие под условия
V **вернется значение THEN первого условия**
ошибка
вернется значение THEN последнего условия


**В этом SQL-запросе допущено несколько ошибок (в данных при этом ошибок нет). Выберите вариант со всеми перечисленными ошибками:**

with base as (
select
from payments
where exists(select payment_system_id from payment_systems )
)
select
from base
where amount > ( select countries , count(distinct payment_types ) from table_countries group by 1 )
left join (
select
from ( select id from users union select id from employees )
) on base.id = users.id
group by 1,2
right join ( select payment_id , old_payment_id from payments_history ) old on base.id = old.id
having sum(revenue ) > ( select min(amount ) from revenue )

JOIN происходит по полю, которого нет в подзапросе; EXISTS нельзя применять в CTE; для всех подзапросов нет алиаса
подзапросы не могут быть больше первого уровня вложенности; подзапрос нельзя писать в HAVING; один из подзапросов в WHERE возвращает две колонки
подзапрос нельзя писать в HAVING; для всех подзапросов нет алиаса; JOIN происходит по полю, которого нет в подзапросе
один из подзапросов в WHERE возвращает две колонки; подзапрос нельзя указывать в WHERE: для одного подзапроса нет алиаса
V **один из подзапросов в WHERE возвращает две колонки; для двух подзапросов нет алиаса; JOIN происходит по полю, которого нет в подзапросе**


**У вас есть уже существующее материальное представление test_view. Вы хотите добавить в него новый столбец num_purchases. Как сделать это синтаксически верно?**

delete materialized view test_view ; create alter materialized view test_view add column num
replace alter materialized view test_view as select user_id , min(dt ) as first_payed , sum(pr
delete materialized view test_view ; create or replace materialized_view test_view as select
V **drop materialized view; create materialized view as select user_id , min(dt ) as first_payed ,**
drop materialized view; create view test_view as select user_id , min(dt ) as first_payed , sur

**Укажите запрос, который выберет все фильмы, связанные со словами bad, good, angry. В названиях фильмов могут содержаться эти слова в разном виде, например в разных регистрах (Badboys) или в измененной форме (goodspeed):**

select movie_name from movies where lower(movie_name ) like 'bad ' or lower ( movie_name ) like
select movie_name from movies where movie_name like "Good " or movie_name like ' % Bad or m
V **select movie_name from movies where lower(movie_name) like '%bad%' or lower(movie_name) like '%good%' or lower(movie_name) like '%angry%**
select movie_name from movies where movie_name like " Sbad % or movie_name like ' % angry % or
select movie_name from movies where movie_name in ( ' bad ' , ' angry ' , ' good ' )


**В данных есть особенность: в поле amount могут находиться целые и дробные данные с указанием валюты, например 1.43 EUR , 250 , 37.18 , 893 RUB.**

Также есть SQL-запрос, который написан аналитиком и рассчитывает сумму одобренных транзакций по месяцам 2023 года.

Запрос:

select
to_char(transaction_date::date , "YYYY-MM ) as month ,
sum(cast ( regexp_replace(amount , '[^0-9.]', '','g' ) as numeric ) ) as total_approved_amount
from transactions
where
status = 'approved'
and date_trunc ( 'YEAR' , transaction_date::date ) = '2023'
group by month
order by month

Выберите вариант, где для каждого запроса указана ошибка, из-за которой запрос либо не сработает, либо вернет неверные значения:

regexp_replace возвращает некорректное значение для CAST, а date_trunc('YEAR' , transaction_date::date ) = "2023" записано с ошибкой
V **regexp_replace искажает числовые значения, а group by month некорректно сгруппирует данные**
to_char(transaction_date , 'YYYY-MM" ) не поддерживает преобразование дат, а sum ( ... ) не суммирует значения типа numeric
cast(regexp_replace ( ... ) ) as numeric нельзя применять в агрегатных функциях, а date_trunc('YEAR' , transaction_date::date ) " 2023 " не фильтрует по году
date_trunc не работает с датами в формате YYYY, а regexp_replace удаляет только буквы, но не лишние символы


**Дана таблица с заказами:**

Для данной таблицы необходимо:

Рассчитать скользящую сумму заказов за пять последних заказов пользователя.
Определить разницу во времени между текущим заказом и предыдущим для каждого пользователя.
Пронумеровывать заказы каждого пользователя по дате.
Вычислить процент заказа от общей суммы заказов пользователя.
Вывести ранг пользователя по сумме заказов за месяц.
Ниже дан запрос, который выводит всю запрашиваемую информацию, однако в нем некоторые из пяти показателей подсчитаны неверно. Какие?

Запрос:

select
user_id ,
order_id ,
order_date ,
order_amount ,
sum(order_amount ) over ( partition by user_id order by order_date rows between 5 preceding and current row) as rolling_sum ,
extract ( epoch from ( order_date - lag(order_date ) over ( partition by user_id order by order_date ) ) ) as time_diff ,
row_number ( ) over ( partition by user_id order by order_date ) as order_number ,
order_amount/sum(order_amount ) over ( partition by user_id ) as order_percentage ,
rank ( ) over ( partition by date_trunc("month " , order_date ) order by sum(order_amount ) over ( partition by user_id ) ) as user_rank
from orders

скользящая сумма заказов, разница во времени между заказами, ранг пользователя по сумме заказов
V **скользящая сумма заказов, ранг пользователя по сумме заказов, процент заказа от общей суммы**
разница во времени между заказами, номер заказа по дате, ранг пользователя по сумме заказов
номер заказа по дате, процент заказа от общей суммы, разница во времени между заказами
скользящая сумма заказов, номер заказа по дате, процент заказа от общей суммы


**Выберите синтаксически корректный запрос:**

update table public.table_1 ( user_id int , salary float , department_id str )
alter table public.table_1 add ( user_id int , salary float , department_id int )
modify table public.table_1 ( user_id int , salary float , department_id str )
alter table public.table_1 ( user_id int , add salary float , add department_id int )
V **alter table public.table_1 add user_id int , add salary float , add department_id int**


**Какой из следующих индексов будет наиболее оптимальным для ускорения запросов, фильтрующих данные по user_id и сортирующих их по created_at?**

create index payments_gin_idx on payments using gin ( to_tsvector('english ' , user_id::text ) ) ;
create index payments_user_id_hash_idx on payments using hash ( user_id ) ;
create index payments_user_id_idx on payments using btree ( user_id ) ;
V **create index payments_user_id_created_at_idx on payments using btree ( user_id , created_at ) ;**
create index payments_brin_idx on payments using brin ( created_at ) ;


**Определите список разрешений, на который можно выдать или отозвать права с помощью операторов GRANT , REVOKE:**

GRANT , INSERT , UPDATE , EXCEPT
IF , SELECT , JOIN , UNION
INTERSECT , DROP , SELECT , ALL
CREATE , TRUNCATE , DELETE , TRIGGER
V **INSERT , SELECT , JOIN , CREATE**


**Выберите верное утверждение:**

ANY и EXISTS полностью взаимозаменяемы, так как оба проверяют наличие значений в подзапросе
ANY всегда используется только с оператором = для сравнения значений из подзапроса
ANY EXISTS можно использовать только в WHERE, но не в HAVING
V **EXISTS проверяет, содержит ли подзапрос хотя бы одну строку, и возвращает TRUE, подзапрос возвращает одну или несколько строк**
EXISTS выполняет подзапрос один раз и кэширует результат, а ANY выполняет подзапрос для каждой строки


**Выберите верное утверждение:**

INTERSECT выполняет пересечение минимум трех наборов данных или таблиц
ключевое слово ALL является обязательным для операторов INTERSECT и EXCEPT
смена порядка запросов для INTERSECT поменяет выводимые данные
команда UNION выполняется быстрее, чем команда UNION ALL
V **смена порядка запросов для EXCEPT поменяет выводимые данные**

**Выберите операторы, относящиеся только к DDL:**

SELECT , TRUNCATE , UPDATE , DROP
RENAME , ALTER , TRUNCATE , DELETE
V **DROP , ALTER , CREATE , RENAME**
INSERT , DROP , DELETE , UPDATE
CREATE , DROP , RENAME , UPDATE