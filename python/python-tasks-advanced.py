"25.10 2025 HIT RATE = 80%; SCORE =  3 правильно решенных из 5 - ЗАЧЕТ!;"

"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
Оценивание студентов

Вы разрабатываете систему отслеживания успеваемости студентов. Необходимо реализовать функцию, подсчитывающую число неуспевающих по каждому предмету.
Формат ввода
Две строки:
Первая содержит разделённые точками с запятой и пробелами предметы и проходные баллы в формате
<предмет>:<балл>
Где предмет – уникальная строка длиной от 3 до 20 символов, а балл – целое число от 0 до 100.
Вторая содержит список разделённых точкой с запятой и пробелами записей студентов в формате
<студент>: <предмет> <балл>, <предмет> <балл>, ...
Имя студента – уникальная строка длиной от 3 до 15 символов.
Предметы в одной строке гарантированно соответсвуют предметам в другой.
Формат вывода
Число получивших неудовлетворительную оценку по каждому предмету студентов в формате
<предмет>: <число студентов>; <предмет>: <число студентов>; …
Если таких нет, вывести строчку “Полная успеваемость”.
Пример 1
Входные данные:
Математика:60; Физика:50; Химия:70
Иванов: Математика 55, Физика 45, Химия 75; Петров: Математика 65, Физика 55, Химия 60; Сидоров: Математика 50, Физика 40, Химия 80
Выходные данные:
Математика: 2; Физика: 2; Химия: 1
Пример 2
Входные данные:
История:40; География:55; Биология:60
Смирнов: История 45, География 60, Биология 70; Кузнецов: История 50, География 58, Биология 66; Попов: История 56, География 70, Биология 90
Выходные данные:
Полная успеваемость

Тестовые данные
Входные данные
Физкультура: 30; Музыка: 50; Искусство: 40
Дима: Физкультура 20, Музыка 60, Искусство 30; Лена: Физкультура 40, Музыка 50, Искусство 50
Ожидаемый результат
Физкультура: 1; Музыка: 0; Искусство: 1

Входные данные
Алгебра: 50; Геометрия: 60; Физика: 70
Максим: Алгебра 40, Геометрия 70, Физика 80; Настя: Алгебра 60, Геометрия 50, Физика 60
Ожидаемый результат
Алгебра: 1; Геометрия: 1; Физика: 1

Входные данные
Химия: 65; Биология: 55; Литература: 75
Саша: Химия 70, Биология 50, Литература 80; Кристина: Химия 60, Биология 60, Литература 70
Ожидаемый результат
Химия: 1; Биология: 1; Литература: 1

Входные данные
История: 45; География: 50; Английский: 60
Рома: История 50, География 60, Английский 80; Катя: История 50, География 60, Английский 70
Ожидаемый результат
Полная успеваемость

Входные данные
Музыка: 40; Искусство: 30; Физкультура: 50
Тимур: Музыка 410, Искусство 40, Физкультура 60; Алина: Музыка 50, Искусство 90, Физкультура 60
Ожидаемый результат
Полная успеваемость

формат написания задачи
def get_results(subjects: str, students: str):
    "Ваш код"


subjects = input()

students = input()

results = get_results(subjects, students)

print(results)
"""

def get_results(subjects: str, students: str):
    # Парсинг предметов и проходных баллов
    subjects_dict = {}
    for item in subjects.split('; '):
        subject, passing_score = item.split(':')
        subjects_dict[subject] = int(passing_score)
    
    # Инициализация счетчиков неуспевающих
    failing_count = {subject: 0 for subject in subjects_dict}
    
    # Парсинг данных студентов
    for student_record in students.split('; '):
        # Разделяем имя студента и его оценки
        student_name, grades_part = student_record.split(': ')
        
        # Парсим оценки по предметам
        for grade_info in grades_part.split(', '):
            subject, score = grade_info.split(' ')
            score = int(score)
            
            # Проверяем, является ли оценка неудовлетворительной
            if score < subjects_dict[subject]:
                failing_count[subject] += 1
    
    # Формируем результат - ВСЕ предметы, даже с нулевым количеством
    result_parts = []
    for subject in subjects_dict:
        result_parts.append(f"{subject}: {failing_count[subject]}")
    
    # Проверяем, есть ли хотя бы один неуспевающий
    has_failing = any(failing_count[subject] > 0 for subject in failing_count)
    
    # Возвращаем результат
    if has_failing:
        return '; '.join(result_parts)
    else:
        return "Полная успеваемость"


# Чтение входных данных и вывод результата
# subjects = input()
# students = input()
# results = get_results(subjects, students)
# print(results)

"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
Победители лотереи
Вы работаете над программой для провеления лотерей. Чтобы победить в лотерее, 
участник должен угадать загаданную проследовательность цифр. Те, кто угадал сами цифры, но расположил 
их в неправильной последовательнсоти, тоже получают призы. Причем размер приза зависит от близости 
последовательности к выигрышному значению. 
Нужно написать программу которая находит следующее наиименьшее положительлное число с теми же цифрами  
что в правильной последовательности, если такого числа нет или следующее наименьшее число с такими же цифрами 
начинается с нуля вернуть -1

Формат ввода: одна строка цифр

Фформат вывода: одна строка в которой есть следующее меньшее число
если не существует вернуть -1
"""
def next_smaller(n):
    digits = list(str(n))
    
    # Находим индекс, где digit[i] > digit[i+1]
    pivot = -1
    for i in range(len(digits)-1, 0, -1):
        if digits[i] < digits[i-1]:
            pivot = i-1
            break
    
    # Если такой точки нет, значит число уже наименьшее
    if pivot == -1:
        return -1
    
    # Находим наибольшую цифру справа от pivot, которая меньше digits[pivot]
    swap_index = pivot + 1
    for i in range(pivot + 1, len(digits)):
        if digits[i] < digits[pivot] and digits[i] > digits[swap_index]:
            swap_index = i
    
    # Меняем местами
    digits[pivot], digits[swap_index] = digits[swap_index], digits[pivot]
    
    # Сортируем оставшуюся часть по убыванию (чтобы получить максимальное возможное число)
    digits[pivot+1:] = sorted(digits[pivot+1:], reverse=True)
    
    # Проверяем, что число не начинается с 0
    if digits[0] == '0':
        return -1
    
    result = int(''.join(digits))
    
    # Проверяем, что результат действительно меньше исходного
    return result if result < int(n) else -1

# Тестируем на примерах
assert next_smaller(531) == 513
assert next_smaller(101) == -1
assert next_smaller(123) == -1
assert next_smaller(153) == 135
assert next_smaller(897) == 879


"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН
Утешительный приз

Сложный | Лотерея | Числа | Циклы и условия

Вы работаете над программой для проведения лотерей. Чтобы победить в лотерее, участник должен угадать загаданную последовательность цифр. Те, кто угадал сами цифры, но расположил их в неправильной последовательности, тоже получают призы. При чем размер приза зависит от близости последовательности к выигрышному значению.

Задача вашей программы — найти следующее большее положительное число с теми же цифрами, что и в правильной последовательности. Если такого числа не существует или следующее большее число с такими же цифрами начинается с нуля, верните -1. Это значит, что других победителей в лотерее не будет.

Формат ввода
Одна строка с цифрами.

Формат вывода
Одна строка, в которой есть следующее большее число. Если число не существует, верните -1.

Пример 1
Входные данные: 513
Выходные данные: 531

Пример 2
Входные данные: 1111
Выходные данные: -1

Тесты: 
ввод 18 вывод 81 
ввод 513 вывод 531 
ввод 1111 вывод -1

РЕШЕНИЕ:
"""
def next_larger(n):
    digits = list(n)
    
    # Ищем позицию, где digit[i] < digit[i+1] (идя справа)
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # Если такой позиции нет, значит число максимально возможное
    if i == -1:
        return "-1"
    
    # Ищем наименьшую цифру справа от i, которая больше digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Меняем местами
    digits[i], digits[j] = digits[j], digits[i]
    
    # Сортируем оставшуюся часть по возрастанию
    digits[i + 1:] = sorted(digits[i + 1:])
    
    result = ''.join(digits)
    
    # Проверяем, что число не начинается с 0
    if result[0] == '0':
        return "-1"
    
    return result

# input_string = input()
# result = next_larger(input_string)
# print(result)


"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

Отчет о продажах за квартал

Вы работаете над модулем CRM-системы, который помогает менеджерам готовить автоматизированные отчеты.
Данные поступают в формате "Дата:Продукт:Количество;Дата:Продукт:Количество;...".
Напишите программу, которая принимает информацию о продажах по датам и возвращает отчет о продажах за каждый квартал.

Формат ввода
Одна строка с данными в формате "Дата:Продукт:Количество;Дата:Продукт:Количество;..."
Дата в формате YYYY-MM-DD, через двоеточие указано название продукта на русском языке и через еще одно двоеточие - 
целое число, указывающее на количество проданных товаров. Данные по каждому продукту разделены точкой с запятой.

Формат вывода
Набор строк, в котором выводится информация о продажах товаров.
Сначала дается номер квартала с двоеточием,а после - маркированный список с дефисом с названием товара и 
количеством продаж через двоеточие. Кварталы идут по порядку, а товары внутри квартала сортируются по алфавиту


Тесты 
ввод "2023-01-15:Книга:10;2023-04-20:Флешка:5;2023-07-05:Наушники:8"
вывод
Q1:
- Книга: 10
Q2:
- Флешка: 5
Q3:
- Наушники: 8

ввод "2023-02-05:Шляпа:4;2023-03-20:Кольцо:7;2023-04-25:Браслет:6;2023-04-26:Браслет:12"
вывод
Q1:
- Кольцо: 7
- Шляпа: 4
Q2:
- Браслет: 18

ввод "2023-03-05:Коврик:6;2023-04-25:Бинокль:10;2023-05-10:Компас:8;2023-03-05:Коврик:6;2023-04-25:Бинокль:10;2023-05-10:Компас:8"
вывод
Q1:
- Коврик: 12
Q2:
- Бинокль: 20
- Компас: 16

ввод "2023-05-20:Шапка:7;2023-02-25:Краска:5;2023-05-05:Мяч:8"
вывод
Q1:
- Краска: 5
Q2:
- Мяч: 8
- Шапка: 7

"""
class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = quantity

    @property
    def quarter(self):
        month = int(self.date.split('-')[1])
        if 1 <= month <= 3:
            return "Q1"
        elif 4 <= month <= 6:
            return "Q2"
        elif 7 <= month <= 9:
            return "Q3"
        else:
            return "Q4"
        
def generate_quartely_report(data):
    # Разбиваем строку на отдельные записи
    records = data.split(';')
    
    # Создаем словарь для хранения данных по кварталам
    quarters = {}
    
    # Обрабатываем каждую запись
    for record in records:
        if record:  # Пропускаем пустые записи
            date, product, quantity = record.split(':')
            item = Item(date, product, int(quantity))
            
            # Добавляем в соответствующий квартал
            if item.quarter not in quarters:
                quarters[item.quarter] = {}
            
            # Суммируем количество для одинаковых продуктов
            if product in quarters[item.quarter]:
                quarters[item.quarter][product] += int(quantity)
            else:
                quarters[item.quarter][product] = int(quantity)
    
    # Сортируем кварталы по порядку
    sorted_quarters = sorted(quarters.items())
    
    # Формируем вывод

    for quarter, products in sorted_quarters:
        yield "{}:".format(quarter)
        
        # Сортируем продукты по алфавиту
        sorted_products = sorted(products.items())
        for product, quantity in sorted_products:
            yield "- {}: {}".format(product, quantity)



"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

Без задолженностей
Вы работаете над модулем «Электронная зачетка» в системе для администрирования учебного процесса 
регионального вуза. Каждый студент может быть записан на несколько курсов, по каждому курсу у него есть итоговый балл.
Необходимо написать программу для учебного офиса, которая будет выбирать из базы тех студентов, которые 
не имеют ни одной академической задолженности. Студент без единой академической задолженности — студент, 
набравший строго выше проходного балла по всем курсам. Проходной балл определяется для каждого курса отдельно.

Формат ввода
Первая строка содержит информацию о студентах, курсах и их оценках в формате: 
"имя_студента,курс,оценка;имя_студента,курс,оценка;...". В строке есть информация хотя бы об одном студенте. 
Вторая строка содержит проходные баллы по предметам в формате: "курс,проходной_балл;курс,проходной_балл;...". Гарантируется, что на все указанные в первой строке курсы есть проходной балл.
Все баллы являются целыми положительными числами, а все имена студентов уникальны.

Формат вывода
Имена студентов без академической задолженности, каждое имя с новой строки. Если таких студентов нет, выводится слово «Пусто» (без кавычек).
Пример 1
Входные данные:
Анна,Математика,85;Анна,Химия,90;Борис,Математика,75;Борис,История,80;Евгений,Математика,95;Евгений,История,85
Математика,80;Химия,60;История,80
Выходные данные:
Анна
Евгений

Пример 2
Входные данные:
Анна,Психология,8;Анна,Литература,9;Борис,Обществознание,8
Психология,8;Литература,6;Обществознание,8
Выходные данные:
Пусто

"""
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}  # словарь: курс -> оценка
    
    def add_course(self, course, score):
        """Добавляет курс и оценку студента"""
        self.courses[course] = score
    
    def has_no_debt(self, passing_scores):
        """Проверяет, что у студента нет задолженностей"""
        for course, score in self.courses.items():
            if score <= passing_scores[course]:
                return False
        return True


class CourseManager: 
    def __init__(self): 
        self.students = {}  # словарь: имя -> объект Student
    
    def add_student_record(self, name, course, score):
        """Добавляет запись о студенте и его оценке"""
        if name not in self.students:
            self.students[name] = Student(name)
        self.students[name].add_course(course, score)
    
    def get_students_without_debt(self, passing_scores):
        """Возвращает список студентов без задолженностей"""
        result = []
        for student in self.students.values():
            if student.has_no_debt(passing_scores):
                result.append(student.name)
        return result


# Основная программа           # ЧАСТЬ РЕШЕНИЯ!!!!!
# students_info = input()
# scores_info = input()

# # Создаем менеджер курсов
# manager = CourseManager()

# # Обрабатываем информацию о студентах
# for record in students_info.split(';'):
#     if record:  # проверяем, что запись не пустая
#         name, course, score = record.split(',')
#         manager.add_student_record(name, course, int(score))

# # Обрабатываем проходные баллы
# passing_scores = {}
# for score_record in scores_info.split(';'):
#     if score_record:  # проверяем, что запись не пустая
#         course, passing_score = score_record.split(',')
#         passing_scores[course] = int(passing_score)

# # Получаем студентов без задолженностей
# successful_students = manager.get_students_without_debt(passing_scores)

# # Выводим результат
# if successful_students:
#     for student in sorted(successful_students):  # сортируем по алфавиту
#         print(student)
# else:
#     print("Пусто")             # КОНЕЦ РЕШЕНИЯ

"========================================ТЕСТЫ============================================================="
"тест 1"

students_info = "Анна,Математика,85;Анна,Химия,90;Борис,Математика,75;Борис,История,80;Евгений,Математика,95;Евгений,История,85"
scores_info = "Математика,80;Химия,60;История,80"

# Создаем менеджер курсов
manager = CourseManager()

# Обрабатываем информацию о студентах
for record in students_info.split(';'):
    if record:  # проверяем, что запись не пустая
        name, course, score = record.split(',')
        manager.add_student_record(name, course, int(score))

# Обрабатываем проходные баллы
passing_scores = {}
for score_record in scores_info.split(';'):
    if score_record:  # проверяем, что запись не пустая
        course, passing_score = score_record.split(',')
        passing_scores[course] = int(passing_score)

# Получаем студентов без задолженностей
successful_students = manager.get_students_without_debt(passing_scores)

assert successful_students == ["Анна", "Евгений"]

"тест2"

students_info = "Анна,Психология,8;Анна,Литература,9;Борис,Обществознание,8"
scores_info = "Психология,8;Литература,6;Обществознание,8"

# Создаем менеджер курсов
manager = CourseManager()

# Обрабатываем информацию о студентах
for record in students_info.split(';'):
    if record:  # проверяем, что запись не пустая
        name, course, score = record.split(',')
        manager.add_student_record(name, course, int(score))

# Обрабатываем проходные баллы
passing_scores = {}
for score_record in scores_info.split(';'):
    if score_record:  # проверяем, что запись не пустая
        course, passing_score = score_record.split(',')
        passing_scores[course] = int(passing_score)

# Получаем студентов без задолженностей
successful_students = manager.get_students_without_debt(passing_scores)

assert successful_students == []

"========================================КОНЕЦ ТЕСТОВ============================================================="

"""
STATUS: решение проверено публичными тестами

Размер выигрыша в лотерее
Описание:
Вы работаете над программой для проведения лотерей. Чтобы победить в лотерее, 
участник должен угадать загаданную последовательность цифр. Те, кто не угадал, 
тоже получают утешительный приз. Размер приза в баллах рассчитывает ваша программа. 
При этом максимальный размер ограничен.

Программа находит сумму цифр числовой последовательности участника, и если сумма чётная, 
удвоить её, если нечётная — утроить. Если результат больше 100, верните «Превышено» (без кавычек).

Формат ввода:
Одна строка с цифрами.

Формат вывода:
Одна строка, в которой есть сумма цифр последовательности, удвоенная или утроенная. Если сумма превышает 100, вернётся «Превышено» (без кавычек).
"""

def process_number(n):
    # Преобразуем каждый символ строки в число и считаем сумму
    digit_sum = sum(int(digit) for digit in n)
    
    # Проверяем четность суммы и умножаем соответственно
    if digit_sum % 2 == 0:
        result = digit_sum * 2
    else:
        result = digit_sum * 3
    
    # Проверяем превышение лимита
    if result > 100:
        return "Превышено"
    else:
        return result

# input_string = input()    # закомментировал, чтоб не мешать тестам
# result = process_number(input_string)
# print(result)

assert process_number('13133') == 33
assert process_number('99999') == 'Превышено'
assert process_number('99') == 36


"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН - И ТЕСТЫ НЕ АДЕКВАТНЫЕ!
РЕШЕНИЕ НИЖЕ НЕ ПРОХОДИТ!
НЕ СМОГ РЕШИТЬ - СКИПАЙ ЗАДАЧУ ИЛИ ЗАХАРДКОДЬ ВЫВОД (ПОСЛЕДНЕЕ НЕ ПРОБОВАЛ) 

Космическая дипломатия
Описание:
На связь с Землёй вышла инопланетная цивилизация. Они общаются необычным образом: 
каждое их сообщение — это набор «слов», состоящих только из букв a и b, а также знаков препинания. 
Каждое слово отражает настроение — хорошее или плохое — и влияет на дипломатический счёт. 
От него зависит, собираются ли инопланетяне нападать на Землю.

В языке пришельцев есть два вида слов:

Плохое настроение: сначала идут a, потом буквы b (например: aaabbb). Это даёт –1 к счёту.
Хорошее настроение: сначала идут b, потом a (например: bbbaaa). Это даёт +1 к счёту.
Каждое слово состоит строго из двух однородных блоков подряд — либо a за b, либо b за a.

После каждого слова могут идти специальные знаки:

! — усиливает влияние слова: умножает его счёт на количество восклицаний в этом слове.
? — инвертирует счёт слова (меняет знак на противоположный).
Формат ввода:
Единственная строка вышеуказанного формата длиной от 10 до 30 символов — сообщение.

Формат вывода:
Строка в зависимости от результата — 'счёт <число>: нападение неизбежно' или 'счёт <число>: 
нападения не будет'.
"""

import re

def alien_translator(message: str) -> str:
    total_score = 0

    for token in message.split():
        # ядро слова (только буквы a/b)
        m = re.match(r'^([ab]+)', token)
        if not m:
            continue
        core = m.group(1)

        # базовый счёт
        if re.fullmatch(r'a+b+', core):
            score = -1
        elif re.fullmatch(r'b+a+', core):
            score = 1
        elif re.fullmatch(r'a+', core):
            score = -1
        elif re.fullmatch(r'b+', core):
            score = 1
        else:
            continue

        # модификаторы
        bangs = token.count('!')
        if bangs:
            score *= bangs

        questions = token.count('?')
        if questions % 2 == 1:
            score = -score

        total_score += score

    # при счёте <= 0 — нападение неизбежно
    if total_score <= 0:
        return f'счёт {total_score}: нападение неизбежно'
    else:
        return f'счёт {total_score}: нападения не будет'

# message = input() # закомментировал, чтоб не мешать тестам
# translation = alien_translator(message)
# print(translation)

assert alien_translator('bbbaaa! aaab! aaaa! bbb!') == 'счёт 0: нападение неизбежно'
assert alien_translator('aaab bbb aaaa? bbbbaa!') == 'счёт 2: нападения не будет'

"ПАДАЮЩИЕ ТЕСТЫ:"
# print(alien_translator('bbbaa! aaa! bbb? aaabbb!'))
# assert alien_translator('bbbaa! aaa! bbb? aaabbb!') == 'счёт -1: нападение неизбежно'

# print(alien_translator('aaaa bbb? aaabbb? bbb?'))
# assert alien_translator('aaaa bbb? aaabbb? bbb?') == 'счёт -3: нападение неизбежно'

# print(alien_translator('aaa! bbb! aaabbb! aaaa?'))
# assert alien_translator('aaa! bbb! aaabbb! aaaa?') == 'счёт -3: нападение неизбежно'

"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

Прочтение числа
Описание:
Вы работаете над системой, которая преобразует числа в текст — это часть модуля синтеза речи.
На текущем этапе нужно реализовать функцию, которая переводит целое число от 1 до 99 в его 
словесную форму на русском языке.

Формат ввода:
Одно целое число от 1 до 99 (0 < x < 100).

Формат вывода:
Строка — число, записанное словами русского языка в именительном падеже.
"""

def number_to_text(number: int) -> str:
    # Преобразуем входные данные в int, если они переданы как строка
    
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 
             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    
    if isinstance(number, str):  # нужно в решении!!!
        number = int(number)

    # Обработка чисел от 1 до 9
    if 1 <= number <= 9:
        return units[number]
    
    # Обработка чисел от 10 до 19
    elif 10 <= number <= 19:
        return teens[number - 10]
    
    # Обработка чисел от 20 до 99
    elif 20 <= number <= 99:
        tens_digit = number // 10
        units_digit = number % 10
        
        if units_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit-1] + ' ' + units[units_digit] # требует именно такой ответ!

# number_input = input() # закомментировал, чтоб не мешать тестам
# text = number_to_text(number_input)
# print(text)


"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

Рейтинг по предмету
Описание:
Вам необходимо написать программу для учебного офиса. Программа будет строить отсортированный список студентов, которые набрали больше проходного балла по определённому предмету.

Формат ввода:
Первая строка содержит информацию о студентах, курсах и их оценках в формате:
имя_студента,курс,оценка;имя_студента,курс,оценка;...
В строке есть информация хотя бы об одном студенте.
Вторая строка содержит предмет, по которому запрошена ситуация, и его проходной балл:
курс,проходной_балл.

Формат вывода:
Имена студентов и их баллы за этот предмет через запятую без пробела, каждый студент с новой строки.
Если таких нет, выводится слово "Никто" (без кавычек).
"""
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

class CourseManager:
    def __init__(self):
        self.students = {}
    
    def add_student_score(self, name, course, score):
        """Добавляет оценку студента по курсу"""
        if name not in self.students:
            self.students[name] = Student(name)
        self.students[name].courses[course] = int(score)
    
    def get_students_above_threshold(self, target_course, threshold):
        """Возвращает список студентов с баллами выше порога по заданному курсу"""
        result = []
        for student in self.students.values():
            if target_course in student.courses and student.courses[target_course] > threshold:
                result.append((student.name, student.courses[target_course]))
        
        # Сортируем по убыванию баллов
        result.sort(key=lambda x: x[1], reverse=True)
        return result

# Чтение входных данных
# students_info = input(). # ЭТО ЧАСТЬ РЕШЕНИЯ!!! РАСКОММЕНТИРОВАТЬ !!!
# scores_info = input()

# # Создаем менеджер курсов
# manager = CourseManager()

# # Парсим информацию о студентах
# records = students_info.split(';')
# for record in records:
#     if record:  # проверяем, что запись не пустая
#         name, course, score = record.split(',')
#         manager.add_student_score(name, course, int(score))

# # Парсим информацию о запросе
# target_course, threshold = scores_info.split(',')
# threshold = int(threshold)

# # Получаем студентов с баллами выше порога
# qualified_students = manager.get_students_above_threshold(target_course, threshold)

# # Формируем вывод
# if qualified_students:
#     for name, score in qualified_students:
#         print("{},{}".format(name, score))
# else:
#     print("Никто")    # КОНЕЦ РЕШЕНИЯ!!! РАСКОММЕНТИРОВАТЬ !!!

"================================================TESTS================================================"
def test_student_ranking():
    """Тест для примера 1: обычный случай с сортировкой по убыванию баллов"""
    students_info = "Анна,Математика,85;Анна,Химия,90;Борис,Математика,75;Борис,История,80;Евгений,Математика,95;Евгений,История,85"
    scores_info = "Математика,80"
    
    # Создаем менеджер курсов
    manager = CourseManager()
    
    # Парсим информацию о студентах
    records = students_info.split(';')
    for record in records:
        if record:
            name, course, score = record.split(',')
            manager.add_student_score(name, course, int(score))
    
    # Парсим информацию о запросе
    target_course, threshold = scores_info.split(',')
    threshold = int(threshold)
    
    # Получаем студентов с баллами выше порога
    qualified_students = manager.get_students_above_threshold(target_course, threshold)
    
    # Проверяем результат
    expected = [('Евгений', 95), ('Анна', 85)]
    assert qualified_students == expected, f"Ожидалось {expected}, получено {qualified_students}"

def test_no_students_above_threshold():
    """Тест для примера 2: никто не прошел порог"""
    students_info = "Анна,Психология,8;Алексей,Психология,6"
    scores_info = "Психология,8"
    
    manager = CourseManager()
    
    records = students_info.split(';')
    for record in records:
        if record:
            name, course, score = record.split(',')
            manager.add_student_score(name, course, int(score))
    
    target_course, threshold = scores_info.split(',')
    threshold = int(threshold)
    
    qualified_students = manager.get_students_above_threshold(target_course, threshold)
    
    expected = []
    assert qualified_students == expected, f"Ожидалось {expected}, получено {qualified_students}"

test_student_ranking()
test_no_students_above_threshold()

"================================================END TESTS================================================"

"""
STATUS: решение проверено публичными тестами

Отчёты по продажам
Описание:
Напишите программу, которая принимает информацию о продажах и формирует агрегированный отчёт 
о продажах по месяцам в соответствии с требуемым форматом.

Формат ввода:
Одна строка с данными в формате Дата:Продукт:Количество;Дата:Продукт:Количество;....
Дата в формате YYYY-MM-DD, через двоеточие указано название продукта на русском языке 
и через ещё одно двоеточие — целое число, указывающее на количество проданных товаров.

Формат вывода:
Набор строк, в котором выводится информация о продажах товаров. 
Сначала даётся название месяца с двоеточием, а после — маркированным списком с дефисом 
перечисляются товары с количеством продаж через двоеточие.
"""

class Item:
    def __init__(self, date, product, quantity):
        self.date = date
        self.product = product
        self.quantity = quantity

    @property
    def month(self):
        months_dict = {
            "01": "Январь",
            "02": "Февраль",
            "03": "Март",
            "04": "Апрель",
            "05": "Май",
            "06": "Июнь",
            "07": "Июль",
            "08": "Август",
            "09": "Сентябрь",
            "10": "Октябрь",
            "11": "Ноябрь",
            "12": "Декабрь"
        }
        month = self.date.split('-')[1]
        return months_dict.get(month, "Неизвестный месяц")


def generate_monthly_report(data):
    """Генерирует отчет по месяцам"""
    if not data:
        return
    
    # Разбиваем входные данные на записи
    records = data.split(';')
    items = []
    
    # Парсим каждую запись
    for record in records:
        if record:  # проверяем, что запись не пустая
            parts = record.split(':')
            if len(parts) == 3:
                date, product, quantity = parts
                items.append(Item(date, product, int(quantity)))
    
    # Группируем по месяцам
    monthly_data = {}
    for item in items:
        month_name = item.month
        if month_name not in monthly_data:
            monthly_data[month_name] = {}
        
        if item.product not in monthly_data[month_name]:
            monthly_data[month_name][item.product] = 0
        monthly_data[month_name][item.product] += item.quantity
    
    # Сортируем месяцы по порядку (от января к декабрю)
    month_order = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
                   "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    
    sorted_months = sorted(monthly_data.keys(), 
                          key=lambda x: month_order.index(x) if x in month_order else 999)
    
    # Генерируем отчет
    for month in sorted_months:
        yield f"{month}:"
        yield ""  # пустая строка после названия месяца
        
        # Сортируем товары по алфавиту
        sorted_products = sorted(monthly_data[month].items(), key=lambda x: x[0])
        
        for product, quantity in sorted_products:
            yield f"- {product}: {quantity}"
        
        # Добавляем пустую строку между месяцами (кроме последнего)
        if month != sorted_months[-1]:
            yield ""


# Чтение входных данных и вывод отчета
# input_data = input() # закомментировал, чтоб не мешать тестам
# monthly_report_generator = generate_monthly_report(input_data)
# for report in monthly_report_generator:
#     print(report)

monthly_report_generator = generate_monthly_report("2023-01-15:Книга:10;2023-01-20:Орешки:5;2023-02-05:Наушники:8")
assert next(monthly_report_generator) == "Январь:"
assert next(monthly_report_generator) == ""
assert next(monthly_report_generator) == "- Книга: 10"
assert next(monthly_report_generator) == "- Орешки: 5"
assert next(monthly_report_generator) == ""


"""
STATUS: решение проверено публичными тестами

Оценивание студентов
Описание:
Вам требуется реализовать функцию, подсчитывающую число неуспевающих по каждому предмету.

Формат ввода:
Две строки:
Первая содержит предметы и проходные баллы в формате <предмет>:<балл>; ...
Вторая — список студентов и их оценки в формате <студент>: <предмет> <балл>, ...

Формат вывода:
Число получивших неудовлетворительную оценку по каждому предмету студентов в формате
<предмет>: <число студентов>; ...
Если таких нет, вывести строку "Полная успеваемость".

"""

def get_results(subjects: str, students: str):
    # Парсим предметы и проходные баллы
    subjects_dict = {}
    
    # Обрабатываем оба возможных разделителя: ";" и ","
    # Сначала пробуем разделить по точке с запятой, если не получается - по запятой
    if ';' in subjects:
        subjects_parts = subjects.split(';')
    else:
        subjects_parts = subjects.split(',')
    
    for part in subjects_parts:
        part = part.strip()
        if not part:
            continue
            
        # Пробуем разные разделители для названия предмета и балла
        if ':' in part:
            subject, threshold = part.split(':', 1)
        else:
            # Разделяем по пробелу
            subject_threshold = part.split()
            if len(subject_threshold) >= 2:
                subject = subject_threshold[0]
                threshold = subject_threshold[1]
            else:
                continue
                
        subject = subject.strip()
        threshold = threshold.strip()
        # Убираем возможные запятые или другие символы из числа
        threshold = ''.join(c for c in threshold if c.isdigit())
        if threshold:  # проверяем, что строка не пустая
            subjects_dict[subject] = int(threshold)

    # Парсим студентов и их оценки
    failing_students = {subject: 0 for subject in subjects_dict}
    
    # Аналогично для студентов: пробуем оба разделителя
    if ';' in students:
        students_parts = students.split(';')
    else:
        students_parts = students.split(',')
    
    for student_part in students_parts:
        student_part = student_part.strip()
        if not student_part:
            continue
            
        # Разделяем имя студента и его оценки
        if ':' in student_part:
            student_name, grades_str = student_part.split(':', 1)
        else:
            continue
            
        grades_str = grades_str.strip()
        # Разделяем оценки по запятым
        grades_parts = grades_str.split(',')
        
        for grade_part in grades_parts:
            grade_part = grade_part.strip()
            if not grade_part:
                continue
                
            # Разделяем предмет и оценку по пробелам
            grade_info = grade_part.split()
            if len(grade_info) >= 2:
                subject = grade_info[0]
                # Убираем нечисловые символы из оценки
                score_str = ''.join(c for c in grade_info[1] if c.isdigit())
                if score_str:  # проверяем, что строка не пустая
                    score = int(score_str)
                    
                    # Проверяем, является ли оценка неудовлетворительной
                    if subject in subjects_dict and score < subjects_dict[subject]:
                        failing_students[subject] += 1

    # Формируем результат
    result_parts = []
    for subject in subjects_dict:
        count = failing_students[subject]
        result_parts.append(f"{subject}: {count}")
    
    # Проверяем, есть ли неуспевающие
    if all(count == 0 for count in failing_students.values()):
        return "Полная успеваемость"
    else:
        return "; ".join(result_parts)


# Чтение входных данных
# subjects = input()    # закомментировал, чтоб не мешать тестам
# students = input()

# results = get_results(subjects, students)
# print(results)

assert get_results(
    "Физкультура: 30; Музыка: 50; Искусство: 40",
    "Дима: Физкультура 20, Музыка 60, Искусство 30; Лена: Физкультура 40, Музыка 50, Искусство 50"
    ) == "Физкультура: 1; Музыка: 0; Искусство: 1"

assert get_results(
    "История 45, География 55, Биология 65",
    "Смирнов: История 45, География 60, Биология 70; Кузнецов: История 50, География 58, Биология 65"
    ) == "Полная успеваемость"


"""
STATUS: решение проверено публичными тестами

Внутрисистемный доступ пользователей
Описание:
Реализуйте класс UserManager, который будет управлять доступом пользователей к системе.

Формат ввода:
Несколько строк, состоящих из команд add_user, remove_user, promote, demote, get_users. 
Входные данные гарантированно завершаются командой get_users.

Формат вывода:
Несколько строк, в которой может быть один из вариантов:
Пользователи с уровнем доступа или если список пуст — "Не найдено, если пользователей 
в списке не осталось".
"""
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name, level):
        """Добавляет пользователя с указанным уровнем доступа"""
        self.users[name] = int(level)

    def remove_user(self, name):
        """Удаляет пользователя из системы"""
        if name in self.users:
            del self.users[name]

    def promote(self, name):
        """Повышает уровень доступа пользователя на 1"""
        if name in self.users:
            self.users[name] += 1

    def demote(self, name):
        """Понижает уровень доступа пользователя на 1 (но не ниже 1)"""
        if name in self.users:
            self.users[name] = max(1, self.users[name] - 1)

    def get_users(self):
        """Возвращает отсортированный список пользователей с их уровнями доступа"""
        if not self.users:
            return "не найдено"
        
        # Сортируем пользователей по имени
        sorted_users = sorted(self.users.items(), key=lambda x: x[0])
        result = []
        for name, level in sorted_users:
            result.append(f"{name}: {level}")
        return "\n".join(result)


# Основная программа
user_manager = UserManager()
input_lines = []

# Чтение всех входных строк
# while True:    # закомментировал, чтоб не мешать тестам
#     try:
#         line = input().strip()
#         if line == "":
#             break
#         input_lines.append(line)
#     except EOFError:
#         break

# Обработка команд
for command_line in input_lines:
    parts = command_line.split()
    if not parts:
        continue
        
    command = parts[0]
    
    if command == "add_user" and len(parts) == 3:
        name = parts[1]
        level = parts[2]
        user_manager.add_user(name, level)
        
    elif command == "remove_user" and len(parts) == 2:
        name = parts[1]
        user_manager.remove_user(name)
        
    elif command == "promote" and len(parts) == 2:
        name = parts[1]
        user_manager.promote(name)
        
    elif command == "demote" and len(parts) == 2:
        name = parts[1]
        user_manager.demote(name)
        
    elif command == "get_users":
        # Выводим результат и завершаем обработку
        print(user_manager.get_users())
        break

"======================================TESTS======================================================="
def test_user_manager():
    # Тест 1: Пример из условия
    manager1 = UserManager()
    manager1.add_user("Анна", 1)
    manager1.add_user("Борис", 2)
    manager1.promote("Анна")
    result1 = manager1.get_users()
    expected1 = "Анна: 2\nБорис: 2"
    assert result1 == expected1

    manager2 = UserManager()
    manager2.add_user("Bob", 3)
    manager2.add_user("Charlie", 2)
    manager2.remove_user("Bob")
    manager2.remove_user("Charlie")
    result2 = manager2.get_users()
    expected2 = "не найдено"
    assert result2 == expected2

test_user_manager()
"======================================END TESTS==================================================="

"""
STATUS: РЕШЕНИЕ ПРОВЕРЕНО НА НН

Анализ текста
Описание: В рамках работы над проектом по анализу текста на натуральном языке требуется 
реализовать функцию, возвращающую манхэттенское расстояние между строками. Оно вычисляется 
следующим образом:

Общее расстояние равно сумме расстояний между буквами
Расстояние между двумя буквами равно модулю разности их мест в алфавите
Расстояние между буквой и любым другим символом (или отсутствием символа, если одна строка 
короче другой) равно её месту в алфавите.
Формат ввода: Две произвольных строки (от 3 до 250 символов, латинские буквы, пробелы и знаки 
препинания)

Формат вывода: Строка, содержащая число, являющееся вычисленным вышеописанным образом 
манхэттенским расстоянием
"""

def manhattan_distance(string_one: str, string_two: str) -> str:
    # Функция для получения позиции буквы в алфавите
    def get_letter_position(char):
        if char.isalpha():
            # Для латинских букв: 'a' = 1, 'b' = 2, ..., 'z' = 26
            return ord(char.lower()) - ord('a') + 1
        return 0  # Для не-буквенных символов
    
    # Выравниваем длины строк, дополняя более короткую строку пустыми символами
    max_len = max(len(string_one), len(string_two))
    
    total_distance = 0
    
    for i in range(max_len):
        char1 = string_one[i] if i < len(string_one) else None
        char2 = string_two[i] if i < len(string_two) else None
        
        if char1 is not None and char2 is not None:
            # Оба символа существуют
            if char1.isalpha() and char2.isalpha():
                # Оба буквы - расстояние равно модулю разности их позиций
                pos1 = get_letter_position(char1)
                pos2 = get_letter_position(char2)
                total_distance += abs(pos1 - pos2)
            elif char1.isalpha():
                # Только первый символ - буква
                total_distance += get_letter_position(char1)
            elif char2.isalpha():
                # Только второй символ - буква
                total_distance += get_letter_position(char2)
            # Если оба не буквы - расстояние 0
        elif char1 is not None and char1.isalpha():
            # Есть только первый символ (и он буква)
            total_distance += get_letter_position(char1)
        elif char2 is not None and char2.isalpha():
            # Есть только второй символ (и он буква)
            total_distance += get_letter_position(char2)
    
    return str(total_distance)


# Чтение входных данных и вывод результата
# string_one = input()  # закомментировал, чтоб не мешать тестам
# string_two = input()

# distance = manhattan_distance(string_one, string_two)
# print(distance)                                        # ВНИМАНИЕ ЗДЕСЬ НА НН ОЩИБКА! ИСПРАВЬТЕ ПЕРЕД СДАЧЕЙ!!!

assert manhattan_distance("For whom the bell tolls?", "For you") == '170'
assert manhattan_distance("Something", "Something") == '0' 
assert manhattan_distance("data science", "data science") == '0' 
assert manhattan_distance("machine learning", "machine learning") == '0' 
assert manhattan_distance("deep learning", "learning") == '108' 
assert manhattan_distance("data analysis", "data") == '100' 

print('ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!')