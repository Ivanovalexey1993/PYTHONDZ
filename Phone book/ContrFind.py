import Finder.findUI as UI
import Finder.fnder as F

def Fnd_Smbd(m):
    if m == 3:
        nm=''
        UI.Print_Search_Res(F.fnd_srnm(nm))
    else:
        nm = UI.Fnder_SrNM()
        UI.Print_Search_Res(F.fnd_srnm(nm))