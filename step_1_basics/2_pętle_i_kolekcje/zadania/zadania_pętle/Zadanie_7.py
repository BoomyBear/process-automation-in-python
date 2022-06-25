"""
Wymagania:
Napisz program
pytajacy uzytkownika o litere a nastepnie
wypisujacy litery (z zakresu od a do z)
zaczynajac od a a konczac na n-tej literze przez uzytkownika
zakoncz program jesli uzytkownik wpisze slowo "exit" lub "quit"
"""
from string import ascii_lowercase

while True:
    letterProvidedByUser = input('Enter a letter: ').lower()
    if letterProvidedByUser == 'exit' or letterProvidedByUser == 'quit':
        break

    for literaZAscii in ascii_lowercase:
        print(f'{literaZAscii}')
        if literaZAscii == letterProvidedByUser:
            break
