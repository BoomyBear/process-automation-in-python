"""
Wymagania:
Napisz program, który wczytuje od użytkownika wartości
i dodaje je do listy dopóki użytkownik nie poda wartości 'nie'

Wypisz listę na ekran.
"""

listOfValuesEnteredByUser = []

while True:

    userEnteredValue = input('Enter value. Enter "nie" to stop the program: ')

    if userEnteredValue == 'nie':
        break

    listOfValuesEnteredByUser.append(userEnteredValue)

if len(listOfValuesEnteredByUser) != 0:
    print(f'List of values entered by user:\n {listOfValuesEnteredByUser}')
else:
    print('There were no values entered by the user')