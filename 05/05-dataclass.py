# 1. Balik jako datova trida

# Uprav třídu Package na datovou třídu. Třída bude mít atributy address, weight, a state.
# U každého z atributů vymysli a nastav vhodný datový typ. Existující metody ve třídě ponech.

# Následně vyzkoušej, zda funguje vytváření balíků. A co cenné balíky, fungují pořád, i když dědí od datové třídy?

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Adresa: {self.address} ({self.weight} Kg) - {self.state}"

    def delivery_price(self):
        if self.weight < 10:
            cena = 129
        elif self.weight < 20:
            cena = 159
        else:
            cena = 359
        return cena

    def deliver(self):
        if self.state == 'nedoruceno':
            self.state = 'doruceno'
            return 'Balik dorucen.'
        else:
            return f'Balik na adresu {self.address} jiz byl dorucen.'
