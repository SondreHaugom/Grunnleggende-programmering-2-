class Konto:
    def __init__(self, eier, saldo=0):
        self.eier = eier
        self.saldo = saldo

    def __str__(self):
        return f"{self.eier}: {self.saldo} kr"