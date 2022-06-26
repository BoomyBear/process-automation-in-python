"""
Używając aplikacji Challenge Primer i wiedzy z zadania 3
zautomatyzuj proces zdobywania flag.
Wszystkie flagi zapisz do pliku flags_primer.txt
"""
from pprint import pprint

import requests as r

url = 'http://localhost:8081/challenge/primer'
response = r.get(f"{url}/information")
pprint(response.json())

response = r.get(f"{url}/tryout")
pprint(response.json())

response = r.get(f"{url}/flag")
pprint(response.json())

found_flags = 0
checkNumber = 0
number_of_hidden_flags = 2

list_of_flags = []
while True:
    response = r.get(f"{url}/flag/{checkNumber}")
    if response.status_code == 200:
        print(f'Checked number: {checkNumber}')
        pprint(response.json())
        found_flags += 1
        list_of_flags.append(response.json()['flag'])
    if found_flags == number_of_hidden_flags:
        break
    checkNumber += 1

user = {
    "username": "test",
    "password": "user"
}

non_existing_user = {
    "username": "1231144fat",
    "password": "u1123afd"
}

response = r.post(f"{url}/register", json=user)
print(response.json())
response = r.post(f"{url}/register", json=user)
print(response.json())
list_of_flags.append(response.json()['flag'])

response = r.post(f"{url}/login", json=non_existing_user)
print(response.json())
list_of_flags.append(response.json()['flag'])

response = r.post(f"{url}/login", json=user)
print(response.json())
print(response.cookies['session'])
list_of_flags.append(response.cookies['session'])


print(list_of_flags)
with open("plik.txt", "w") as f:
    lines = '\n'.join(list_of_flags)
    f.writelines(lines)
