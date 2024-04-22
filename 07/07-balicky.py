# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/balicky-z-internetu/lesson

# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
# rates = c.get_rates('CZK')
# currency_list = ["GBP", "EUR", "USD"]
# for key, value in rates.items():
#     if key in currency_list:
#         rate = 1 / value
#         print(f"1 {key} = {round(rate, 2)}")

# Faker
from faker import Faker
fake = Faker('cs_CZ')

for _ in range(3):
  print(fake.name_female())
  print(fake.address())
  print()


# from faker.providers import internet

# fake.add_provider(internet)
# print(fake.email())

# je treba doinstalovat balicek faker_music
# pip install faker_music

# from faker_music import MusicProvider

# fake.add_provider(MusicProvider)
# print(fake.music_genre())