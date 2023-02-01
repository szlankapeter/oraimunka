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
    gepPontok = [7, 4, 5, 3]
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "játékos vesztett"
    if kapott == vart:
        print("A teszt sikeres")
    else:
        print("A teszt sikertelen")


def gepVeszetettTeszt():
    jatekosPont = [7, 4, 5, 3]
    gepPontok = [9, 9, 9, 9]
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "gép vesztett"
    if kapott == vart:
        print("A teszt sikeres")
    else:
        print("A teszt sikertelen")

def dontetlen():
    jatekosPont = [7, 4, 5, 3]
    gepPontok = [7, 4, 5, 3]
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "döntetlen"
    if kapott == vart:
        print("A teszt sikeres")
    else:
        print("A teszt sikertelen")
def mindenkiVesztett():
    jatekosPont = [9, 9, 9, 9]
    gepPontok = [9, 9, 9, 8]
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "mindkettő vesztett"
    if kapott == vart:
        print("A teszt sikeres")
    else:
        print("A teszt sikertelen")


def tesztek():
    jatekosVeszetettTeszt()
    gepVeszetettTeszt()
    dontetlen()
    mindenkiVesztett()

tesztek()