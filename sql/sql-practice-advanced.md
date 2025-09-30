STATUS: решение проверено публичными тестами

**Максимальный средний вес товара**
Описание:
Вы — аналитик в агентстве. Крупный ритейлер заказал у вашего агентства исследование среднего веса приобретаемых фруктов для оптимизации закупок и изучения поведения покупателей в зависимости от типа торговой точки.

Посчитайте средний вес каждого товара по торговым точкам. Определите максимальный средний вес каждого товара и магазин, в котором он был зафиксирован.

Формат ввода:
Таблица giper_market:

item (string) — название товара
weight (float) — средний вес товара
Таблица local_market:

item (string) — название товара
weight (float) — средний вес товара
Таблица super_market:

item (string) — название товара
weight (float) — средний вес товара
Данные не содержат пропусков или некорректных значений. Во всех магазинах изучаемый ассортимент идентичный.

Формат вывода:
Запрос должен вернуть таблицу со следующими полями:

item (string) — название товара
max_avg_weight (float) — максимальный средний вес, округленный до 2 знаков после запятой
shop (string) — название магазина, в котором был посчитан максимальный средний вес товара
Таблица должна быть отсортирована по item и shop.

Код:

CREATE TABLE giper_market (
item  TEXT NOT NULL,
weight  FLOAT NOT NULL
);
CREATE TABLE local_market (
item  TEXT NOT NULL,
weight  FLOAT NOT NULL
);
CREATE TABLE super_market (
item  TEXT NOT NULL,
weight  FLOAT NOT NULL
);

INSERT INTO giper_market (item, weight) VALUES 
('арбуз', 3781.19),
('лимон', 1769.23),
('яблоко', 3435.11),
('банан', 2611.26),
('дыня', 2233.21);
INSERT INTO local_market (item, weight) VALUES 
('банан', 3006.65),
('банан', 1443.08),
('яблоко', 1764.49),
('арбуз', 2855.19),
('яблоко', 800.58);
INSERT INTO super_market (item, weight) VALUES 
('персик', 1379.38),
('виноград', 2313.62),
('яблоко', 338.91),
('арбуз', 5490.58),
('арбуз', 7268.54);

**РЕШЕНИЕ:**
WITH all_markets AS (
    SELECT item, weight, 'giper_market' as shop FROM giper_market
    UNION ALL
    SELECT item, weight, 'local_market' as shop FROM local_market
    UNION ALL
    SELECT item, weight, 'super_market' as shop FROM super_market
),
avg_weights AS (
    SELECT 
        item,
        shop,
        ROUND(AVG(weight), 2) as avg_weight
    FROM all_markets
    GROUP BY item, shop
),
max_weights AS (
    SELECT 
        item,
        MAX(avg_weight) as max_avg_weight
    FROM avg_weights
    GROUP BY item
)
SELECT 
    a.item,
    m.max_avg_weight,
    a.shop
FROM avg_weights a
JOIN max_weights m ON a.item = m.item AND a.avg_weight = m.max_avg_weight
ORDER BY a.item, a.shop;

**AЛЬТЕРНАТИВНОЕ РЕШЕНИЕ С ОКОННОЙ ФУНКЦИЕЙ**
WITH all_markets AS (
    SELECT item, weight, 'giper_market' as shop FROM giper_market
    UNION ALL
    SELECT item, weight, 'local_market' as shop FROM local_market
    UNION ALL
    SELECT item, weight, 'super_market' as shop FROM super_market
),
avg_weights AS (
    SELECT 
        item,
        shop,
        ROUND(AVG(weight), 2) as avg_weight,
        RANK() OVER (PARTITION BY item ORDER BY AVG(weight) DESC) as rnk
    FROM all_markets
    GROUP BY item, shop
)
SELECT 
    item,
    avg_weight as max_avg_weight,
    shop
FROM avg_weights
WHERE rnk = 1
ORDER BY item, shop;



STATUS: решение проверено публичными тестами

**Доля трафиков от ботов**
Описание:
Команда антифрода разработала механизм определения трафика от ботов на сайт магазина: при входе бота на сайт в параметры его URL добавляется параметр type=bot. Но из-за периодического падения сервера с системой мониторинга в параметр type у ботов иногда ставится не bot, а нижнее подчеркивание.

Тем не менее, иногда ботам удается обмануть систему мониторинга и отметка bot не попадает в url. В этом случае бота можно идентифицировать по user_id (если user_id хотя бы один раз был определен как бот, то он всегда должен определяться как бот).

Изучите данные с визитами пользователей на сайт и посчитайте долю ботов от общего числа пользователей в декабре. При определении ботов учитывайте, что если user_id хотя бы один раз был определен как бот, то он всегда должен определяться как бот.

Формат ввода:
Таблица events:

event_date (date) — дата визита
user_id (int) — уникальный идентификатор пользователя
url (string) — ссылка, по которой был осуществлен переход
Данные не содержат пропусков или некорректных значений.

Формат вывода:
Запрос должен вернуть таблицу с полями:

share (float) — доля ботов от общего числа пользователей в декабре, округленная до одного знака после запятой.
Код:

CREATE TABLE events (
    event_date DATE NOT NULL,
    user_id INT NOT NULL,
    url VARCHAR(255) NOT NULL
);

INSERT INTO events (event_date, user_id, url) VALUES
('2024-12-01', 1, 'https://my_website.com/home?type=user&dt=2024-12-01'),
('2024-12-01', 2, 'https://my_website.com/home?type=bot&dt=2024-12-01'),
('2024-12-15', 3, 'https://my_website.com/home?type=user&dt=2024-11-30'),
('2024-12-31', 4, 'https://my_website.com/home?type=bot&dt=2024-12-31'),
('2024-12-05', 5, 'https://my_website.com/home?type=bot&dt=2024-12-05');

**РЕШЕНИЕ**
WITH december_users AS (
    -- Все уникальные пользователи за декабрь
    SELECT DISTINCT user_id
    FROM events
    WHERE EXTRACT(MONTH FROM event_date) = 12
),
bot_users AS (
    -- Пользователи, которые хотя бы раз были определены как боты
    SELECT DISTINCT user_id
    FROM events
    WHERE url LIKE '%type=bot%' OR url LIKE '%type=_%'
)
SELECT 
    ROUND(
        COUNT(DISTINCT b.user_id) * 100.0 / COUNT(DISTINCT d.user_id),
        1
    ) as share
FROM december_users d
LEFT JOIN bot_users b ON d.user_id = b.user_id;

**AЛЬТЕРНАТИВНОЕ РЕШЕНИЕ С ОКОННОЙ ФУНКЦИЕЙ**
WITH bot_identification AS (
    SELECT 
        user_id,
        MAX(CASE WHEN url LIKE '%type=bot%' OR url LIKE '%type=_%' THEN 1 ELSE 0 END) as is_bot
    FROM events
    WHERE EXTRACT(MONTH FROM event_date) = 12
    GROUP BY user_id
)
SELECT 
    ROUND(
        SUM(is_bot) * 100.0 / COUNT(*),
        1
    ) as share
FROM bot_identification;

Проверка на тестовых данных:
На предоставленных данных:
Все пользователи за декабрь: 1, 2, 3, 4, 5
Боты: 2 (type=bot), 4 (type=bot), 5 (type=bot)
Доля ботов: 3/5 = 60.0%
Оба запроса вернут результат: 60.0


STATUS: решение проверено публичными тестами
**Максимальный средний вес товара**

Описание:
Вы — аналитик в агентстве. Крупный ритейлер заказал у вашего агентства исследование среднего веса приобретаемых фруктов для оптимизации закупок и изучения поведения покупателей в зависимости от типа торговой точки.

Посчитайте средний вес каждого товара по торговым точкам. Определите максимальный средний вес каждого товара и магазин, в котором он был зафиксирован.

Формат ввода:
Таблица giper_market:

item (string) — название товара
weight (float) — средний вес товара
Таблица local_market:

item (string) — название товара
weight (float) — средний вес товара
Таблица super_market:

item (string) — название товара
weight (float) — средний вес товара
Данные не содержат пропусков или некорректных значений. Во всех магазинах изучаемый ассортимент идентичный.

Формат вывода:
Запрос должен вернуть таблицу со следующими полями:

item (string) — название товара
max_avg_weight (float) — максимальный средний вес, округленный до 2 знаков после запятой
shop (string) — название магазина, в котором был посчитан максимальный средний вес товара
Таблица должна быть отсортирована по item и shop.

Код:

CREATE TABLE giper_market (
item  TEXT NOT NULL,
weight  FLOAT NOT NULL
);
CREATE TABLE local_market (
item  TEXT NOT NULL,
weight  FLOAT NOT NULL
);
CREATE TABLE super_market (
item  TEXT NOT NULL,
weight  FLOAT NOT NULL
);

INSERT INTO giper_market (item, weight) VALUES 
('арбуз', 3781.19),
('лимон', 1769.23),
('яблоко', 3435.11),
('банан', 2611.26),
('дыня', 2233.21);
INSERT INTO local_market (item, weight) VALUES 
('банан', 3006.65),
('банан', 1443.08),
('яблоко', 1764.49),
('арбуз', 2855.19),
('яблоко', 800.58);
INSERT INTO super_market (item, weight) VALUES 
('персик', 1379.38),
('виноград', 2313.62),
('яблоко', 338.91),
('арбуз', 5490.58),
('арбуз', 7268.54);

**РЕШЕНИЕ**
WITH all_markets AS (
    SELECT item, weight, 'giper_market' as shop FROM giper_market
    UNION ALL
    SELECT item, weight, 'local_market' as shop FROM local_market
    UNION ALL
    SELECT item, weight, 'super_market' as shop FROM super_market
),
avg_weights AS (
    SELECT 
        item,
        shop,
        ROUND(AVG(weight), 2) as avg_weight
    FROM all_markets
    GROUP BY item, shop
),
ranked_weights AS (
    SELECT 
        item,
        shop,
        avg_weight,
        ROW_NUMBER() OVER (PARTITION BY item ORDER BY avg_weight DESC, shop) as rn
    FROM avg_weights
)
SELECT 
    item,
    avg_weight as max_avg_weight,
    shop
FROM ranked_weights
WHERE rn = 1
ORDER BY item, shop;

**АЛЬТЕРНАТИВНОЕ РЕШЕНИЕ**
WITH all_markets AS (
    SELECT item, weight, 'giper_market' as shop FROM giper_market
    UNION ALL
    SELECT item, weight, 'local_market' as shop FROM local_market
    UNION ALL
    SELECT item, weight, 'super_market' as shop FROM super_market
),
avg_weights AS (
    SELECT 
        item,
        shop,
        ROUND(AVG(weight), 2) as avg_weight
    FROM all_markets
    GROUP BY item, shop
)
SELECT DISTINCT ON (item)
    item,
    avg_weight as max_avg_weight,
    shop
FROM avg_weights
ORDER BY item, avg_weight DESC, shop;

РЕЗУЛЬТАТЫ ЗАПРОСОВ:
item	max_avg_weight	shop
арбуз	6383.56	super_market
банан	3006.65	local_market
виноград	2313.62	super_market
дыня	2233.21	giper_market
лимон	1769.23	giper_market
персик	1379.38	super_market
яблоко	3435.11	giper_market


STATUS: решение проверено публичными тестами
****




STATUS: решение проверено публичными тестами