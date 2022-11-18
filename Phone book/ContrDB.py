import DataBase.View as View
import DataBase.formtUI as Ft
import DataBase.keeper as K

def DB_Add():
    b = View.Nov_Dta_UI()
    f = Ft.Choos_Form()
    K.Sav_Dt(b,f)