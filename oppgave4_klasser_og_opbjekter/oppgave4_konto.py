class Konto:
    def __init__(self, eier, saldo=0,):
        self.eier = eier
        self.saldo = saldo


    def __str__(self):
        return f"{self.eier}: {self.saldo} kr"

kari = Konto("Kari", 500)
ola = Konto("Ola") # Ola`s saldo endrer seg ikke for saldo blir aldri kalt og har ingen verdi som enderer den
kari.saldo = kari.saldo + 100
print(kari)
print(ola)



