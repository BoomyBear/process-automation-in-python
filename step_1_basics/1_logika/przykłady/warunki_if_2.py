name = input("Podaj Imie: ")

# jesli ostatnia litera jest 'a' to najprawdopodobniej kobieta
if name.endswith("a") and not name == "Jan Maria":
    print(f"Hej {name}, jesteś najpewniej kobietą")

# jezeli napisze Jan Maria to witamy Pana Rokite
if name == "Jan Maria":
    print("Witaj, Panie Rokita.")

else:
    print(f"Hej {name}, jesteś chyba mężczyzną")


