"""
Używając aplikacji Fundamentals i sekcji "Cookies"
napisz odpowiednie requesty i sprawdź responsy przy użyciu python requests
tak aby uzyskać dostęp do zasobu for_logged_users_only. Wspomóż sięswaggerem w razie potrzeby
"""

import requests as r
from faker import Faker

from requests.auth import HTTPBasicAuth

url = "http://localhost:8080"

fake = Faker()

user = {
    "username": fake.name(),
    "password": "string"
}
response = r.post(f"{url}/register", json=user)

assert response.status_code == 201
print(response.status_code)
print(response.json())

registration_key = response.json()['key']
print(registration_key)

response = r.get(f"{url}/for_logged_in_users_only")
assert response.status_code == 401
assert response.json()['message'] == "I find your lack of cookie disturbing..."

response = r.post(f"{url}/login", json=user)
assert response.status_code == 202
print(response.json())
print(response.cookies)

for cookie in response.cookies:
    print(cookie)

response = r.get(f"{url}/for_logged_in_users_only", cookies=response.cookies)
print(response.status_code)
print(response.json())
print(response.cookies)
