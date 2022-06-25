"""
Pobierz dane numeryczne od użytkownika i zapisz je do listy.
Użyj obsługi wyjątków by zwrócić użytkownikowi uwagę, gdy poda dane nienumeryczne.
Kontynuuj pytanie o dane dopóki użytkownik nie wpisze litery "N"
"""

numbers = []
while True:
    inputData = input('podaj liczbe (lub N by zakonczyc program): ')
    if inputData == 'N':
        print('Do zobaczenia.')
        break
    try:
        numbers.append(int(inputData))
    except ValueError:
        print('Prosze podac liczbe')


print(numbers)