class Konto:
    def __init__(self, eier, saldo=0,):
        self.eier = eier
        self.saldo = saldo


    def sett_inn(self, belop=0):
        if belop < 0:
            print(f"Du kan ikke sette inn et negativt beløp. {belop} kr er ikke gyldig.")
        else:
            self.saldo += belop
            print(f"{belop} kr er satt inn. Ny saldo: {self.saldo} kr")


    
    def ta_ut(self, belop=0):
        if belop > self.saldo:
            print(f"Du kan ikke ta ut mer enn det du har på kontoen. {belop} kr er ikke gyldig.")
        elif belop < 0:
            print(f"Du kan ikke ta ut et negativt beløp. {belop} kr er ikke gyldig.")
        else:
            self.saldo -= belop
            print(f"{belop} kr er tatt ut. Ny saldo: {self.saldo} kr")

    def __str__(self):
        return f"{self.eier}: {self.saldo} kr"

class Sparekonto(Konto):
    def __init__(self, eier, saldo=0, rentesats=2.5):
        super().__init__(eier, saldo)
        self.rentesats = rentesats


    def legg_til_renter(self):
        
        


"""
ola = Konto("Ola") # Ola`s saldo endrer seg ikke for saldo får ikke en verdi som blir endret.
kari = Konto("Kari", 500)
kari.ta_ut(300)
kari.ta_ut(1000)
kari.sett_inn(-50)
print(kari)

"""

sparing = Sparekonto("Kari", 1000, 3.0)
sparing.sett_inn(500)
sparing.legg_til_renter()
print(sparing)


