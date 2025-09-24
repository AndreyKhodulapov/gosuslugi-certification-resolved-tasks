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
STATUS: решение проверено публичными тестами

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

import re

def alien_translator(message: str) -> str:
    words = message.split()
    total_score = 0
    
    for word in words:
        # Проверяем, что слово соответствует формату (только a и b в двух блоках)
        if not re.match(r'^[ab]+[!?]*$', word):
            continue
            
        # Отделяем буквенную часть от знаков препинания
        letters_match = re.match(r'^[ab]+', word)
        letters = letters_match.group()
        punctuation = word[len(letters):]
        
        # Проверяем, что слово состоит из двух однородных блоков
        # Находим границу перехода от a к b или от b к a
        transition_found = False
        for i in range(1, len(letters)):
            if letters[i] != letters[0]:
                # Проверяем, что после перехода все символы одинаковые
                if len(set(letters[i:])) == 1:
                    transition_found = True
                break
        
        if not transition_found:
            # Если нет перехода, пропускаем некорректное слово
            continue
        
        # Определяем базовый счет по первой букве
        if letters.startswith('a'):
            base_score = -1
        else:  # начинается с 'b'
            base_score = 1
        
        # Подсчитываем знаки препинания
        exclamation_count = punctuation.count('!')
        question_count = punctuation.count('?')
        
        # Применяем модификаторы согласно условию:
        # 1. Сначала базовый счет
        score = base_score
        
        # 2. ! умножает на количество восклицательных знаков
        if exclamation_count > 0:
            score *= exclamation_count
        
        # 3. ? инвертирует счет (умножает на -1 за каждый знак вопроса)
        # Если нечетное количество ? - знак меняется, если четное - возвращается к исходному
        if question_count % 2 == 1:
            score = -score
        
        total_score += score
    
    # Формируем результат
    if total_score <= 0:
        return f'счёт {total_score}: нападение неизбежно'
    else:
        return f'счёт {total_score}: нападения не будет'

# message = input() # закомментировал, чтоб не мешать тестам
# translation = alien_translator(message)
# print(translation)

assert alien_translator('bbbaaa! aaab! aaaa! bbb!') == 'счёт 0: нападение неизбежно'
assert alien_translator('aaabbb?!!!??? bbba! ba') == 'счёт -1: нападение неизбежно'

"""
STATUS: решение проверено публичными тестами

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
    if isinstance(number, str):
        number = int(number)
    
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 
             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    
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
            return f"{tens[tens_digit]} {units[units_digit]}"

# number_input = input() # закомментировал, чтоб не мешать тестам
# text = number_to_text(number_input)
# print(text)

assert number_to_text('1') == 'один'
assert number_to_text('34') == 'тридцать четыре'
assert number_to_text('67') == 'шестьдесят семь'

"""
STATUS: решение проверено публичными тестами

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
students_info = input()
scores_info = input()

# Создаем менеджер курсов
manager = CourseManager()

# Парсим информацию о студентах
records = students_info.split(';')
for record in records:
    if record:  # проверяем, что запись не пустая
        name, course, score = record.split(',')
        manager.add_student_score(name, course, int(score))

# Парсим информацию о запросе
target_course, threshold = scores_info.split(',')
threshold = int(threshold)

# Получаем студентов с баллами выше порога
qualified_students = manager.get_students_above_threshold(target_course, threshold)

# Формируем вывод
if qualified_students:
    for name, score in qualified_students:
        print(f"{name},{score}")
else:
    print("Никто")


# TODO добавить тесты


print('ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!')