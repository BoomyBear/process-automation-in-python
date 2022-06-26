"""
Używając aplikacji Fundamentals i sekcji "Successful requests responses"
zmodyfikuj listę ludzi używając poszczególnych endpointów.
Za każdym razem sprawdź poprawność modyfikacji.
"""
from pprint import pprint

import requests as r

def checkHumanInfo(humanId, url):
    response = r.get(f"{url}/human/{human_id}", )
    pprint(response.json())

url = "http://localhost:8080"
#response = r.get(f"{url}/get_all_people/")

#pprint(response.json())

human_id = 11

checkHumanInfo(10,url)

person_change = {"last_name" : "ghjkalskfl"}
response = r.patch(f"{url}/human/{human_id}",json=person_change)
pprint(response.json())
checkHumanInfo(human_id,url)

response = r.delete(f"{url}/human/{human_id}")
pprint(response.json())
checkHumanInfo(human_id,url)

person_change = {"first_name":"John","last_name" : "Tester"}
response = r.post(f"{url}/human/{human_id}")
pprint(response.json())
response = r.get(f"{url}/get_all_people/")
pprint(response.json())
