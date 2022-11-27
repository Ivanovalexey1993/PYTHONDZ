from datetime import datetime as dt
from menu import dict_log


def get_log(result, operation):
    dtime = dt.now()
    with open('history.txt', 'a', encoding = 'UTF - 8') as file:
        file.write('{}; операция: {}; результат: {}\n'.format(
            dtime, operation, result))