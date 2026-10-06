"""
Oppgave 3 - Feilsøking
======================

Dette er et lite utstyrslager, skrevet uten klasser. Det ser fornuftig ut,
og det gjør noe. Det gjør bare ikke helt det det skal.

Det ligger SEKS feil i programmet. Noen krasjer. Noen gir bare feil svar,
stille, uten at noe ser galt ut.

Programmet skal IKKE skrives om fra bunnen. Det skal repareres.

Jobb systematisk:
  1. Les koden før du kjører den. Hva TROR du skjer?
  2. Kjør den. Stemte det?
  3. Dann en hypotese om hva som er galt, og hvor.
  4. Test hypotesen - gjerne med en print eller et lite eksempel.
  5. Rett, og kjør på nytt.

Fyll ut FEILLOGG.md underveis, ikke etterpå.
"""

# Hvert utstyr: [id, navn, dagspris, dager_utlaant, utlaant_til]
LAGER = [
    ["PC-042", "Dell Latitude", 10.7, 3, "Kari"],
    ["SKJ-011", "Skjerm 27 tomme", 4.0, 0, None],
    ["TAST-100", "Tastatur", 2.0, 0, None],
    ["PC-043", "Dell Latitude", 10.7, 45, "Ola"],
    ["PRO-002", "Projektor", 30.0, 9, "Mats"],
    ["MUS-100", "Mus", 1.0, 120, "Robin"],
]

# Dagspriser slik de kommer inn fra det gamle økonomisystemet, som tekst
PRISLISTE = [
    ["PC-042", 10.7],
    ["PRO-002", 30.0],
    ["MUS-100", 1.0],
    ["SKJ-011", 4.0],
]

# Utlån som totalt koster nøyaktig dette beløpet dekkes av avdelingen
FRITAKSBELOEP = 32.1


def skriv_lager(lager):
    """Skriver ut alt utstyret i lageret."""
    print("--- Lagerliste ---")
    for i in range(len(lager) - 1):
        utstyr = lager[i]
        if utstyr[4] is None:
            print(utstyr[0], utstyr[1], "- på lager")
        else:
            print(utstyr[0], utstyr[1], "- utlånt til", utstyr[4])


def finn_utstyr(lager, utstyrs_id = LAGER[0][0]):
    """Finner utstyret med gitt id, eller None hvis det ikke finnes."""
    for utstyr in lager:
        if utstyr[0] == utstyrs_id:
            return utstyr
    return None


def purrestatus(dager):
    """Hvor alvorlig er det at utstyret ikke er levert inn?"""
    if dager > 7:
        return "purring"
    elif dager > 30:
        return "til inkasso"
    elif dager > 0:
        return "utlånt"
    else:
        return "på lager"


def fjern_tilgjengelig(lager):
    """Plukker ut det som står på lager, så bare aktive utlån blir igjen."""
    for utstyr in lager:
        if utstyr[4] is None:
            lager.remove(utstyr)
    return lager


def dyreste(prisliste = PRISLISTE):
    """Finner utstyret med høyest dagspris."""
    beste = prisliste[0]
    for rad in prisliste:
        if rad[1] > beste[1]:
            beste = rad
    return beste


def total_kostnad(dagspris, dager):
    """Summerer dagsprisen for hver dag utstyret har vært utlånt."""
    total = 0.0
    for _ in range(dager):
        total = total + dagspris
    return total


def skal_faktureres(total):
    """Beløp som er nøyaktig lik fritaksbeløpet skal ikke faktureres."""
    if total == FRITAKSBELOEP:
        return False
    return True


def snitt_dager(lager):
    """Gjennomsnittlig antall dager for utstyret som faktisk er utlånt."""
    sum_dager = 0
    antall = 0
    for utstyr in lager:
        if utstyr[3] > 0:
            sum_dager = sum_dager + utstyr[3]
        antall = antall + 1
    return sum_dager / antall


def main():
    skriv_lager(LAGER)

    print()
    print("--- Purrestatus ---")
    for utstyr in LAGER:
        print(utstyr[0], "->", purrestatus(utstyr[3]))

    print()
    print("--- Snitt dager utlånt ---")
    print(round(snitt_dager(LAGER), 1))

    print()
    print("--- Dyreste utstyr ---")
    print(dyreste(prisliste = PRISLISTE))

    print()
    print("--- Fakturering ---")
    for utstyr in LAGER:
        total = total_kostnad(utstyr[2], utstyr[3])
        print(utstyr[0], round(total, 2), "faktureres:", skal_faktureres(total))

    print()
    print("--- Aktive utlån ---")
    aktive = fjern_tilgjengelig(list(LAGER))
    for utstyr in aktive:
        print(utstyr[0], "->", utstyr[4])

    print()
    print("--- Oppslag ---")
    funnet = finn_utstyr(LAGER, utstyrs_id = LAGER[0][0] )  
    print("Fant:", funnet[1])


if __name__ == "__main__":
    main()
