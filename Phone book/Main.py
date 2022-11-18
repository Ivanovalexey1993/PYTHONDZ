import ContrDB as CDB
import ContrFind as CF

while True:
    print('===========================================')
    print('Выберите режим работы со справочником')
    print('1 - Создание новой записи')
    print('2 - Поиск по фамилии')
    print('3 - Вывести на экран все записи')
    k = int(input())
    if k ==1: CDB.DB_Add()
    elif k ==2: CF.Fnd_Smbd(k)
    elif k ==3: CF.Fnd_Smbd(k)
    else: print('Введите 1, 2 или 3')