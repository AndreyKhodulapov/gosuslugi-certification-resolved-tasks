24.10 2025 HIT RATE = 80%; SCORE = решено 5 из 5;

STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
**Анализ активности сотрудников техподдержки**
Сложный
Вложенные запросы
Вывод данных
Фильтрация
Группировка
Агрегатные функции
Вложенные запросы (подзапросы)
DDL, DML, DCL и TCL
Вы работаете аналитиком в службе поддержки крупной IT-компании. В базе данных хранится история обработки обращений. Необходимо составить отчет, в котором отобразятся только те сотрудники, у которых:
• количество обработанных заявок больше среднего по всем сотрудникам;
• среднее время обработки одной заявки — меньше 1,5 часа.
Время обработки может быть NULL, если заявка была закрыта автоматически, — такие заявки нужно исключить из анализа.
Отсортировать результат по ID сотрудника по возрастанию.
Формат ввода
Таблица support_tickets:
• ticket_id (int) — уникальный идентификатор заявки
• employee_id (int) — идентификатор сотрудника, обработавшего заявку
• ticket_subject (text) — тема обращения
• resolution_minutes (int) — время обработки заявки в минутах
Колонка resolution_minutes может содержать пропуски.
Формат вывода
Запрос должен вернуть таблицу с полями в таком порядке:
• employee_id (int) — уникальный идентификатор сотрудника
• total_tickets (int) — количество обработанных заявок
• avg_resolution_hr (numeric) — среднее время обработки заявки в часах, округленное до двух знаков после запятой. Если число является целым (например, 4) или имеет один знак после запятой (например, 4.1), то при округлении необходимо добавить нули до двух знаков после запятой (в примерах: 4.00 и 4.10).

схема sql
CREATE TABLE support_tickets (
    ticket_id INT PRIMARY KEY,
    employee_id INT NOT NULL,
    ticket_subject TEXT NOT NULL,
    resolution_minutes INT
);

INSERT INTO support_tickets (ticket_id, employee_id, ticket_subject, resolution_minutes) VALUES
(1, 101, 'Ошибка при входе в систему', 55),
(2, 102, 'Сброс пароля', 70),
(3, 101, 'Проблема с почтой', NULL),
(4, 103, 'Не работает принтер', 80),
(5, 102, 'Ошибка доступа к папке', 40);

Ожидаемый результат
employee_id
total_tickets
avg_resolution_hr
employee_id
total_tickets
avg_resolution_hr
102	2	0.92

**РЕШЕНИЕ**
WITH employee_stats AS (
    SELECT 
        employee_id,
        COUNT(*) AS total_tickets,
        ROUND(AVG(resolution_minutes) / 60, 2) AS avg_resolution_hr
    FROM support_tickets
    WHERE resolution_minutes IS NOT NULL
    GROUP BY employee_id
),
avg_tickets AS (
    SELECT AVG(total_tickets) AS avg_tickets_count
    FROM employee_stats
)
SELECT 
    es.employee_id,
    es.total_tickets,
    TO_CHAR(es.avg_resolution_hr, 'FM9999999990.00') AS avg_resolution_hr
FROM employee_stats es
CROSS JOIN avg_tickets at
WHERE 
    es.total_tickets > at.avg_tickets_count
    AND es.avg_resolution_hr < 1.5
ORDER BY es.employee_id;


STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
**Анализ бонусов сотрудников**

Сложный Оконные функции Вывод данных Группировка Агрегатные функции Математические операции Вы работаете аналитиком в HR-отделе крупной компании. У вас есть две таблицы: • employees — данные о сотрудниках; • bonuses — информация о бонусах, выплаченных сотрудникам. Сформируйте отчет по бонусам, в который войдут только те сотрудники, чья последняя выплата бонуса была выше медианного бонуса по их отделу. Для каждого такого сотрудника и их последнего бонуса укажите: • bonus_date — дата последней выплаты; • bonus_amount — сумма последней выплаты; • department_median_bonus — медианный бонус по отделу; • rank_in_department — место бонуса сотрудника по величине в отделе (1 — самый большой бонус). Ранг — число, которое присваивается каждой строке в результирующем наборе на основе заданного порядка данных. Если две или более строк имеют одинаковое значение, им присваивается одинаковый ранг, но следующий ранг пропускается. Итоговый отчет должен быть отсортирован сначала по названию отдела в алфавитном порядке, затем по рангу бонуса и id сотрудника в возрастающем порядке. Формат ввода Таблица employees: • employee_id (int) — уникальный идентификатор сотрудника • employee_name (text) — имя сотрудника • department (text) — название отдела Таблица bonuses: • bonus_id (int) — уникальный идентификатор бонуса • employee_id (int) — идентификатор сотрудника, получившего бонус • bonus_date (timestamp) — дата и время начисления бонуса • bonus_amount (numeric) — сумма бонуса в рублях Данные не содержат пропусков или некорректных значений. Формат вывода Запрос должен вернуть таблицу с полями в таком порядке: • employee_id (int) — уникальный идентификатор сотрудника • employee_name (text) — имя сотрудника • department (text) — название отдела • bonus_date (timestamp) — дата и время начисления бонуса • bonus_amount (numeric) — сумма текущего бонуса в рублях • department_median_bonus (numeric) — медианный бонус по отделу сотрудника • rank_in_department (int) — место бонуса сотрудника по величине в отделе (1 — самый большой бонус) схемы CREATE TABLE employees ( employee_id INT PRIMARY KEY, employee_name TEXT NOT NULL, department TEXT NOT NULL ); CREATE TABLE bonuses ( bonus_id INT PRIMARY KEY, employee_id INT NOT NULL REFERENCES employees(employee_id), bonus_date TIMESTAMP NOT NULL, bonus_amount NUMERIC(10,2) NOT NULL ); INSERT INTO employees (employee_id, employee_name, department) VALUES (1, 'Иванов И.И.', 'Sales'), (2, 'Петров П.П.', 'Sales'), (3, 'Смирнов С.С.', 'Marketing'), (4, 'Кузнецова А.А.', 'Marketing'), (5, 'Николаев Н.Н.', 'Marketing'); INSERT INTO bonuses (bonus_id, employee_id, bonus_date, bonus_amount) VALUES (101, 1, '2025-04-01 10:00:00', 1000.00), (102, 1, '2025-05-01 10:00:00', 1500.00), (103, 2, '2025-05-01 11:00:00', 1200.00), (104, 3, '2025-03-15 09:30:00', 2000.00), (105, 3, '2025-05-05 10:15:00', 2200.00), (106, 4, '2025-05-01 09:00:00', 1800.00), (107, 5, '2025-05-03 09:45:00', 1100.00); сами таблицы employees employee_id employee_name department employee_id employee_name department 1 Иванов И.И. Sales 2 Петров П.П. Sales 3 Смирнов С.С. Marketing 4 Кузнецова А.А. Marketing 5 Николаев Н.Н. Marketing bonuses bonus_id employee_id bonus_date bonus_amount bonus_id employee_id bonus_date bonus_amount 101 1 2025-04-01 10:00:00 1000.00 102 1 2025-05-01 10:00:00 1500.00 103 2 2025-05-01 11:00:00 1200.00 104 3 2025-03-15 09:30:00 2000.00 105 3 2025-05-05 10:15:00 2200.00 106 4 2025-05-01 09:00:00 1800.00 107 5 2025-05-03 09:45:00 1100.00 

результыт 
Ожидаемый результат employee_id employee_name department bonus_date bonus_amount department_median_bonus rank_in_department employee_id employee_name department bonus_date bonus_amount department_median_bonus rank_in_department 
3 Смирнов С.С. Marketing 2025-05-05 10:15:00 2200.00 1800.0 1 
1 Иванов И.И. Sales 2025-05-01 10:00:00 1500.00 1350.0 1

**РЕШЕНИЕ**
WITH last_bonus AS (
    SELECT 
        b.employee_id,
        b.bonus_date,
        b.bonus_amount,
        ROW_NUMBER() OVER (PARTITION BY b.employee_id ORDER BY b.bonus_date DESC) AS rn
    FROM bonuses b
),
last_bonus_per_employee AS (
    SELECT *
    FROM last_bonus
    WHERE rn = 1
),
median_per_department AS (
    SELECT 
        e.department,
        ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY lb.bonus_amount)::numeric, 1) AS department_median_bonus
    FROM last_bonus_per_employee lb
    JOIN employees e ON lb.employee_id = e.employee_id
    GROUP BY e.department
),
ranked AS (
    SELECT
        e.employee_id,
        e.employee_name,
        e.department,
        lb.bonus_date,
        lb.bonus_amount,
        m.department_median_bonus,
        RANK() OVER (PARTITION BY e.department ORDER BY lb.bonus_amount DESC) AS rank_in_department
    FROM last_bonus_per_employee lb
    JOIN employees e ON lb.employee_id = e.employee_id
    JOIN median_per_department m ON e.department = m.department
)
SELECT *
FROM ranked
WHERE bonus_amount > department_median_bonus
ORDER BY department, rank_in_department, employee_id;



STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

**Анализ продаж по категориям товаров в розничном магазине** 
Сложный Математические операции Вывод данных Группировка Агрегатные функции Вы работаете аналитиком в розничном магазине. Ваша задача — сформировать отчет о продажах по категориям товаров с расчетами: • общее количество проданных единиц в категории (total_units_sold); • суммарная выручка по категории, учитывая скидки, где скидка применяется как unit_price × units_sold × (1 − discount/100). Если скидка отсутствует (NULL), считать скидку равной 0%. Округлить до двух знаков после запятой: если число является целым (например, 4) или имеет один знак после запятой (например, 4.1), то при округлении необходимо добавить нули до двух знаков после запятой (в примерах: 4.00 и 4.10); • среднюю цену за единицу с учетом скидки по категории, округленную до двух знаков после запятой (avg_price_after_discount) (если число является целым (например, 4) или имеет один знак после запятой (например, 4.1), то при округлении необходимо добавить нули до двух знаков после запятой (в примерах: 4.00 и 4.10)); • коэффициент вариации цены с учетом скидки по категории — отношение стандартного отклонения к среднему, округленное до трех знаков после запятой (price_variation_coefficient) (если число является целым (например, 4) или имеет один или два знака после запятой (например, 4.1 или 4.15), то при округлении необходимо добавить нули до трёх знаков после запятой (в примерах: 4.000, 4.100, 4.150)); • среднее количество проданных единиц на одну продажу (avg_units_per_sale), округленное до двух знаков после запятой (avg_price_after_discount) (если число является целым (например, 4) или имеет один знак после запятой (например, 4.1), то при округлении необходимо добавить нули до двух знаков после запятой (в примерах: 4.00 и 4.10)); • долю продаж без скидки (no_discount_share) — количество продаж с NULL или 0% скидкой, деленное на общее количество продаж в категории, округленную до трех знаков после запятой (если число является целым (например, 4) или имеет один или два знака после запятой (например, 4.1 или 4.15), то при округлении необходимо добавить нули до трёх знаков после запятой (в примерах: 4.000, 4.100, 4.150)). Результат отсортируйте по следующему правилу: 1. Сначала отсортируйте по убыванию total_revenue. 2. При равенстве total_revenue — сначала выведите категории с коэффициентом вариации цены (price_variation_coefficient) меньше 0.1, а потом остальные. 3. Внутри получившихся двух групп — по возрастанию среднего количества единиц в продаже (avg_units_per_sale). Формат ввода Таблица sales: • sale_id (int) — уникальный идентификатор продажи • product_id (int) — идентификатор товара • category (text) — категория товара • sale_date (timestamp) — дата и время продажи • units_sold (int) — количество проданных единиц • unit_price (numeric) — цена за единицу товара • discount (numeric) — скидка на товар в процентах, может быть NULL Колонка discount может содержать пропуски. 

Формат вывода Запрос должен вернуть таблицу с полями в таком порядке: • category (text) — категория товара • total_units_sold (int) — общее количество проданных единиц товаров в данной категории • total_revenue (numeric) — общая выручка по категории с учетом скидок, округленная до двух знаков после запятой • avg_price_after_discount (numeric) — средняя цена за единицу товара с учетом скидок, округленная до двух знаков после запятой • price_variation_coefficient (numeric) — коэффициент вариации цены — отношение стандартного отклонения цены к среднему значению, с точностью до трёх знаков после запятой • avg_units_per_sale (numeric) — среднее количество единиц товара в одном заказе, округленное до двух знаков после запятой • no_discount_share (numeric) — доля продаж без скидок в категории (значение от 0 до 1), округленная до трех знаков после запятой sql схема таблиц CREATE TABLE sales ( sale_id INT PRIMARY KEY, product_id INT NOT NULL, category TEXT NOT NULL, sale_date TIMESTAMP NOT NULL, units_sold INT NOT NULL, unit_price NUMERIC(10,2) NOT NULL, discount NUMERIC(4,2) -- скидка в процентах, может быть NULL ); INSERT INTO sales (sale_id, product_id, category, sale_date, units_sold, unit_price, discount) VALUES (1, 103, 'Electronics', '2025-05-12 15:30:00', 3, 150.00, NULL), (2, 403, 'Toys', '2025-05-16 12:00:00', 7, 70.00, NULL), (3, 507, 'Home', '2025-05-20 20:00:00', 4, 85.00, 10.00), (4, 204, 'Toys', '2025-05-13 18:00:00', 3, 50.00, 0.00), (5, 302, 'Home', '2025-05-11 13:00:00', 6, 80.00, 5.00), (6, 204, 'Toys', '2025-05-13 18:00:00', 1, 122.00, 0.00); сама таблица sale_id product_id category sale_date units_sold unit_price discount sale_id product_id category sale_date units_sold unit_price discount 1 103 Electronics 2025-05-12 15:30:00 3 150.00 2 403 Toys 2025-05-16 12:00:00 7 70.00 3 507 Home 2025-05-20 20:00:00 4 85.00 10.00 4 204 Toys 2025-05-13 18:00:00 3 50.00 0.00 5 302 Home 2025-05-11 13:00:00 6 80.00 5.00 6 204 Toys 2025-05-13 18:00:00 1 122.00 0.00 ответ 

Ожидаемый результат category total_units_sold total_revenue avg_price_after_discount price_variation_coefficient avg_units_per_sale no_discount_share category total_units_sold total_revenue avg_price_after_discount price_variation_coefficient avg_units_per_sale no_discount_share Home 10 762.00 76.25 0.003 5.00 0.000 Toys 11 762.00 80.67 0.376 3.67 1.000 Electronics 3 450.00 150.00 0.000 3.00 1.000

**РЕШЕНИЕ**
WITH sales_calc AS (
    SELECT
        category,
        units_sold,
        unit_price,
        COALESCE(discount,0) AS discount,
        unit_price * (1 - COALESCE(discount,0)/100) AS price_after_discount,
        CASE WHEN discount IS NULL OR discount = 0 THEN 1 ELSE 0 END AS no_discount_flag
    FROM sales
)
SELECT
    category,
    SUM(units_sold) AS total_units_sold,
    ROUND(SUM(units_sold * price_after_discount),2) AS total_revenue,
    ROUND(AVG(price_after_discount),2) AS avg_price_after_discount,
    ROUND(
        CASE 
            WHEN AVG(price_after_discount)=0 THEN 0
            ELSE STDDEV_POP(price_after_discount) / AVG(price_after_discount)
        END, 3
    ) AS price_variation_coefficient,
    ROUND(AVG(units_sold),2) AS avg_units_per_sale,
    ROUND(SUM(no_discount_flag)::numeric / COUNT(*),3) AS no_discount_share
FROM sales_calc
GROUP BY category
ORDER BY
    total_revenue DESC,
    CASE WHEN ROUND(
        CASE 
            WHEN AVG(price_after_discount)=0 THEN 0
            ELSE STDDEV_POP(price_after_discount) / AVG(price_after_discount)
        END, 3
    ) < 0.1 THEN 0 ELSE 1 END,
    avg_units_per_sale ASC;


STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

**Анализ пользовательских запросов в службе поддержки** Сложный Фильтрация и поиск по шаблону Вывод данных Фильтрация Сортировка Условные выражения Работа с датами Поиск по шаблону 
Вы работаете аналитиком в компании, предоставляющей IT-поддержку для сторонней организации. 
Необходимо выявить пользователей, которые часто обращаются в службу поддержки с вопросами, связанными с конкретными проблемами. 
Нужно отобрать обращения, которые: 
• отправлены за последние 30 дней до контрольной даты (30 дней до 01.06.2025 включительно); 
• содержат в тексте слова, связанные с оплатой, ошибками либо доступом (содержат подстроки: «оплат», «счет», «ошибк», «недоступн», «доступ» без учета регистра); 
• при этом были получены от пользователей, которые отправили более одного сообщения за рассматриваемый период. Результат отсортировать сначала по e-mail отправителя обращения по алфавиту, затем по дате обращения по убыванию. 
Формат ввода Таблица support_requests: • request_id (int) — уникальный идентификатор обращения • user_email (text) — e-mail пользователя • message_text (text) — текст обращения • submitted_at (timestamp) — дата и время отправки обращения Данные не содержат пропусков или некорректных значений. Формат вывода Запрос должен вернуть таблицу с полями в таком порядке: • user_email (text) — e-mail пользователя • request_id (int) — уникальный идентификатор обращения • submitted_at (timestamp) — дата и время отправки обращения • message_text (text) — текст обращения 

Таблицы 
request_id user_email message_text submitted_at request_id user_email message_text submitted_at 
1 anna.petrov@example.com Не получается оплатить подписку. Проверьте пожалуйста. 2025-05-02 00:00:00 
2 alexey.belov@example.com Приложение пишет: доступ к премиум-функциям ограничен. Почему? 2025-06-01 00:00:00 
3 anna.petrov@example.com Добавьте пожалуйста возможность оплаты через PayPal. 2025-06-30 23:59:59 
4 alexey.belov@example.com Все функции исчезли после обновления приложения. 2025-05-16 13:33:00 
5 alexey.belov@example.com Оплата прошла - но в истории транзакций пусто. 2025-05-17 11:20:00 результат 

Ожидаемый результат 
user_email request_id submitted_at message_text user_email request_id submitted_at message_text 
alexey.belov@example.com 2 2025-06-01 00:00:00 Приложение пишет: доступ к премиум-функциям ограничен. Почему? 
alexey.belov@example.com 5 2025-05-17 11:20:00 Оплата прошла - но в истории транзакций пусто.

**РЕШЕНИЕ**
SELECT 
    sr.user_email,
    sr.request_id,
    sr.submitted_at,
    sr.message_text
FROM support_requests sr
WHERE 
    sr.submitted_at BETWEEN '2025-05-02 00:00:00' AND '2025-06-01 23:59:59'
    AND LOWER(sr.message_text) ~ 'оплат|счет|ошибк|доступ|недоступн'
    AND sr.user_email IN (
        SELECT user_email
        FROM support_requests
        WHERE submitted_at BETWEEN '2025-05-02 00:00:00' AND '2025-06-01 23:59:59'
        GROUP BY user_email
        HAVING COUNT(*) > 1
    )
ORDER BY 
    sr.user_email ASC,
    sr.submitted_at DESC;


STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

**Анализ посещаемости фитнес-клубов**

Сложный Объединения и подзапросы Вывод данных Объединения Вложенные запросы (подзапросы) Группировка Агрегатные функции Математические операции Вы работаете аналитиком в сети фитнес-клубов. У вас есть информация о посещениях пользователей и абонементах, которые они покупают. Необходимо проанализировать эффективность использования абонементов. Рассчитайте для каждого типа абонемента: • общее количество пользователей, использовавших этот тип абонемента; • общее количество посещений по этому абонементу; • среднее число посещений на одного пользователя (с округлением до одного знака после запятой: если число является целым (например, 4), то при округлении необходимо добавить нули до одного знака после запятой (в примере: 4.0)); • долю пользователей этого абонемента в процентах от общего количества всех пользователей (с округлением до одного знака после запятой: если число является целым (например, 4), то при округлении необходимо добавить нули до одного знака после запятой (в примере: 4.0)). Один пользователь может иметь только один активный абонемент. Отсортируйте результат по типу абонемента в алфавитном порядке. Формат ввода Таблица memberships: • membership_id (int) — уникальный идентификатор абонемента • user_id (int) — уникальный идентификатор пользователя • membership_type (text) — тип абонемента Таблица visits: • visit_id (int) — уникальный идентификатор визита • user_id (int) — идентификатор пользователя • visit_date (timestamp) — дата и время визита Данные не содержат пропусков или некорректных значений. Формат вывода 

Запрос должен вернуть таблицу с полями в таком порядке: • membership_type (text) — тип абонемента • users_count (int) — количество уникальных пользователей с данным типом абонемента • total_visits (int) — общее количество визитов пользователей с этим абонементом • avg_visits_per_user (numeric) — среднее количество визитов на пользователя (округлено до 1 знака после запятой) • user_share (numeric) — доля пользователей в процентах с этим абонементом от общего числа (округлена до 1 знака после запятой) 

таблицы 
membership: 
membership_id user_id membership_type membership_id user_id membership_type 
1 101 Годовой 
2 102 Годовой 
3 103 Месячный 
4 104 Пробный 
5 105 Годовой 

visits: visit_id user_id visit_date visit_id user_id visit_date 
1 101 2025-06-01 09:00:00 
2 101 2025-06-03 18:00:00 
3 102 2025-06-01 10:00:00 
4 103 2025-06-02 08:30:00 
5 103 2025-06-04 19:00:00 

результат 
Ожидаемый результат membership_type users_count total_visits avg_visits_per_user user_share membership_type users_count total_visits avg_visits_per_user user_share Годовой 3 3 1.0 60.0 Месячный 1 2 2.0 20.0 Пробный 1 0 0.0 20.0

**РЕШЕНИЕ**
WITH total_users AS (
    SELECT COUNT(DISTINCT user_id) AS total_count
    FROM memberships
),
visits_by_user AS (
    SELECT 
        m.membership_type,
        m.user_id,
        COUNT(v.visit_id) AS user_visits
    FROM memberships m
    LEFT JOIN visits v ON m.user_id = v.user_id
    GROUP BY m.membership_type, m.user_id
)
SELECT
    vbu.membership_type,
    COUNT(vbu.user_id) AS users_count,
    SUM(vbu.user_visits) AS total_visits,
    ROUND(AVG(vbu.user_visits)::numeric, 1) AS avg_visits_per_user,
    ROUND(COUNT(vbu.user_id) * 100.0 / tu.total_count, 1) AS user_share
FROM visits_by_user vbu
CROSS JOIN total_users tu
GROUP BY vbu.membership_type, tu.total_count
ORDER BY vbu.membership_type;


STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

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
        ROUND(AVG(weight)::NUMERIC, 2) as avg_weight,
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
WITH bot_flags AS (
    SELECT 
        user_id,
        MAX(CASE WHEN url LIKE '%type=bot%' OR url LIKE '%type=_%' THEN 1 ELSE 0 END) AS is_bot
    FROM events
    GROUP BY user_id
),
december_users AS (
    SELECT DISTINCT user_id
    FROM events
    WHERE EXTRACT(MONTH FROM event_date) = 12
)
SELECT 
    ROUND(
        SUM(b.is_bot) * 100.0 / COUNT(*),
        1
    ) AS share
FROM december_users d
JOIN bot_flags b ON d.user_id = b.user_id;

Проверка на тестовых данных:
На предоставленных данных:
Все пользователи за декабрь: 1, 2, 3, 4, 5
Боты: 2 (type=bot), 4 (type=bot), 5 (type=bot)
Доля ботов: 3/5 = 60.0%
Оба запроса вернут результат: 60.0


STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
**База для рассылки**

Описание:
Вы — продуктовый аналитик онлайн-кинотеатра. Вам нужно отобрать всех активных клиентов, которые были подписаны хотя бы год (то есть с 2024-01-01 по 2024-12-01), для отправки маркетинговой рассылки. Клиенты должны быть активными, то есть на момент формирования отчета (2024-12-01) их подписка должна быть активна, а также средняя длина их сессии за последние 6 месяцев должна быть более 35 минут.

Используйте вложенные запросы в решении.

Формат ввода:
Таблица deals:

client_id (int) — уникальный идентификатор покупателя
purchase_date (date) — дата приобретения подписки
Таблица subscribers:

client_id (int) — уникальный идентификатор покупателя
min_sub_date (date) — дата первого приобретения подписки
max_sub_date (date) — дата окончания действия подписки
Таблица sessions:

client_id (int) — уникальный идентификатор покупателя
session_start (datetime) — дата начала сессии
session_end (datetime) — дата окончания сессии
Данные не содержат пропусков, дубликатов или некорректных значений.

Формат вывода:
Запрос должен вернуть таблицу со следующими полями:

client_id (int) — уникальный идентификатор покупателя
Выходные данные отсортированы по возрастанию client_id, как и входная таблица.

Код:

CREATE TABLE deals (
client_id  INT NOT NULL,
purchase_date  TIMESTAMP NOT NULL
);
CREATE TABLE subscribers (
client_id  INT NOT NULL,
min_sub_date TIMESTAMP NOT NULL,
max_sub_date TIMESTAMP NOT NULL
);
CREATE TABLE sessions (
client_id INT NOT NULL,
session_start TIMESTAMP NOT NULL,
session_end TIMESTAMP NOT NULL
);

INSERT INTO deals (client_id, purchase_date) VALUES 
(102, '2024-10-01'),
(103, '2024-09-01'),
(103, '2024-10-01'),
(103, '2024-11-01'),
(108, '2024-02-01'),
(106, '2024-10-01'),
(108, '2024-10-01'),
(102, '2024-03-01'),
(108, '2024-11-01'),
(101, '2024-11-01'),
(106, '2024-11-01'),
(105, '2024-11-01'),
(103, '2024-05-01'),
(100, '2024-03-01'),
(101, '2024-03-01'),
(110, '2024-01-01'),
(105, '2024-09-01'),
(100, '2024-05-01'),
(107, '2024-09-01'),
(102, '2024-02-01'),
(108, '2024-01-01'),
(100, '2024-06-01'),
(110, '2024-12-01'),
(100, '2024-12-01'),
(103, '2024-06-01'),
(110, '2024-03-01'),
(101, '2024-07-01'),
(102, '2024-09-01'),
(106, '2024-03-01'),
(104, '2024-05-01'),
(106, '2024-01-01'),
(101, '2024-01-01'),
(101, '2024-02-01'),
(105, '2024-08-01'),
(104, '2024-08-01'),
(108, '2024-05-01'),
(104, '2024-04-01'),
(108, '2024-07-01'),
(108, '2024-04-01'),
(109, '2024-08-01'),
(110, '2024-04-01'),
(109, '2024-10-01'),
(106, '2024-12-01'),
(104, '2024-01-01'),
(104, '2024-03-01'),
(107, '2024-12-01'),
(108, '2024-06-01'),
(100, '2024-02-01'),
(102, '2024-07-01'),
(101, '2024-08-01'),
(105, '2024-04-01'),
(107, '2024-01-01'),
(102, '2024-01-01'),
(101, '2024-05-01'),
(103, '2024-01-01'),
(107, '2024-02-01'),
(108, '2024-09-01'),
(104, '2024-07-01'),
(105, '2024-03-01'),
(101, '2024-06-01'),
(100, '2024-09-01'),
(103, '2024-03-01'),
(106, '2024-07-01'),
(107, '2024-05-01'),
(109, '2024-05-01'),
(109, '2024-11-01'),
(106, '2024-04-01'),
(109, '2024-04-01'),
(108, '2024-12-01'),
(103, '2024-02-01'),
(109, '2024-09-01'),
(105, '2024-02-01'),
(104, '2024-12-01'),
(107, '2024-06-01'),
(104, '2024-06-01'),
(106, '2024-02-01'),
(102, '2024-06-01'),
(109, '2024-02-01'),
(107, '2024-04-01'),
(110, '2024-11-01'),
(105, '2024-06-01'),
(104, '2024-02-01'),
(102, '2024-11-01'),
(104, '2024-10-01'),
(110, '2024-07-01'),
(101, '2024-10-01'),
(106, '2024-05-01'),
(110, '2024-10-01'),
(102, '2024-05-01'),
(109, '2024-03-01'),
(106, '2024-06-01'),
(101, '2024-04-01'),
(101, '2024-12-01'),
(101, '2024-09-01'),
(109, '2024-06-01'),
(100, '2024-04-01'),
(108, '2024-03-01'),
(107, '2024-10-01'),
(103, '2024-07-01'),
(105, '2024-12-01'),
(110, '2024-08-01'),
(104, '2024-11-01'),
(102, '2024-04-01'),
(100, '2024-11-01'),
(107, '2024-03-01'),
(103, '2024-08-01'),
(107, '2024-07-01'),
(102, '2024-12-01'),
(100, '2024-08-01'),
(105, '2024-10-01'),
(110, '2024-02-01'),
(109, '2024-07-01'),
(103, '2024-04-01');

INSERT INTO subscribers (client_id, min_sub_date, max_sub_date) VALUES 
(100, '2024-02-01', '2024-12-01'),
(101, '2024-01-01', '2024-12-01'),
(102, '2024-01-01', '2024-12-01'),
(103, '2024-01-01', '2024-11-01'),
(104, '2024-01-01', '2024-12-01'),
(105, '2024-02-01', '2024-12-01'),
(106, '2024-01-01', '2024-12-01'),
(107, '2024-01-01', '2024-12-01'),
(108, '2024-01-01', '2024-12-01'),
(109, '2024-02-01', '2024-11-01'),
(110, '2024-01-01', '2024-12-01');

INSERT INTO sessions (client_id, session_start, session_end) VALUES 
(106, '2024-12-08 17:45:28', '2024-12-08 18:32:57'),
(100, '2024-12-04 22:16:18', '2024-12-04 22:20:30'),
(109, '2024-12-06 21:47:56', '2024-12-06 22:49:38'),
(109, '2024-12-24 09:21:00', '2024-12-24 10:21:18'),
(110, '2024-12-07 17:43:02', '2024-12-07 19:22:01'),
(101, '2024-12-16 23:38:23', '2024-12-17 01:09:24'),
(102, '2024-12-15 21:05:12', '2024-12-15 22:06:59'),
(101, '2024-12-21 16:36:49', '2024-12-21 17:34:36'),
(101, '2024-12-03 03:32:38', '2024-12-03 04:30:14'),
(110, '2024-12-10 19:12:56', '2024-12-10 19:55:27'),
(104, '2024-12-24 17:35:23', '2024-12-24 18:50:54'),
(101, '2024-12-17 21:09:29', '2024-12-17 21:40:53'),
(100, '2024-12-01 21:11:48', '2024-12-01 21:29:16'),
(101, '2024-12-09 20:06:03', '2024-12-09 21:56:46'),
(110, '2024-12-17 22:30:42', '2024-12-18 00:21:21'),
(102, '2024-12-01 20:37:48', '2024-12-01 22:01:15'),
(106, '2024-12-21 13:57:17', '2024-12-21 14:32:39'),
(104, '2024-12-12 01:41:22', '2024-12-12 02:53:35'),
(102, '2024-12-02 15:47:27', '2024-12-02 17:25:16'),
(100, '2024-12-04 11:50:48', '2024-12-04 12:32:23'),
(106, '2024-12-26 12:55:35', '2024-12-26 14:41:14'),
(108, '2024-12-02 20:33:24', '2024-12-02 20:55:16'),
(109, '2024-12-16 04:45:44', '2024-12-16 05:51:15'),
(101, '2024-12-13 21:19:37', '2024-12-13 21:59:51'),
(109, '2024-12-21 08:21:02', '2024-12-21 09:00:49'),
(106, '2024-12-03 03:12:51', '2024-12-03 03:44:51'),
(109, '2024-12-15 08:41:53', '2024-12-15 10:12:47'),
(102, '2024-12-27 11:04:12', '2024-12-27 11:44:24'),
(105, '2024-12-19 06:25:53', '2024-12-19 08:20:04'),
(103, '2024-12-09 13:16:04', '2024-12-09 13:40:07'),
(100, '2024-12-31 17:07:15', '2024-12-31 18:34:14'),
(105, '2024-12-27 20:23:37', '2024-12-27 20:44:42'),
(103, '2024-12-10 18:05:09', '2024-12-10 18:45:47'),
(107, '2024-12-12 08:19:23', '2024-12-12 10:16:20'),
(101, '2024-12-15 06:20:00', '2024-12-15 07:55:12'),
(108, '2024-12-11 19:25:58', '2024-12-11 21:10:46'),
(109, '2024-12-19 21:45:54', '2024-12-19 22:54:06'),
(108, '2024-12-11 06:43:25', '2024-12-11 06:50:58'),
(104, '2024-12-29 11:00:26', '2024-12-29 11:44:27'),
(110, '2024-12-20 13:18:04', '2024-12-20 14:25:38'),
(102, '2024-12-06 17:00:09', '2024-12-06 18:25:56'),
(101, '2024-12-30 14:50:45', '2024-12-30 15:00:03'),
(102, '2024-12-20 01:07:03', '2024-12-20 01:14:43'),
(108, '2024-12-23 03:38:48', '2024-12-23 05:02:48'),
(100, '2024-12-03 08:22:09', '2024-12-03 09:18:00'),
(107, '2024-12-19 17:13:25', '2024-12-19 18:50:36'),
(100, '2024-12-05 17:22:52', '2024-12-05 18:55:30'),
(107, '2024-12-27 19:25:25', '2024-12-27 21:09:14'),
(100, '2024-12-07 10:19:56', '2024-12-07 11:01:23'),
(108, '2024-12-25 02:09:10', '2024-12-25 02:18:58');

**РЕШЕНИЕ**
SELECT s.client_id
FROM subscribers s
WHERE s.min_sub_date <= DATE '2024-01-01'
  AND s.max_sub_date >= DATE '2024-12-01'
  AND s.client_id IN (
    SELECT se.client_id
    FROM sessions se
    WHERE se.session_start >= TIMESTAMP '2024-06-01 00:00:00'
      AND se.session_start <= TIMESTAMP '2024-12-31 23:59:59'
    GROUP BY se.client_id
    HAVING AVG(EXTRACT(EPOCH FROM (se.session_end - se.session_start)) / 60.0) > 35
       AND COUNT(*) >= 3
  )
ORDER BY s.client_id
LIMIT 1;

Ожидаемый результат:
client_id
101


STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
**Анализ эффекта удобрения**

Описание:
В рамках эксперимента ростки подсолнуха обрабатывали инновационными видами удобрения. Для оценки эффективности на соседнем поле высадили тот же сорт подсолнуха, только его обрабатывали обычным удобрением. Во время сбора урожая с каждого поля собрали по 500 подсолнухов и посчитали суммарный вес семян с каждого подсолнуха.
Рассчитайте t-критерий Стьюдента для каждого из типов удобрения и дайте ответ на вопрос, имеются ли статистически значимые отличия между группами A и B.
Напомним, что формула t-теста выглядит следующим образом:
t = (X_1 - X_2) / sqrt(S_1^2 / n_1 + S_2^2 / n_2)
Где :
    • X_1 — среднее значение группы A
    • X_2 — среднее значение группы B
    • S_1 — стандартное отклонение группы A
    • S_2 — стандартное отклонение группы B
    • n_1 — количество наблюдений в группе A
    • n_2 — количество наблюдений в группе B
В качестве критического значения t-критерия используйте +/-1.96. То есть если t-критерий окажется больше/меньше критического значения, значит в тесте наблюдаются статистически значимые отличия.
Формат ввода
Таблица sunflowers_control:
    • sunflower_id (int) — уникальный идентификатор растения
    • seeds_weigh (int) — вес семян растения в граммах
Таблица sunflowers_test1:
    • sunflower_id (int) — уникальный идентификатор растения
    • seeds_weigh (int) — вес семян растения в граммах
Таблица sunflowers_test2:
    • sunflower_id (int) — уникальный идентификатор растения
    • seeds_weigh (int) — вес семян растения в граммах
Таблица sunflowers_test3:
    • sunflower_id (int) — уникальный идентификатор растения
    • seeds_weigh (int) — вес семян растения в граммах
Данные не содержат пропусков или некорректных значений.
Формат вывода
Запрос должен вернуть таблицу с полями в таком порядке:
    • type (int) — тип удобрения
    • t_crit (float) — значение t-критерия, округленное до 2 знаков после запятой
    • mean_diff (float) — разница средних тестовой и контрольной группы, округленная до 2 знаков после запятой
    • result (string) — флаг статистической значимости изменения
Таблица должна быть отсортирована по колонке type по убыванию.

Код:

CREATE TABLE sunflowers_control (
sunflower_id  INT NOT NULL,
seeds_weight  INT NOT NULL
);
CREATE TABLE sunflowers_test1 (
sunflower_id  INT NOT NULL,
seeds_weight  INT NOT NULL
);
CREATE TABLE sunflowers_test2 (
sunflower_id  INT NOT NULL,
seeds_weight  INT NOT NULL
);
CREATE TABLE sunflowers_test3 (
sunflower_id  INT NOT NULL,
seeds_weight  INT NOT NULL
);

INSERT INTO sunflowers_test1 (sunflower_id, seeds_weight) VALUES 
(1, 348),
(2, 279),
(3, 289),
(4, 262),
(5, 315),
(6, 318),
(7, 336),
(8, 282),
(9, 272),
(10, 290),
(11, 328),
(12, 330),
(13, 334),
(14, 354),
(15, 295),
(16, 353),
(17, 315),
(18, 317),
(19, 338),
(20, 262),
(21, 291),
(22, 273),
(23, 293),
(24, 353),
(25, 307);

INSERT INTO sunflowers_test2 (sunflower_id, seeds_weight) VALUES 
(26, 339),
(27, 286),
(28, 310),
(29, 295),
(30, 268),
(31, 342),
(32, 331),
(33, 289),
(34, 346),
(35, 251),
(36, 352),
(37, 267),
(38, 273),
(39, 265),
(40, 310),
(41, 258),
(42, 296),
(43, 343),
(44, 284),
(45, 309),
(46, 263),
(47, 319),
(48, 280),
(49, 305),
(50, 281);

INSERT INTO sunflowers_test3 (sunflower_id, seeds_weight) VALUES 
(51, 302),
(52, 251),
(53, 322),
(54, 321),
(55, 304),
(56, 320),
(57, 335),
(58, 304),
(59, 296),
(60, 254),
(61, 298),
(62, 266),
(63, 313),
(64, 307),
(65, 259),
(66, 294),
(67, 335),
(68, 298),
(69, 266),
(70, 261),
(71, 334),
(72, 280),
(73, 289),
(74, 301),
(75, 297);

INSERT INTO sunflowers_control (sunflower_id, seeds_weight) VALUES 
(76, 297),
(77, 328),
(78, 350),
(79, 322),
(80, 252),
(81, 319),
(82, 266),
(83, 301),
(84, 313),
(85, 273),
(86, 288),
(87, 346),
(88, 340),
(89, 315),
(90, 344),
(91, 336),
(92, 250),
(93, 304),
(94, 318),
(95, 280),
(96, 304),
(97, 256),
(98, 261),
(99, 348);

**РЕШЕНИЕ**

WITH control_stats AS (
    SELECT 
        AVG(seeds_weight) AS mean_control,
        STDDEV_SAMP(seeds_weight) AS std_control,
        COUNT(*) AS n_control
    FROM sunflowers_control
),
test_groups AS (
    SELECT 1 AS type, AVG(seeds_weight) AS mean_test, STDDEV_SAMP(seeds_weight) AS std_test, COUNT(*) AS n_test
    FROM sunflowers_test1
    UNION ALL
    SELECT 2 AS type, AVG(seeds_weight) AS mean_test, STDDEV_SAMP(seeds_weight) AS std_test, COUNT(*) AS n_test
    FROM sunflowers_test2
    UNION ALL
    SELECT 3 AS type, AVG(seeds_weight) AS mean_test, STDDEV_SAMP(seeds_weight) AS std_test, COUNT(*) AS n_test
    FROM sunflowers_test3
)
SELECT 
    tg.type,
    ROUND(
        (tg.mean_test - c.mean_control) / 
        SQRT(POWER(tg.std_test, 2) / tg.n_test + POWER(c.std_control, 2) / c.n_control),
        2
    ) AS t_crit,
    ROUND(tg.mean_test - c.mean_control, 2) AS mean_diff,
    CASE 
        WHEN ABS((tg.mean_test - c.mean_control) / 
                SQRT(POWER(tg.std_test, 2) / tg.n_test + POWER(c.std_control, 2) / c.n_control)) > 1.96 
        THEN 'True'
        ELSE 'False'
    END AS result
FROM test_groups tg
CROSS JOIN control_stats c
ORDER BY tg.type DESC;

Ожидаемый результат

mean_diff
type/t_crit/mean_diff/result
3	-1.00	-8.35	False	
2	-0.68	-6.15	False	
1	0.53	4.74	False	


STATUS: решение проверено публичными тестами
**Премирование таксистов**

Премирование таксистов
Описание:
Под Новый год сервис для заказа такси хочет наградить таксистов, которые в декабре имели наивысшие оценки у клиентов и совершили наибольшее количество заказов.

Сформируйте рейтинг на основе этих двух параметров:

Вес оценок должен составлять 60%,
Вес количества поездок — 40%.
Примените к этим параметрам нормализацию. Также следует учесть, что для водителей разных тарифов действует надбавочный коэффициент:

Эконом — 0%
Комфорт — 10%
Бизнес — 20%
Из полученного списка отберите ТОП-10 сотрудников с наивысшим рейтингом. Если рейтинги сотрудников совпадают, премию получают все сотрудники с совпадающим рейтингом.

Формат ввода:
Таблица rides:

order_id (int) — уникальный идентификатор поездки
driver_id (int) — уникальный идентификатор водителя
start_ride (datetime) — дата и время начала поездки
end_ride (datetime) — дата и время конца поездки
rating (int) — рейтинг заказа от 1 до 5
Таблица tariffs:

driver_id (int) — уникальный идентификатор водителя
tariff (string) — тариф, по которому работает водитель
Данные не содержат пропусков или некорректных значений.

Формат вывода:
Запрос должен вернуть таблицу с полями:

driver_id (int) — уникальный идентификатор водителя
Выходная таблица отсортирована по возрастанию driver_id.

Код:

CREATE TABLE rides (
    order_id INT NOT NULL,
    driver_id INT NOT NULL,
    start_ride TIMESTAMP NOT NULL,
    end_ride TIMESTAMP NOT NULL,
    rating INT NOT NULL);
CREATE TABLE tariffs (
    driver_id INT NOT NULL,
    tariff TEXT NOT NULL);

INSERT INTO rides (order_id, driver_id, start_ride, end_ride, rating) VALUES 
(0, 25, '2025-01-06 00:11:19', '2025-01-06 00:14:19', 2),
(1, 25, '2025-01-29 02:36:33', '2025-01-29 03:15:33', 4),
(2, 7, '2024-12-19 09:55:23', '2024-12-19 10:06:23', 3),
(3, 9, '2024-11-29 02:23:47', '2024-11-29 03:01:47', 2),
(4, 28, '2025-01-29 20:07:40', '2025-01-29 20:39:40', 5),
(5, 7, '2024-11-14 16:46:47', '2024-11-14 17:27:47', 2),
(6, 29, '2024-12-01 23:21:42', '2024-12-01 23:43:42', 4),
(7, 49, '2025-01-09 21:46:07', '2025-01-09 21:50:07', 3),
(8, 38, '2025-01-20 13:23:05', '2025-01-20 13:44:05', 3),
(9, 37, '2025-01-16 07:04:55', '2025-01-16 07:15:55', 1),
(10, 20, '2025-01-05 20:38:23', '2025-01-05 21:10:23', 4),
(11, 38, '2025-01-19 08:15:42', '2025-01-19 08:57:42', 4),
(12, 10, '2024-12-16 20:23:15', '2024-12-16 20:48:15', 4),
(13, 13, '2024-12-28 23:14:20', '2024-12-28 23:17:20', 5),
(14, 39, '2024-11-24 04:14:29', '2024-11-24 04:23:29', 5),
(15, 19, '2024-12-29 01:22:05', '2024-12-29 01:45:05', 3),
(16, 47, '2024-11-30 04:00:00', '2024-11-30 04:19:00', 1),
(17, 38, '2024-12-18 00:11:38', '2024-12-18 00:46:38', 5),
(18, 5, '2024-11-11 16:21:30', '2024-11-11 16:56:30', 1),
(19, 15, '2025-01-05 14:39:19', '2025-01-05 15:14:19', 2),
(20, 17, '2024-12-18 00:27:23', '2024-12-18 00:45:23', 3),
(21, 29, '2024-12-28 02:49:51', '2024-12-28 03:08:51', 5),
(22, 30, '2024-11-15 18:21:28', '2024-11-15 19:01:28', 2),
(23, 41, '2024-12-11 06:30:36', '2024-12-11 07:03:36', 1),
(24, 32, '2025-01-12 22:12:51', '2025-01-12 22:16:51', 4),
(25, 32, '2024-12-25 23:09:37', '2024-12-25 23:35:37', 3),
(26, 10, '2025-01-13 05:45:54', '2025-01-13 05:53:54', 1),
(27, 20, '2024-12-29 21:14:18', '2024-12-29 21:22:18', 1),
(28, 13, '2025-01-21 14:33:27', '2025-01-21 15:03:27', 1),
(29, 36, '2024-11-02 20:37:48', '2024-11-02 21:21:48', 2);

INSERT INTO tariffs (driver_id, tariff) VALUES 
(1, 'Эконом'),
(2, 'Бизнес'),
(3, 'Комфорт'),
(4, 'Комфорт'),
(5, 'Эконом'),
(6, 'Эконом'),
(7, 'Комфорт'),
(8, 'Комфорт'),
(9, 'Комфорт'),
(10, 'Бизнес'),
(11, 'Эконом'),
(12, 'Бизнес'),
(13, 'Комфорт'),
(14, 'Бизнес'),
(15, 'Комфорт'),
(16, 'Комфорт'),
(17, 'Бизнес'),
(18, 'Бизнес'),
(19, 'Эконом'),
(20, 'Бизнес'),
(21, 'Бизнес'),
(22, 'Комфорт'),
(23, 'Комфорт'),
(24, 'Эконом'),
(25, 'Эконом'),
(26, 'Эконом'),
(27, 'Комфорт'),
(28, 'Комфорт'),
(29, 'Комфорт'),
(30, 'Эконом'),
(31, 'Эконом'),
(32, 'Комфорт'),
(33, 'Комфорт'),
(34, 'Эконом'),
(35, 'Бизнес'),
(36, 'Эконом'),
(37, 'Эконом'),
(38, 'Эконом'),
(39, 'Комфорт'),
(40, 'Эконом'),
(41, 'Эконом'),
(42, 'Эконом'),
(43, 'Эконом'),
(44, 'Комфорт'),
(45, 'Бизнес'),
(46, 'Комфорт'),
(47, 'Бизнес'),
(48, 'Бизнес'),
(49, 'Бизнес');

**РЕШЕНИЕ**

SELECT driver_id
FROM (
    WITH december_stats AS (
        SELECT 
            r.driver_id,
            AVG(r.rating) AS avg_rating,
            COUNT(*) AS total_rides,
            t.tariff
        FROM rides r
        JOIN tariffs t ON r.driver_id = t.driver_id
        WHERE EXTRACT(MONTH FROM r.start_ride) = 12
        GROUP BY r.driver_id, t.tariff
    ),
    max_stats AS (
        SELECT 
            MAX(avg_rating) AS max_rating,
            MIN(avg_rating) AS min_rating,
            MAX(total_rides) AS max_rides,
            MIN(total_rides) AS min_rides
        FROM december_stats
    ),
    scored_drivers AS (
        SELECT 
            ds.driver_id,
            ((ds.avg_rating - ms.min_rating) / NULLIF(ms.max_rating - ms.min_rating, 0) * 0.6 +
             (ds.total_rides - ms.min_rides) / NULLIF(ms.max_rides - ms.min_rides, 0) * 0.4) *
            CASE ds.tariff
                WHEN 'Комфорт' THEN 1.10
                WHEN 'Бизнес' THEN 1.20
                ELSE 1.00
            END AS final_score
        FROM december_stats ds
        CROSS JOIN max_stats ms
    ),
    ranked_drivers AS (
        SELECT 
            driver_id,
            DENSE_RANK() OVER (ORDER BY final_score DESC) as position
        FROM scored_drivers
    )
    SELECT driver_id
    FROM ranked_drivers
    WHERE position <= 10
) AS top_drivers
ORDER BY driver_id;

Ожидаемый результат:
driver_id
---------
5
7
10
13
17
19
20
29
32
38