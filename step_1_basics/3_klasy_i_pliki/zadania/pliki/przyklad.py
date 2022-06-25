from faker import Faker

fake = Faker()
with open("plik.txt", "w" ) as f:
    lines = '\n'.join([fake.text() for _ in range(100)])
    f.writelines(lines)