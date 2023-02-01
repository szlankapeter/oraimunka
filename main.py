#megoldas
def eredmeny(jPont, gPont):
    if pontOszz(jPont) > 21:
        return "játékos vesztett"
    if pontOszz(gPont) > 21:
        return "gép vesztett"

def pontOszz(tomb):
    osszeg = 0
    i = 0
    pont = 0
    while i < len(tomb):
        osszeg += tomb[i]
        i += 1
    return osszeg
#teszteset

def jatekosVeszetettTeszt():
    jatekosPont = [9, 9, 9, 9]
    gepPontok = [1, 1, 1, 1]
    print(eredmeny(jatekosPont, gepPontok))

def tesztek():
    jatekosVeszetettTeszt()

tesztek()