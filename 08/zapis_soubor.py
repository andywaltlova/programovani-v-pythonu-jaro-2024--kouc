# 1 Dny v měsíci
# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.

with open('kalendar.txt', mode="w", encoding="utf-8") as output_file:
    for den in pocty_dni:
        print(den, file=output_file)


# 2 Vytvoření souboru
# Napište program, který se po spuštění zeptá na název souboru, který má vytvořit
# (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat.

soubor = input('Zadej cestu k souboru pro zapsani: ')
text = input('Zadej text ktery chces zapsat: ')

with open(f'data/{soubor}', mode="w", encoding="utf-8") as output_file:
    print(text, file=output_file)



# 3 Rozepsaná výplata
# Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou
# výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na terminál
# Poté program upravte tak, aby vypsal tyto výsledky do souboru

# hodinova_mzda = int(input('Zadej hodinovou mzdu: '))
# with open('vykaz.txt') as file:
#     vysledek = []
#     for line in file:
#         vyplata = int(line) * hodinova_mzda
#         print(vyplata)
#         vysledek.append(vyplata)

# print(vysledek)

# with open('vyplaty.txt', mode="w", encoding="utf-8") as output_file:
#     for vyplata in vysledek:
#         print(vyplata, file=output_file)