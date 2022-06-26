"""
Używając aplikacji Reactor Challenge i wiedzy z zadania 3 i 4
zautomatyzuj proces zdobywania flag.
Wszystkie flagi zapisz do pliku flags_reactor.txt
"""
from pprint import pprint

import requests as r
from faker import Faker

url = 'http://localhost:8080/challenge/reactor'
list_of_flags = []
faker = Faker()
key_obtained_at_desk = None

response = r.get(f'{url}/information')
pprint(response.json())

name_to_desk = {
    "name": faker.name()
}

def getKeyFromDesk(user,printSteps):
    if printSteps:
        print('Attempt to check in at the desk')
    response = r.post(f'{url}/desk', json=name_to_desk)
    if printSteps:
        pprint(response.json())
    return response.json()['key']

def getReactorPowerAndStatus(key,printSteps):
    if printSteps:
        print('Analysis information from Control Room')
    response = r.get(f'{url}/{key}/control_room/analysis')
    if printSteps:
        pprint(response.json())
    return response.json()['_ReactorCore__power'],response.json()['_ReactorCore__state']

# print('Reset progress without key.')
# response = r.get(f'{url}/{key_obtained_at_desk}/reset_progress',json=name_to_desk)
# pprint(response.json())
# list_of_flags.append(response.json()['flag'])
#
# print('Control room without key.')
# response = r.get(f'{url}/{key_obtained_at_desk}/control_room',json=name_to_desk)
# pprint(response.json())
# list_of_flags.append(response.json()['message'][-18:])
#
# az_5_override = {
#   "pressed": True
# }
#
# print('Control room using AZ-5 without key.')
# response = r.put(f'{url}/{key_obtained_at_desk}/control_room/az_5',json=az_5_override)
# pprint(response.json())
#
#
# print('1-st attempt to check in at the desk')
# response = r.post(f'{url}/desk', json=name_to_desk)
# pprint(response.json())
# key_obtained_at_desk = response.json()['key']
#
# print('2-nd attempt to check in at the desk')
# response = r.post(f'{url}/desk',json=name_to_desk)
# pprint(response.json())
#
# print('Checking reactor core')
# response = r.get(f'{url}/{key_obtained_at_desk}/reactor_core',json=name_to_desk)
# pprint(response.json())
# list_of_flags.append(response.json()['flag'])
#
# # print('Control room with key.')
# # response = r.get(f'{url}/{key_obtained_at_desk}/control_room',json=name_to_desk)
# # pprint(response.json())
#
#
# print('Control room using AZ-5 without key.')
# response = r.put(f'{url}/{key_obtained_at_desk}/control_room/az_5',json=az_5_override)
# pprint(response.json())
# list_of_flags.append(response.json()['flag'])
#
#
#
# print('Reset progress with key')
# response = r.get(f'{url}/{key_obtained_at_desk}/reset_progress',json=name_to_desk)
# pprint(response.json())
# list_of_flags.append(response.json()['flag'])

key_obtained_at_desk = getKeyFromDesk(name_to_desk,False)

reactor_power,reactor_status = getReactorPowerAndStatus(key_obtained_at_desk,False)

print('Control room analysis')
response = r.get(f'{url}/{key_obtained_at_desk}/control_room/analysis')
pprint(response.json())

print('Control room with key.')
response = r.get(f'{url}/{key_obtained_at_desk}/control_room')
pprint(response.json())

print('Playing with control rods')
for contronRodId, controlRod in enumerate(response.json()['reactor data']['_ReactorCore__control_rods']):
    print(controlRod)
    if controlRod != None:
        response_ = r.rem()

print('Control room analysis')
response = r.get(f'{url}/{key_obtained_at_desk}/control_room/analysis')
pprint(response.json())

print('Control room with key.')
response = r.get(f'{url}/{key_obtained_at_desk}/control_room')
pprint(response.json())

# print("List of found flags:")
# pprint(list_of_flags)
