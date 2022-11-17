#Урок 7. Python: от простого к практике
#Задание : Создать телефонный справочник с возможностью импорта 
# и экспорта данных в нескольких форматах.


import time
import string
import secrets

print()
print("Телефонный справочник")


filename = "Tel_book.csv" 
myfile = open(filename, "a+") 
myfile.close
 

def main_menu(): 
    print( "\n ГЛАВНОЕ МЕНЮ \n") 
    print( "1. Все контакты") 
    print( "2. Новый контакт") 
    print( "3. Найти контакт") 
    print( "4. Выход") 
    choice = input("Выберите пункт: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Контакт не обнаружен") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter для продолжения") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter для продолжения") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter для продолжения") 
        main_menu() 
    elif choice == "4": 
        print("Спасибо, что используете Наш справочник!") 
    else: 
        print( "Введите заново \n") 
        enter = input("Нажмите Enter для продолжения")
        main_menu()
 
      
def searchcontact(): 
    searchname = input("Введите ИМЯ контакта: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print("Найден контакт: ", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print(f"Контакт {searchname} отсутствует в справочнике") 
 

def input_firstname(): 
    first = input("Введите ваше имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 

def input_lastname(): 
    last = input("Введите вашу фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname


def key_gen():
    alphabet = string.ascii_letters + string.digits
    key = ''.join(secrets.choice(alphabet) for i in range(4))
    return key
key = key_gen()
  
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input("Введите ваш номер телефона: ") 
    emailID = input("Введите ваш E-mail: ") 
    contactDetails =(f"{key};" + firstname + " " + lastname + ";" + phoneNum + ";" + emailID +  "\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print("Новая запись : \n " + contactDetails + " успешно создана!")  
 
main_menu()
time.sleep(5)