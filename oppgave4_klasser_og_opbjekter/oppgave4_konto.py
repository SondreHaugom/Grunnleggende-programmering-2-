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
        rente = self.saldo * self.rentesats / 100
        self.saldo += rente
        print(f"Renter på {self.rentesats}% er lagt til. Ny saldo: {self.saldo} kr")
        



konto1 = Konto("Ola", 1000) # Ola`s saldo endrer seg ikke for saldo får ikke en verdi som blir endret.
konto2 = Sparekonto("Kari", 500, 3.0)
konto3 = Konto("Per", 300)
konto4 = Sparekonto("Pål", 800, 3.0)


kontoer = [konto1, konto2, konto3, konto4]
#print(kontoer)



def total_saldo(kontoer):
    total = 0
    for konto in kontoer:
        print(konto)
total_saldo(kontoer)
