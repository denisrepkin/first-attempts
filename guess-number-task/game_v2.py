"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number:int=1)-> int:
    """Функция реализующая алгоритм бинарного поиска 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    low_n = 1 # Нижняя граница интервала
    high_n = 101 # Верхняя граница интервала
    mid = 0 # Средний элемент
    predict_number = int(np.random.randint(1, 101))
    while predict_number != number:
        count += 1
        if predict_number > number:
           high_n = predict_number
           predict_number = (high_n + low_n) // 2
        elif predict_number < number:
           low_n = predict_number
           predict_number = (high_n + low_n) // 2
        else:
            break
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
