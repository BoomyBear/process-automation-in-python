imie = input("Podaj imie: ")

# w pythonie 3.6 można tak jak ponizej, ale tylko w 3.6 i kolejnych wersjach
print(f"Witaj {imie}!")

# nazwisko powinno byc z duzej
imie = imie.capitalize()
print("Witaj {}".format(imie))

# szukamy pierwszego wystapienia znaku
x = imie.find("A")
print(x)

# ------------------------
imie2 = 'anna'

# wszystko wydrukuje sie tak samo
print(f"Hello {imie2}")
print("Hello {}".format(imie2))
print("Hello " + imie2)

# -------------------------

# Nowa forma wprowadzona w Python 3.6
name = 'Fred'
age = 42
string = f"He said his name is {name} and he is {age} years old."
print(string)

# Poprzednie formy
name = 'Alan'
age = 53
string = 'He said his name is {name} and he is {age} years old.'.format(name = name, age = age)
print(string)

name = 'Greg'
age = 17
string = 'He said his name is {0} and he is {1} years old.'.format(name, age)
print(string)

name = 'George'
age = 27
string = "He said his name's {} and he is {} years old.".format(name, age)
print(string)

# ukłon w stronę ECMAscript2016
name = 'Fred'
seven = 7
string = f"""He said his name is {name.upper()}
and he is {6 * seven} years old."""
print(string)
