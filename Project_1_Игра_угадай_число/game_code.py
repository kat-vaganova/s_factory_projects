import numpy as np

my_min = 1
my_max = 101


def guess_numbers(start, end):
    """ Функция рандомно загадывающая число

    Args:
        start (int): нижняя граница для загадывания числа
        end (int): верхняя граница для загадывания числа

    Returns:
        int: загаданное число
    """
    guess_number = np.random.randint(start, end)
    # print (f' загаданное число {guess_number}')
    return guess_number


def predict_number(guess_numbers):
    """Рандомно угадываем число

    Args:
        guess_numbers: функция рандомно загадывающая число

    Returns:
        int: Число попыток
    """
    start = my_min
    end = my_max
    try_count = 0
    middle_number = (my_min + my_max) // 2
    guess_number = guess_numbers(my_min, my_max)

    while True:
        try_count += 1
        find_number = np.random.randint(start, end)
        if find_number == guess_number:
            # print(find_number)
            break
        elif find_number > guess_number >= middle_number:
            start = middle_number
            end = find_number
            # print(f'1 - {find_number}, start={start}, end={end} ')
        elif find_number > guess_number and guess_number < middle_number:
            end = find_number
            # print(f'2 - {find_number}, start={start}, end={end} ')
        elif find_number < guess_number < middle_number:
            start = find_number
            end = middle_number
            # print(f'3 - {find_number}, start={start}, end={end}, загаданное число {guess_number} ')
        else:
            start = find_number
    #         print(f'4 - {find_number}, start={start}, end={end} ')
    # print(f' кол-во попыток {try_count}')
    return try_count

# predict_number(guess_numbers)


def score_game(predict_number) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_number: функция угадывания

    Returns:
        int: среднее количество попыток
    """
    # np.random.seed(1)
    count_ls = []

    while len(count_ls) < 1000:
        count_ls.append(predict_number(guess_numbers))

    score = int(np.mean(count_ls))
    # print(f' count_ls {count_ls}')
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")

    return score


score_game(predict_number)
