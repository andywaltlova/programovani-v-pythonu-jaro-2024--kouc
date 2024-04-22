# 1 Výplata přesněji
# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin,
# což není příliš realistické. Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na každém
# řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
# Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte
# celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.


with open('vykaz.txt') as file:
    hodiny = []
    for line in file:
        hodiny.append(int(line))

# hodinova_mzda = int(input("Zadej hodinovou mzdu: "))

# vyplata_rok = sum(hodiny) * hodinova_mzda
# prumer_mesic = vyplata_rok / len(hodiny)


with open('vykaz.txt') as file:
    soucet = 0
    for line in file:
        soucet += int(line)

# hodinova_mzda = int(input("Zadej hodinovou mzdu: "))

# vyplata_rok = soucet * hodinova_mzda
# prumer_mesic = vyplata_rok / 12

# print(sum(hodiny))
# print(vyplata_rok)
# print(prumer_mesic)


# 2 Počet slov
# Stáhněte si odevzdanou slohovou práci. Zadání bylo sepsat text o nejméně 150ti
# slovech pojednávající o našem hlavním městě. Napište program, který spočítá počet slov
# v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
# Vypište na výstup počty slov na každém řádku
# Vypište na výstup celkový počet všech slov v souboru


with open('praha.txt', encoding='utf-8') as file:
    # radky = file.readlines()

    soucet = 0
    for line in file:
        pocet_slov_na_radku = len(line.split())
        print(pocet_slov_na_radku)
        soucet += pocet_slov_na_radku

print('Celkovy pocet slov v souboru:', soucet)









# [BONUS] 3.Půjčovna
# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit,
# kolik všechna auta najezdila dohromady kilometrů. V souboru auta.txt je pro každou SPZ
# zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů.
# Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

# Napište program, který na výstup vypíše součet všech ujetých kilometrů.
# Jistě se vám bude hodit metoda řetězců jménem replace().