"""ПРОСТРАНСТВО ДЛЯ РЕШЕНИЯ ЗАДАЧ С КОДОМ"""
import re

def alien_translator(message: str) -> str:
    words = message.split()
    total_score = 0
    
    for word in words:
        # Отделяем буквенную часть от знаков препинания
        letters_match = re.match(r'^[ab]+', word)
        if not letters_match:
            continue
            
        letters = letters_match.group()
        punctuation = word[len(letters):]
        
        # Проверяем, что слово состоит из двух однородных блоков
        if len(letters) < 2:
            continue
            
        # Проверяем формат: сначала один тип букв, потом другой
        first_char = letters[0]
        transition_index = -1
        
        for i in range(1, len(letters)):
            if letters[i] != first_char:
                transition_index = i
                break
        
        if transition_index == -1:
            continue  # Нет перехода между блоками
            
        # Проверяем, что после перехода все символы одинаковые
        second_block = letters[transition_index:]
        if len(set(second_block)) != 1:
            continue  # Второй блок не однородный
            
        # Определяем базовый счет
        if first_char == 'a':
            base_score = -1
        else:
            base_score = 1
        
        # Обработка модификаторов
        score = base_score
        
        # ! умножает на количество восклицательных знаков
        exclamation_count = punctuation.count('!')
        if exclamation_count > 0:
            score *= exclamation_count
        
        # ? инвертирует счет (умножает на -1)
        question_count = punctuation.count('?')
        if question_count > 0:
            # Каждый ? меняет знак, поэтому если нечетное количество - меняем знак
            if question_count % 2 == 1:
                score = -score
        
        total_score += score
    
    # Формируем результат
    if total_score <= 0:
        return "счёт {0}: нападение неизбежно".format(total_score)
    else:
        return "счёт {0}: нападения не будет".format(total_score)

# message = input()
# translation = alien_translator(message)
# print(translation)

assert alien_translator('bbbaa! aaa! bbb? aaabbb!') == 'счёт -1: нападение неизбежно'
assert alien_translator('aaaa bbb? aaabbb? bbb?') == 'счёт -3: нападение неизбежно'
assert alien_translator('aaa! bbb! aaabbb! aaaa?') == 'счёт -3: нападение неизбежно'
assert alien_translator('aaab bbb aaaa? bbbbaa!') == 'счёт 2: нападения не будет'
