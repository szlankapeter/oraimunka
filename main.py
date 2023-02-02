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
    jatekosPont = [11, 5, 6]
    gepPontok = [7, 4, 5]
    print("Teszt(Játékos veszített --> 21 felett): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "játékos vesztett"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")

def jatekosVeszetettTeszt_2():
    jatekosPont = [11, 2, 5]
    gepPontok = [11, 5, 4]
    print("Teszt2(Játékos veszített --> Kevesebb pont): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "játékos vesztett"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")

def jatekosVeszetettTeszt_3():
    jatekosPont = [11, 4, 5]
    gepPontok = [11, 9]
    print("Teszt3(Játékos veszített --> Több lap): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "játékos vesztett"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")


def gepVeszetettTeszt():
    jatekosPont = [7, 4, 5]
    gepPontok = [11, 5, 6]
    print("Teszt(Gép veszített --> 21 felett): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "gép vesztett"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")
def gepVeszetettTeszt_2():
    jatekosPont = [11, 5, 4]
    gepPontok = [11, 2, 5]
    print("Teszt2(Gép veszített --> Kevesebb pont): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "gép vesztett"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")

def gepVeszetettTeszt_3():
    jatekosPont = [11, 9]
    gepPontok = [11, 4, 5]
    print("Teszt3(Játékos veszített --> Több lap): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "játékos vesztett"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")


def dontetlen_1():
    jatekosPont = [11, 9]
    gepPontok = [11, 9]
    print("Teszt(Döntetlen) --> Mindkettő nyert: ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "Döntetlen"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")
def dontetlen_2():
    jatekosPont = [11, 11]
    gepPontok = [11, 11]
    print("Teszt(Döntetlen) --> Mindkettő veszített: ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "Döntetlen"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")

def dontetlen_3():
    jatekosPont = [11, 10, 3]
    gepPontok = [11, 11]
    print("Teszt(Döntetlen) --> Mindkettő veszített(nem egyenlő lapszam): ")
    kapott = eredmeny(jatekosPont, gepPontok)
    vart = "Döntetlen"
    if kapott == vart:
        print("\tA teszt sikeres\n")
    else:
        print("\tA teszt sikertelen\n")

def tesztek():
    jatekosVeszetettTeszt()
    jatekosVeszetettTeszt_2()
    jatekosVeszetettTeszt_3()
    gepVeszetettTeszt()
    gepVeszetettTeszt_2()
    gepVeszetettTeszt_3()
    dontetlen_1()
    dontetlen_2()
    dontetlen_3()

tesztek()