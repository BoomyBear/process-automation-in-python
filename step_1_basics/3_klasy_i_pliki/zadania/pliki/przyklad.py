from faker import Faker

fake = Faker()
with open("plik.txt", "w" ) as f: # w - utworzy/wyczysci plik / zapisze dane
    lines = '\n'.join([fake.text() for _ in range(100)])
    f.writelines(lines)

#
# with open("plik.txt", "a" ) as f: # a - otworzy plik i doda na samym koncu
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)
#
#
# with open("plik.txt", "r" ) as f: # r - odczytuje plik
#     lines = '\n'.join([fake.text() for _ in range(100)])
#     f.writelines(lines)