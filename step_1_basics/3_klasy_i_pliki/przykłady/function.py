#############################
######
######   FUNCTION
######
#############################

# najprostsza funkcja nie robiąca nic
def a():
    pass


# wywołanie funkcji
a()


# Parametry funkcji służą do przekazywania do niej danych
def sayHello(imie):
    print(f"Hello my friend {imie}!")


sayHello(input("Name: "))


#############################
###### słowo klucz
######  |  nazwa funkcji
######  |     |  pierwszy argument
######  |     |     |    drugi argument z defaultowym argumentem 5
######  V     V     V   V
###### def some_fun(a, b=5):
######    ......     < --  mogą być inne operacje
######    return a * b
######      ^      ^
######      |    zwracana wartość
######   słowo kluczowe pozwalające coś zwrócić
#############################


# funkcja przyjmuje jeden parametr name który defaultową wartością jest Alan
def greet(name="Alan"):
    # wypisuje "Hello, <name>. Good morning!" na ekran
    print("Hello, " + name + ". Good morning!")
    # sprawdzenie czy name to Alan
    if name == "Alan":
        # jeśli tak to wypisz "Hej" na ekran
        print("Hej")
    else:
        # jeśli nie to wyjdź z funkcji, return nie musi mieć parametrów. Słowo return wychodzi z funkcji i zwraca
        # chodź tak naprawdę pusty return zwraca None ;)
        # czyli return ---> to to samo co ---> return None
        return
    # ta linijka wykona się tylko wtedy jak name=="Alan"
    print("Poza ifem")


greet("Alan")

# __doc__ odwołuje się do dokumentacji funkcji
# def f():
#   """Some fun docs"""
#    ....   -< jakies operacje
#
# f.__doc__  --> "Some fun docs"
print(greet.__doc__)

sum

###############
###############

def domyslne_wartosci(a="brak", b="brak"):
    print('a=' + a)
    print('b=' + b)


domyslne_wartosci("X", "Y")
domyslne_wartosci()
domyslne_wartosci("coś")
domyslne_wartosci(b="coś innego")
domyslne_wartosci(b="coś innego", a="hmmm")


###############
###############

# przykład funkcji z jednym parametrem zwracający wartość absolutną podanej liczby

def absolute_value(num):
    """
    This function returns the absolute
    value of the entered number

    Args:
        num:

    Returns:

    """

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))


###############
###############

# przykład funkcji która przyjmuję nieskończoną liczbę argumentów nienazwanych
# w funkcji posiadamy
#       - argumenty nienazwane czyli np. f(1,2,3,4,5)
#       - argumenty nazwane czyli np.  f(name='Alan')
#   oczywiście możemy to mieszać
#   def f(a,b,c,d,e):
#       ....
#
#   f(1,2,3, e=1,d=3) <--- argumenty nie nazwane podajemy w kolejności natomiast jeśli podamy parametr nazwany to możemy podać je nie w kolejności
# przy założeniu, że jeśli nie mamy zadnej defaultowej wartości to musimy podać wszystkie argumenty
# ponieważ w definicji funkcji zawsze daultowe wartości muszą być na koncu np

#     def f(a,b,c,d,e=1)
#         ...
#
#     więc możemy f wywołać i każde jest poprawne
#     f(1,2,3,4,5)
#     f(1,2, c=1, d=2)
#     f(1,2, e=3, c=1, d=2)
#     f(b=1,a=2, e=3, c=1, d=2)
#     f(a=1,b=2, c=3, d=1, e=2)


# jeśli wywołamy funkcje def greet(*names) np greet("Monica", "Luke", "Steve", "John")
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # to names będzie listą tych argumentów czyli ["Monica", "Luke", "Steve", "John"]
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")


###############
###############


# def a(*args, **kwargs):
#     .....

# to jeśli `a` wywołamy w taki sposób a(1,2,3, c=2, d='test')
# to
#     - args <--- [1,2,3]
#     - kwargs <--- {'c': 2, 'd': 'test'}

def greet(a, b, *args, c="test", **kwargs):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    print(f"args={args}")
    print(f"kwargs{kwargs}")


greet(1, 2, 3, 4, 5, c=3, d=1, test=1)


###############
###############

# rekurencja jest to wywoływanie funkcji w funkcji do spełnienia warunku


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 3
print("The factorial of", num, "is", factorial(num))


# wywoływania rekurencyjnej funkcji
# factorial(5)
#   ┌factorial(5)
#   │  ┌factorial(4)
#   │  │  ┌factorial(3)
#   │  │  │  ┌factorial(2)
#   │  │  │  │  ┌factorial(1)
#   │  │  │  │  └1
#   │  │  │  └2
#   │  │  └6
#   │  └24
#   └120
# 120

#############################
######
######   lambda
######
#############################

# lambda jest to anonimowa funkcja
# słowo kluczowe
#  |   dwa argumenty funkcji
#  |       |    operacja której wynik zostanie zwrócony
#  V       V      V
#  lambda x, y: x * y

# funkcja o nazwie multi
def multi(x, y):
    return x * y


# odpowiednik funkcji multi jako funkcja anonimowa(lambda)
multi_f = lambda x, y: x * y

print(multi_f(5, 5))


# Możemy przekazywać dosłownie wszystko jako parametr więc możemy np. przekazać referencje do funkcji
def do_something(a, b, cal):
    return cal(a, b)


# jeśli wywołamy powyższą funkcje np
# do_something(1, 2, multi_f)
# to tak jak byśmy uruchomili poniższą funkcje
#
# def do_something(a, b, multi_f=lambda x, y: x * y):
#     return multi_f(a, b)

print(f"{do_something(1, 2, multi_f)}")
print(f"{do_something([1, 2, 3, 4], 2, multi_f)}")
print(f"{dict(do_something([1, 2, 3, 4], [4, 3, 2, 1], zip))}")


###############
###############

def powieksz(x):
    return x.upper()


def zastosuj_dla_wszystkich(fun, *args):
    for a in args:
        print(fun(a))


zastosuj_dla_wszystkich(powieksz, 'siała', 'baba', 'mak')

zastosuj_dla_wszystkich(lambda x: x.upper(), 'siała', 'baba', 'mak')

###############
###############

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)


# Możliwa jest deklaracja funkcji we wnętrzu innej funkcji. Taka funkcja wewnątrz innej funkcji
# będzie widziana tylko w niej:

def zewnetrzna(x):
    def wewnetrzna(x):
        return x * 2

    print(wewnetrzna(x))


zewnetrzna(50)


def wybierz(tryb):
    def powieksz(x):
        return x.upper()

    def pomniejsz(x):
        return x.lower()

    if tryb == 1:
        return powieksz
    elif tryb == 2:
        return pomniejsz


funkcja = wybierz(1)
print(funkcja('Witaj Świecie!'))
funkcja = wybierz(2)
print(funkcja('Witaj Świecie!'))
