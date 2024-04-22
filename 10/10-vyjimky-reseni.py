# 1 Ošetření dělení nulou
# Vytvoř program, který vypíše výsledek dělení těchto čísel.
# Program se postupně zeptá na dvě čísla (mohou být celá i desetinná).
# Vyděl tato čísla mezi sebou a vypiš výsledek dělení. Ošetři, aby program nezhavaroval při pokusu o dělení nulou.
# V tomto případě nemusíš ošetřovat zadání nečíselného vstupu, ošetření více výjimek v jednom bloku si ukážeme v další části.
import sys

cislo_a = float(input("Zadej první číslo: "))
cislo_b = float(input("Zadej druhé číslo: "))

# Zkusim a uvidim
try:
    vysledek = cislo_a / cislo_b
except ZeroDivisionError:
    print("Nulou nelze dělit.")
    sys.exit()

# Nejdriv osetrim a pak provedu
if cislo_b == 0:
    print("Nulou nelze dělit.")
    sys.exit()
else:
    vysledek = cislo_a / cislo_b

print(vysledek)


# 2 Čtení ze seznamu
# Uvažuj program, který čte knížku ze seznamu na základě indexu. Ošetři s použitím výjimky možnou chybu, že program skončí chybou.

knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]


# Zkusim a chytnu vyjimku
try:
    index = int(input("Zadej index knihy: "))
    print(knihy[index])
except IndexError as exception: # Muzu si ulozit detail vyjimky do promenne
    print(exception)
    print("Zadejte prosím číslo.")
    sys.exit()

# Osetrim a pak provedu
if index >= len(knihy):
    print("Zadaný index neexistuje.")
    sys.exit()
else:
    print(knihy[index])


# [BONUS] 3 Datum
# Požádej uživatele o zadání data narození ve formátu RRRR-MM-DD.

# Nejprve ověř pomocí podmínek, že je zadáno správné datum - tj. v datu jsou dvě pomlčky
# a po rozdělení na jednotlivé části obsahuje každá z částí číslo.
# Stále je ale možné, že je zadáno nesmyslné datum. Například je možné zadat datum 31. dubna nebo 29. února pro nepřestupný rok.
# Proto přidej modul datetime a pomocí metody fromisoformat() vyzkoušej převod na typ datetime.
# Ošetři ValueError, která může být způsobena výše uvedenými případy.

# Zase vice zpusobu, ale treba takto:

import sys
from datetime import datetime

datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")

for cast in datum_narozeni.split("-"):
    if not cast.isdigit():
        print("Datum musí obsahovat pouze číslice a pomlčky.")
        sys.exit()

if datum_narozeni.count("-") != 2 :
    print("Datum musí být oddělené pomlčkami.")
    sys.exit()

try:
    datum_narozeni = datetime.fromisoformat(datum_narozeni)
except ValueError:
    print("Zadané datum je ve patnem formatu.", datum_narozeni)
    sys.exit()