#Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
#(значения от -100 до 100)
#многочлена и записать в файл многочлен степени k
#k - максимальная степень многочлена, следующий степень следующего на 1 
#меньше и так до ноля
#Коэффициенты расставляет random, поэтому при коэффициенте 0 
#просто пропускаем данную итерацию степени
#Записываем результат в файл.

#Пример:
#k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
#k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


from random import randint, choice
k = int(input("Введите степень : "))
variable = "x"
result = ""
def make_formula(degree, v, res, i):
    coefficient = (str(randint(-100, 100))+"*") * randint(0, 1)
    res = coefficient + variable + "**" + str(i) + res
    return res
def random_formula(degree, v, res):
    while degree == 0:
        print("Ошибка степень не должна быть 0")
        print("Для выхода необходимо нажать Ctrl+c")
        degree = int(input("Введите степень : "))
    lib_char = ["+", "-"]
    for i in range(1, degree + 1):
        char = choice(lib_char)
        if i == degree:
            if degree == 1:
                res = make_formula(degree, v, res, i)[:-3]
            else:
                res = make_formula(degree, v, res, i)
        elif bool(randint(0, 1)):
            continue
        else:
            if i == 1:
                res = char + make_formula(degree, v, res, i)[:-3]
            else:
                res = char + make_formula(degree, v, res, i)
    res = res + (char + str(randint(-100, 100))) * randint(0, 1) + "=0"
    return res
result = random_formula(k, variable, result)
print(result)
data = open("file_task 4.txt", "a")
data.write(result + "\n")
data.close()