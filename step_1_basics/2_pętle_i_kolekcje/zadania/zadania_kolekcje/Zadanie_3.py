"""
Wymagania:
Napisz program, który wczytuje od użytkownika stringi w postaci klucz - wartość
Dodaj je do słownika.
Jeśli dany klucz istnieje w słowniku - nie rób nic.

Zapewnij możliwość podania kolejnych par klucz-wartość lub zaprzestawania ich podawania.

Wypisz elementy słownika na ekran w formie "klucz -> wartość"

Podpowiedź:
Użyj dwóch inputów do pobrania wartości
"""


def getUserInput(instructionsForUserInput):
    terminate_program = False
    value_entered_by_user = input(instructionsForUserInput)
    if value_entered_by_user == 'exit' or value_entered_by_user == 'quit':
        terminate_program = True
    return value_entered_by_user, terminate_program


dictionary = {}
endProcess = False
while not endProcess:

    enteredKeyName, endProcess = getUserInput('Provide Key Name (to end program type: exit) ')
    if endProcess:
        break
    enteredValue, endProcess = getUserInput('Provide Value Name (to end program type: exit): ')
    if endProcess:
        break

    if enteredKeyName in dictionary:
        print('Entered key does not exist in dictionary.')
        continue

    dictionary[enteredKeyName] = enteredValue

print(dictionary)