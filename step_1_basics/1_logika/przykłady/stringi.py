wiek = input("Podaj wiek: ")

# wszystko co uzytkownik poda jest stringiem, nawet liczby
print(type(wiek))

# musimy zamienic str na int aby moc wykonac arytmetyke
rok_urodzenia = 2022 - int(wiek)
print(type(rok_urodzenia))
a = 1
b = 2
print("Twoj rok urodzenia to {} {} {}".format(rok_urodzenia, a, b))
print(f"{b} Twoj {a} rok urodzenia to {rok_urodzenia}")

wzrost = input("podaj wzrost: ")

# formatowanie wartosci liczbowych
print("Twoj wzrost w centymetrach to {:.2f}".format(float(wzrost)))
print(f"Twoj wzrost w centymetrach to {float(wzrost):.2f}")

print(f"Jedna trzecia to {1 / 3}")
print(f"Jsdna trzecia to {1 / 3:.3f}")

print("Twoj wzrost w centymetrach to {wzrost}, a wiek w latach to {wiek}".format(wzrost=173, wiek=34))
print(f"Twoj wzrost w centymetrach to {wzrost}, a wiek w latach to {wiek}")
print(f"Twoj {wzrost=} cm, a {wiek=} lat")
# print(f"Mój wzrost={wzrost}")
