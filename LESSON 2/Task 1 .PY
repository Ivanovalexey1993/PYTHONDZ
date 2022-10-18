#1) Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

#*Пример:*

#- 6782 -> 23
#- 0,56 -> 11


a = input('Введите число ')

def summa(a):                            
    if float(a) < 0:                            
        a = float(a) * (-1)
    number = 0

    for i in str(a):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(a)}')