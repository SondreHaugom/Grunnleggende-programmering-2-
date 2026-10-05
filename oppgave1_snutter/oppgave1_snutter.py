"""
Oppgave 1 - Les koden som en datamaskin
=======================================

IKKE kjør denne fila før du har fylt ut sporingstabellene.

Fyll ut en tabell per snutt: en rad per gjennomløp av løkka, en kolonne per
variabel, og til slutt hva du tror blir skrevet ut.

Skriv ned svaret ditt FØR du kjører noe. En gjetning du har forpliktet deg
til på papir lærer deg mye mer enn en du justerer underveis.

Kjør en snutt av gangen slik:

    python oppgave1_snutter.py 1
    python oppgave1_snutter.py 2

Snutt 6 er ekstra og helt valgfri.
"""

import sys


# --------------------------------------------------------------------------
# Snutt 1
# --------------------------------------------------------------------------
def snutt_1():
    total = 0
    for i in range(1, 6):
        total = total + i
        if total > 6:
           total = total - 2
    print(total)


# --------------------------------------------------------------------------
# Snutt 2
# --------------------------------------------------------------------------
def snutt_2():
    tekst = "banan"
    resultat = ""
    i = len(tekst) - 1
    while i >= 0:
        if tekst[i] != "a":
            resultat = resultat + tekst[i]
        i = i - 2
    print(resultat)


# --------------------------------------------------------------------------
# Snutt 3
# --------------------------------------------------------------------------
def snutt_3():
    a = [1, 2, 3]
    b = a
    b.append(4)
    c = a[:]
    c.append(5)
    print(a)
    print(b)
    print(c)


# --------------------------------------------------------------------------
# Snutt 4
# --------------------------------------------------------------------------
def snutt_4():
    for i in range(1, 4):
        for j in range(1, 4):
            if i * j > 4:
                break
            print(i, j)


# --------------------------------------------------------------------------
# Snutt 5
# --------------------------------------------------------------------------
def snutt_5():
    def endre(tall, liste):
        tall = tall + 10
        liste.append(10)

    x = 5
    y = [5]
    endre(x, y)
    print(x)
    print(y)


# --------------------------------------------------------------------------
# Snutt 6 - ekstra, valgfri
# --------------------------------------------------------------------------
def snutt_6():
    def legg_til(vare, kurv=[]):
        kurv.append(vare)
        return kurv

    print(legg_til("melk"))
    print(legg_til("brød"))
    print(legg_til("ost", ["egg"]))
    print(legg_til("juice"))


SNUTTER = {
    "1": snutt_1,
    "2": snutt_2,
    "3": snutt_3,
    "4": snutt_4,
    "5": snutt_5,
    "6": snutt_6,
}


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in SNUTTER:
        print("Bruk: python oppgave1_snutter.py <1-6>")
        sys.exit(1)
    SNUTTER[sys.argv[1]]()
