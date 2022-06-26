"""
Używając aplikacji Fundamentals i sekcji "Client error requests responses"
napisz odpowiednie requesty i sprawdź responsy przy użyciu python requests
"""

import requests as r
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080"

response = r.get(f"{url}/limited", auth=HTTPBasicAuth("",""))


print(response.json())
print(response.status_code)

response = r.get(f"{url}/limited", auth=HTTPBasicAuth("Captain_snack","LateNightSausage"))

print(response.json())
print(response.status_code)