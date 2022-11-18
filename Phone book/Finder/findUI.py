def Fnder_SrNM():
    a = input('Введите фамилию: ')
    return a

def Print_Search_Res(matrx):
    if matrx ==[]: print('По Вашему запросу ничего не найдено')
    else: print('Результаты поиска: ')
    for item in matrx:
        print(item)