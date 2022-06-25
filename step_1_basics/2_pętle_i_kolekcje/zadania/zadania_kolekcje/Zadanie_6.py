"""
Stwórz listę trzech słowniki - Krystynę, Agnieszkę i Piotrka
Każdy kursant powinien mieć imię, informację o obecności i pracy domowej oraz punkty na egzaminie

Przejdź przez 6 dni kursu wypisując progres kursantów:
- Imię
- Obecność (ustaw losowo)
- Czy praca domowa jest odrobiona czy nie (ustaw losowo)
- Uzyskane punkty na egzaminie (ustaw losowo) (ustaw dopiero 6 dnia kursu)

Podpowiedź:
użyj random.choice do losowego ustawienia True i False
użyj random.randint do losowego ustawienia punktów (w zakresie 0 - 100)
"""
import copy
import random
from pprint import pprint

listOfAttendees = []
krystyna = {'imie': 'krystyna', 'obecnosc': None, 'praca_domowa': None}
agnieszka = {'imie': 'agnieszka', 'obecnosc': None, 'praca_domowa': None}
piotrek = {'imie': 'piotrek', 'obecnosc': None, 'praca_domowa': None}

for training_day in range(1, 7):
    for kursant in [krystyna, agnieszka, piotrek]:
        k = copy.deepcopy(kursant)
        k['obecnosc'] = random.choice([True, False])
        k['praca_domowa'] = random.choice([True, False])
        if training_day == 6:
            k['punkty'] = random.randint(1, 100)
        print(f'Information for day {training_day} \n {kursant}')
        listOfAttendees.append(k)


pprint(listOfAttendees)