# 1 Kostky
# Vytvoř jednoduchou hru, která simuluje hodu třemi kostkami.

# Na začátku hry uživatel zadá částku, kterou chce vsadit, a jestli sází na sudý nebo lichý součet.
# Pomocí funkce randint z modulu random vygeneruj tři čísla v rozsahu 1 až 6 a vypočti jejich součet.
# Pokud uživatel vsadil správně, vypiš, že vyhrává dvojnásobek. V opačném případě vypiš, že nevyhrává nic.

# Všechny důležité události v průběhu hry by měly být zaznamenány pomocí logování. To zahrnuje:

# začátek a konec hry (úroveň DEBUG),
# výši sázky a číslo, na které uživatel vsadil (úroveň DEBUG),
# výsledek hodů a výsledek hry (výhra/prohra, úroveň INFO).
# Vytvoř vlastní formát logovacích zpráv, který bude obsahovat časové razítko, úroveň logování,
# název souboru, číslo řádku, název funkce a logovací zprávu. Nastav logger tak, aby logovací zprávy byly ukládány do souboru game.log.

import logging
import random
import argparse
import sys


def hod_kostkou():
    return random.randint(1, 6)

def soucet_hodu():
    hody = hod_kostkou() + hod_kostkou() + hod_kostkou()
    logging.info(f"Hody: {hody}")
    return hody

def get_sazka():
    castka = int(input("Zadej částku, kterou chceš vsadit: "))
    sude_liche = input("Na co sázíš? (sudy/lichy): ")
    logging.info("Vsadil si %s Kč na %s", castka, sude_liche)
    return castka, sude_liche

def hraj():
    logging.debug("Začátek hry")

    # vysledek = get_sazka()
    # sazka = vysledek[0]
    # sude_liche = vysledek[1]

    # unpacking
    sazka, sude_liche = get_sazka()
    hody = soucet_hodu()
    vyhra = (hody % 2 == 0 and sude_liche == "sudy") or (hody % 2 != 0 and sude_liche == "lichy")
    if vyhra:
        logging.info(f"Vyhráno: {sazka * 2}")
    else:
        logging.info(f"Prohráno: {sazka}")

    logging.debug("Konec hry")

################################################################################

# argparser = argparse.ArgumentParser(description="Hraješ hru s kostkami")
# argparser.add_argument("--log", help="Zadej úroveň logování", default="DEBUG")
# argparser.add_argument("--file", help="Zadej název souboru pro logování", default="game.log")
# args = argparser.parse_args()

logging.basicConfig(
    filename="game.log",
    # filename=args.file  # zadano jako parametr pri spusteni
    # stream=sys.stdout,
    level="INFO",
    # level=args.log.upper(), # zadano jako parametr pri spusteni
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(funcName)s - %(message)s"
)

hraj()