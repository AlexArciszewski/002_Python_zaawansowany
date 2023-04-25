"""
Dekoratory służą do rozszerzania funkcjonalności metod. Wszędzie tam, gdzie zauważysz zapis @keyword to właśnie
przykład dekoratora. Co więcej, warto również wiedzieć, że wykorzystanie dekoratorów zalicza się do technik
metaprogramowania.
W skrócie - metaprogramowanie polega na na modyfikowaniu działania programu już w trakcie jego kompilacji. Może
to służyć do przenoszenia obliczeń z czasu wykonywania na czas kompilacji, do generowania koduo się kodu.

"""

#@classmethod

""" 
gdy chcemy powiązać daną metodę z samą klasą, aniżeli z obiektem danej klasy.
Metody poprzedzone dekoratorem @classmethod nie potrzebują bowiem do wywołania żadnej instancji klasy. 
Jednak drugą stroną medalu jest, że przez to, iż nie odnoszą się do klasy - jako całościowego bytu - 
nie możemy się z ich poziomu odwoływać ani do pól, ani do innych metod składowych przy użyciu keyword self!

"""

""" 
Syntax:
@classmethod
def func(cls, args...)

cls - klasa (nie obiekt), na rzecz którego func została wywołana
args - dowolne argumenty metody

"""

""" 
Metoda opatrzona dekoratorem @classmethod służy przede wszystkim do tworzenia nowych obiektów 
(istnieje tutaj dość duża korelacja między, tzw. factory methods).

"""

#Przykład1

""" 
Prostym przykładem jej zastosowania może być klasa Worker, która będzie posiadała właśnie metodę z ustawionym 
dekoratorem @classmethod i służyć będzie do wytwarzania nowych obiektów o określonych cechach. 
Załóżmy, że tworzona klasa posiadać będzie takie pola jak: name oraz start_year (rok rozpoczęcia pracy).
Co do kluczowego zagadnienia – pod dekoratorem @classmethod, stworzymy metodę, która przyjmować będzie argument klasowy 
(cls), imię pracownika oraz lata, ile już pracuje na danej posadzie (args). 
Na podstawie tych informacji zadaniem metody będzie wytworzenie (fabrykowanie) i zwrócenie nowego pracownika.

"""

from datetime import date

class Worker:
    def __init__(self, name: str, start_year: int):
        self.name = name
        self.start_year = start_year

    @classmethod
    def fromSeniority(cls, name: str, years: int):
        return cls(name, date.today().year - years)

    def display(self):
        print(f"Worker's name:{self.name}\nWorker's start_year:{self.start_year}\n")

w1 = Worker("John", 2000)
w2 = Worker.fromSeniority("Elizabeth", 5)

w1.display()
w2.display()

#staticmethod nie przyjmuje cls jako pierwszego argumentu). więc tu się nie przyda
""" 
@classmethod uzywamy chcemy tworzyć "statyczne metody" (czyli choćby metody fabrykujące) w danej klasie.

Okazuje się, że mając stworzoną metodę fabrykującą w klasie rodzicielskiej z dekoratorem @staticmethod, niemożliwe staje
się wytwarzanie klas po niej dziedziczących. Czyli rodzic nie może prawidłowo fabrykować swoich dzieci. Konieczne jest 
bowiem przesyłanie argumentu cls (którego de facto w @staticmethod nie ma) – czyli klasy będącej potomkiem, a jedyną 
taką funkcjonalność zapewnia Nam @classmethod. 

"""
#Funkcja może także zwracać referencję do dowolnej funkcji

def outer_func():
    print("Outer!")

    def inner_func():
        print("Inner!")

    return inner_func

var = outer_func()       #Outer
var() #inner


def mui_I(first):
    def mui_II(second):
        return first * second

    return mui_II
mui_I_3 = mui_I(3)
print(mui_I_3(5))
print(mui_I_3(10))


print("Przykład 3")

def make_decorated(func):
    def inner():
        print("Got decorated")
        func()

    return inner
@make_decorated
def ordinary():
    print("I am ordinary")



ordinary()  #got decorated
            #I am ordinary


print("Mój przykład")


def doing_cowboy_stuff(func):
    def inner():
        print("I am drinking cowboy")
        func()

    return inner


@doing_cowboy_stuff
def cowboy():
    print("i lost my boots while drinking whiskey")


cowboy()
"""
1.zrobiłem @dekorator 7
2.zrobiłem funkcję z printem 8-9
3. wróciłem do góry i zrobiłem funkcję o nazwie dekroatora(func)
4.zrobiłem funkcję(inner) w funkcji o nazwie dekratora z argumentem func dającą printa I am drinking cowboy wywołałem funckję func 
5. funkcja o nazwie dekoratora zwraca inner
6.wywołuję funkcje pod dekorato.remove()
"""

def make_universal(func):
    def inner(*args, **kwargs):
        print("Got decorated")
        return func(*args, **kwargs)

    return inner

@make_universal
def ordinary_no_params():
    print("No params")


@make_universal
def ordinary_two_params(param1, param2):
    print(f"Two params: {param1}, {param2}")

ordinary_no_params()
ordinary_two_params("One", "Two")


#Przykład MENU z ramką z gwiazdek

def add_stars(func):
    def inner(*args, **kwargs):
        print(kwargs['amount'] * '*')
        func(*args, **kwargs)
        print(kwargs['amount'] * '*')

    return inner

@add_stars
def print_menu(*args, **kwargs):
    print(args[0])

print_menu("1. Start\n2. Exit", amount = 17)

#mankament związany z przesłanianiem nazwy udekorowanej funkcji przez funkcję wewnętrzną w obrębie dekoratora
#rozwiązanie to @wraps

#Przykład MENU z ramką z gwiazdek


def add_stars(func):
    def inner(*args, **kwargs):
        print(kwargs['amount'] * '*')
        func(*args, **kwargs)
        print(kwargs['amount'] * '*')

    return inner


@add_stars
def print_menu(*args, **kwargs):
    print(args[0])


#print_menu("1. Start\n2. Exit", amount=17)

print(f"Function name:{print_menu.__name__}")
#dostajemy w terminalu: Function name:inner
#funkcja jest udekorowana przez dekorator, w którym znajduje się właśnie inner i to on jest wstawiany jako reprezentacja
#funkcji, do której się odnosimy. Możemy zatem powiedzieć, że w naszym kodzie funkcja oryginalna traci niektóre ze swoich właściwości.


""" 
Pytanie, jakie sobie powinniśmy zadać to: “Jak pisać dekoratory, aby nie powodowały one nadpisania właściwej nazwy 
ozdobionej nimi funkcji?”. Odpowiedź jest prosta - użyć dekorator @wraps i umieścić go nad wewnętrzną funkcją inner!


"""
#Przykład z gwiazdką poprawa aby nei było inner wraps sięs tosuje

from functools import wraps

def add_stars(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(kwargs['amount'] * '*')
        func(*args, **kwargs)
        print(kwargs['amount'] * '*')

    return inner


@add_stars
def print_menu(*args, **kwargs):
    print(args[0])


#print_menu("1. Start\n2. Exit", amount=17)

print(f"Function name:{print_menu.__name__}")

""" 
1)	Aby użyć dekorator wraps - musimy zaimportować go z biblioteki functools
2)	Nad funkcją inner umieściliśmy zaimportowany dekorator i przekazaliśmy do niego referencję do funkcji func.

"""

""" 
Zad. 1
Napisz dekorator, który służyć będzie do logowania, z jakimi argumentami dana funkcja została wywołana. 
Skorzystaj z **kwargs, *args oraz zmiennej specjalnej __name__, aby logować również nazwę funkcji, którą wywołujemy.

Kod:
@logged 
def func(*args): 
   return 3 + len(args) 

func(4, 4, 4) 

Output:
you called func(4, 4, 4) it returned 6


"""


def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"you called {func.__name__}({args}) it returned {result}")
        return result
    return wrapper

@logged
def func(*args):
   return 3 + len(args)

func(4, 4, 4)

""" 
Zad. 2
Stwórz dekorator, który będzie służył do przyozdabiania wyświetlanego tekstu gwiazdkami. 
Dowolny tekst ten ma być wyświetlany z poziomu dekorowanej funkcji.

Efekt:
************
Hello World!
************

"""


from functools import wraps

def add_some_stars(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(kwargs['amount'] * '*')
        func(*args, **kwargs)
        print(kwargs['amount'] * '*')

    return inner


@add_some_stars
def printer(*args, **kwargs):
    print(args[0])

printer("KILL BILL", amount = 30)



""" 
Zad. 3
Napisz dekorator @count, który wyświetlał będzie tworzył słownik, w którym będziemy przechowywali informację, 
ile razy zostały wywołane poszczególne funkcje udekorowane właśnie tym dekoratorem. 
"""
###################################################
print("Zad 3")
from collections import Counter

class CountingProxy():
    def __init__(self, instance):
        self._instance = instance
        self.count = Counter()

    def __getattr__(self, key):
        if hasattr(self._instance, key):
            self.count[key] += 1
        return getattr(self._instance, key)
################################################
def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

class MyList(list):
    @counted
    def pop(self, *args, **kwargs):
        return list.pop(self, *args, **kwargs)

x = MyList([1, 2, 3, 4, 5])
for i in range(3):
    x.pop()

print(x.pop.calls) # prints 3
#####################################################


"""
Zad. 4
W szkoleniu nie zostało o tym wspomniane, ale możemy również określać przesyłane argumenty dekoratorów! Jedyna
 konieczność jaka będzie do zrealizowania, to dodanie kolejnej funkcji wrappującej, czyli np:

def arg_check(arg):
    def check(old_func):
        def new_func():
            # do sth with arg and call old_func as examp
            
        return new_func
    return check
    
@arg_check(arg)
def examp(num):
    # do sth

Twoje zadanie to stworzyć dekorator, który sprawdzać będzie, czy określony w dekoratorze typ jest zgodny z typem 
zmiennej przesłanej do funkcji.

Podpowiedź:
-	Przesyłaj jako argument do dekoratora obiekt typu: int, float itd
-	Sprawdzaj, czy typy są zgodne przy użyciu isinstance(zmienna, typ_oczekiwany)
-	Jeżeli typ będzie niezgodny, rzucaj wyjątkiem

Zad. 5
Utwórz dekorator @timethis mierzący czas wykonania dekorowanej funkcji. Wykorzystaj moduł time i metodę time.time().

"""
print("Zad 5")


def check_type(excepted_type):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, excepted_type):
                raise TypeError(f"Excepted type {excepted_type}, but got {type(arg)}")
            result = func(arg)
            return result
        return wrapper
    return decorator


@check_type(int)
def my_function(x):
    return x * 2

from time import time

def timer_func(func):
    #czas egzekucji obiektu
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function{func.__name__!r} executed in {(t2 - t1): 4f} s")
        return result
    return wrap_func

@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j
long_time(23)




"""
Zad. 6
Zapoznaj się, do czego służą wbudowane w standard Pythona poniższe dekoratory: @property, @dataclass, @classmethod i 
@staticmethod.
Zbuduj proste programy przedstawiające realizację tych dekoratorów i różnice między nimi.

"""
print("Zadanie 6.a classmethod")
from datetime import date


class Worker:

    def __init__(self, name: str, start_year: int) -> None:
        self.name = name
        self.start_year = start_year

    @classmethod  # zamiast staticmethod bo staticmethod nie przyjmuje cls jako pierwszego argumentu
    def fromSeniority(cls, name: str, years: int):
        return cls(name, date.today().year - years)

    def display(self):
        print(f"Worker's name:{self.name} \n Worker's start_year:{self.start_year}\n")


w1 = Worker("John", 2000)
w2 = Worker.fromSeniority("Elizabeth", 5)

w1.display()
w2.display()

print("Zadanie 6.b getter setter deleter")

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - wyciaga wartosc pola
    def age(self):
        return self.__age

    @age.setter  # setter - ustawia nowa wartosc pola
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")
    @age.deleter  # deleter - usuwa pole
    def age(self):
       del self.__age

my_dog = Animal("reksio", 5)
my_dog.age = 3  # Ustawia wiek - korzysta z settera
print(my_dog.age)  # Odczytuje wiek - korzysta z gettera
del my_dog.age  # Usuwa pole - korzysta z deletera


print("Zadanie dodatkowe prosty wrapper")
def my_decorator(func):
    def wrapper_function(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 10)
    return wrapper_function


def say_hello():
    print("Dzien dobry")

@my_decorator
def say_goodbye():
    print(" Do widzenia")

say_hello =my_decorator(say_hello)
say_hello()
say_goodbye()

print("Zad 5")
from time import time

def timer_func(func):
    #czas egzekucji obiektu
    def wrap_func(*args,**kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function{func.__name__!r} executed in {(t2 - t1): 4f} s")
        return result
    return wrap_func

@timer_func
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i*j
long_time(23)


# #### STATIC METHOD ####
# class Math:
#     no_of_calc = 0 # ATRYBUT KLASY
#     def __init__(self, calc_name):
#         self.calc_name = calc_name # ATRYBUT OBIEKTU
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#     @staticmethod
#     def multiply(x, y):
#         return x * y
#
#     def __str__(self):
#         return f"Klasa kalulatora xyz"
#
#     def __repr__(self):
#         return f"Math({self.calc_name})"
#
# print(Math.add(5, 3))
#
# x = Math(5)
#
# print(x)
#
# #### CLASS METHOD ####
# class Person:
#     all_people = []
#     def __init__(self, name, born_year):
#         self.name = name
#         self.born_year = born_year
#         Person.all_people.append(self)
#
#     @classmethod
#     def number_of_people(cls):
#         return len(cls.all_people)
#
#     @classmethod
#     def create_person_from_age(cls, name, age):
#         today_year = 2023
#         return cls(name, today_year - age)
#
#     def __str__(self):
#         return f"{self.name}, {self.born_year}"
#
#
# person1 = Person("Alice", 1998)
# person2 = Person("Bob", 1993)
# print(Person.number_of_people())
# person3 = Person.create_person_from_age('Alice', 19)
#
# print(person1)
# print(person3)
#
# #### PROPERTY METHOD ####
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     def get_radius(self):
#         pass
#
#     def set_radius(self):
#         pass
#
#     @property
#     def radius(self):
#         print("pobieram zmienną:)")
#         return self._radius
#
#
#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError('radius nie moze byc ujemny')
#         self._radius = value
#
#     @radius.deleter
#     def radius(self):
#         del self._radius
#
# circle = Circle(5)
# # circle.get_radius()
# print(circle.radius)
# # circle.radius = -5
# del circle.radius
# print(circle.radius)


#### DATACLASS ####

from dataclasses import dataclass

@dataclass
class Person:           #repr zaciągnięty
    name: str = 'Unknown'
    age: int | str = 'Unknown'

person = Person("Alice", 30)
print(person)


# def make_universal(func):
#     def inner(*args, **kwargs):
#         print("GOt decorated")
#         return func(*args, **kwargs)
#     return inner

def make_universal(xyz):
    def inner(x, y):
        print("GOt decorated")
        return xyz(x, y)
    return inner


@make_universal
def xyz(x, y):
    print("No params")


make_universal(xyz)



def add_some_stars(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(kwargs['amount'] * '*')
        func(*args, **kwargs)
        print(kwargs['amount'] * '*')

    return inner


def add_some_stars(func):
    print("*****")
    result = func()
    print("*****")
    return result


def func():
    pass

result = add_some_stars(func)

"""
Zadanie 1:

Stwórz klasę Pracownik zawierającą następujące atrybuty:

imie (str) - imię pracownika
nazwisko (str) - nazwisko pracownika
stawka (float) - stawka godzinowa pracownika
Klasa powinna mieć również następujące metody:

pracuj() - wyświetl komunikat "Pracuję"
oblicz_wynagrodzenie(godziny: int) -> float - oblicz wynagrodzenie pracownika na podstawie podanych godzin i stawki godzinowej
Następnie stwórz klasę Programista dziedziczącą po klasie Pracownik. Klasa Programista powinna zawierać dodatkowy atrybut jezyki (list of str) - lista znanych przez programistę języków programowania.

Klasa Programista powinna również mieć następujące metody:

napisz_kod() - wyświetl komunikat "Piszę kod"
zwieksz_stawke(procent: float) - zwiększ stawkę godzinową programisty o podany procent
"""

class Pracownik:
    def __init__(self, imie: str, nazwisko: str, stawka: float) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka

    def __repr__(self) -> str:
        return f"Pracownik(imie={self.imie}, nazwisko={self.nazwisko}, stawka={self.stawka})"

    def __str__(self) -> str:
        return f"This is my job. I am {self.imie} {self.nazwisko}"

    @staticmethod
    def pracuj():
        print("pracuje")

    def oblicz_wynagrodzenie(self, godziny: int) -> float:
        return self.stawka * godziny

    @classmethod
    def create_employee(cls, name: str, surname: str, salary_per_month: float):
        return cls(imie=name, nazwisko=surname, stawka=salary_per_month / 168) # cls -> class -> Pracownik(name, surname, salary_per_month / 168)

    @classmethod
    def create_employee_from_yearly(cls, name: str, surname: str, salary_per_year: float):
        return cls(name, surname, salary_per_year / 2080)


class Programista(Pracownik):
    def __init__(self, imie: str, nazwisko: str, stawka: float, jezyki: list[str]) -> None:
        super().__init__(imie, nazwisko, stawka)
        self.jezyki = jezyki

    def napisz_kod(self):
        print("piszę kod")

    def zwieksz_stawke(self, procent: float):
        self.stawka = self.stawka + self.stawka * (procent / 100)
        self.stawka += self.stawka * (procent / 100)


def main():
    player_001 = Pracownik(imie="Jan", nazwisko="Nowak", stawka=50)
    print("TEST CASES")
    print(player_001.imie)
    print("=" * 79) #to daje ramkę
    assert player_001.imie == 'Jan'
    assert player_001.nazwisko == 'Nowak'
    assert player_001.stawka == 50
    assert player_001.oblicz_wynagrodzenie(10) == 500
    player_001.stawka = 60
    assert player_001.oblicz_wynagrodzenie(10) == 600

    # option = 'monthly'
    # if option == 'monthly':
    #     player_001 = Pracownik.create_employee('Jan', 'Nowak', 10_000)
    # elif option == 'hourly':
    #     player_001 = Pracownik('Jan', 'Nowak', 55)
    # elif option == 'yearly':
    #     player_001 = Pracownik.create_employee_from_yearly('Jan', 'Nowka', 120_000)
    #

if __name__ == "__main__":
    main()



