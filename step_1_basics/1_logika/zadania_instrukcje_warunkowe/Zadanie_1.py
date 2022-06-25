"""
Wymagania:
Sprawdź czy podana przez użytkownika liczba
jest podzielna przez 3, 5, 7

Wypisz wyniki na ekran.

Pamiętaj o komentarzach.

Rezultat wypisz na ekran.

Podpowiedź:
Odpowiednio formatuj stringi
"""

x = int(input("Podaj liczbe: "))

x_mod_three_boolean = x % 3 == 0
x_mod_five_boolean = x % 5 == 0
x_mod_seven_boolean = x % 7 == 0


if x_mod_three_boolean or x_mod_five_boolean or x_mod_seven_boolean:
    print('Liczba jest podzielna przez: ', end=(''))
    if x_mod_three_boolean:
        print('3', end=', ')
    if x_mod_five_boolean:
        print('5', end=', ')
    if x_mod_seven_boolean:
        print('7')
else:
    print(f'Liczba nie jest podzielna przez: 3, 5, 7')
