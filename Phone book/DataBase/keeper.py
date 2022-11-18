def Sav_Dt(matr, f):
    if f == 1:
        with open(r'C:\Users\Dns\Desktop\Python home work\Phone book\DataBase\Data.txt','a') as dt:
            for i in range(len(matr)):
                for item in matr[i]:
                    dt.write(item)
                    dt.write(' ')
                dt.write(';')
                dt.write('\n')
    elif f == 2:
        with open(r'C:\Users\Dns\Desktop\Python home work\Phone book\DataBase\Data.csv','a') as dt:
            for i in range(len(matr)):
                for item in matr[i]:
                    dt.write(item)
                    dt.write('\n')
                dt.write(' ')
                dt.write('\n')
