# Wyjątki Exceptions handling
#dzielenie przez zero wyjątek zastępujacy blokade dzielenia:



a = int(input("Type first number: "))
b = int(input("Type second number: "))
#zamiast
#if not b:
#print("Can't divide by 0!")
#else:
 #result = a / b
 #print(f"The result is equal to: {result}")



try:
    result = a/b
    print(f" The result is: {result}")
except:
    print("Can't divide!")


#Dzielenie wartości liczbowej przez wszystkie elementy listy.

values =[ "a", 0, 2, 3.5]

for elem in values:
    try:
        print("The entry is", elem)
        r = 1/elem
        print(f"The result is:{r}")
    except:
        print("Can't divide!")

""" 
Przykład:

try:
 # zrób coś
except ValueError:
 # obsłuż wyjątek ValueError
 except TypeError, ZeroDivisionError:
 # obsłuż kilka wyjątków
 # TypeError i ZeroDivisionError
 ...
except:
 # obsłuż wszystkie pozostałe wyjątki
 …
 ...
"""

values =["a", 0, 2, 3.5]
for elem in values:
    try:
        print("The entry is", elem)
        r =1/elem
        print(f"The result is: {r}")
    except ZeroDivisionError:
        print("Can't divide by 0!")
    except TypeError:
        print("Can't divide by letter!")
#przykład
#Stwórz funkcję obliczającą iloczyn liczb dodatnich.
#Zabezpiecz się przed próbą wykonania operacji na liczbach niedodatnich.


def mul_positive_nums(*args):
    result =1
    for num in args:
        if num <= 0:
            print("Each number should be positive")
            return -1
        else:
            result *= num
    return result

print(mul_positive_nums(1,2,100,311))

#Inna opcja z obsługa błędu:


def mul_positive_nums(*args):
    result = 1
    for num in args:
        if num <= 0:
            raise ValueError("Only positive numbers")
        else:
            result *= num
    return result

try:
    print(mul_positive_nums(1,2,3,4,6,100,-1))
except ValueError as e:
    print(e)

# Try:
#Run this code
#except:
#  Execute this code when there is an exception
#else:
#No exceptions? Run this code
#Finally:
#always run This code


try:
    age = int(input("Enter your age: "))
except:
    print("You have entered an invalid value.")
else:
    if age <= 21:
        print("You are not allowed to enter, you are too young")
    else:
        print("Welcome, you are old enough")

#bardziej zawiły przykład tego kodu:

try:
    age = int(input('Enter your age: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
except:
    print ('You have entered an invalid value.')


#Finally
""" 
Blok finally, wykorzystywany jest najczęściej, gdy chcesz “posprzątać” po pewnych operacjach. 
Najlepszym przykładem będzie otwarcie pliku w bloku try, wykonanie pewnych operacji i jego 
automatyczne zamknięcie w finally.


"""
file = open("test.txt", "w")
try:
    file.write("Testing")
    print("Writing to file.")
except IOError:
    print("Could not write to a file.")
else:
    print("Write successful")
finally:
    file.close()
    print("File closed.") # tu kończymy działanie programu i zamykamy plik


# Własne Exceptions

""" 
W momencie, gdy chcesz spersonalizować rodzaj rzucanego wyjątku, możesz utworzyć własną klasę, 
której obiekty będą właśnie reprezentowały pojedyncze exceptiony. 
Jedyny warunek, który musi zostać spełniony przy tworzeniu własnych klas - wyjątków - muszą 
one dziedziczyć po rodzicu Exception. 

"""

#class CustomError(Exception):
#    pass


#raise CustomError
#Traceback(most recent call last):

#__main__.CustomError


""" 
Tworzenie własnych wyjątków ma prosty cel. Dostarczają one łatwiejsze nawigowanie po programie. 
"""
""" 
Ponadto tworzone przez Nas wyjątki, mogą być przez Nas ulepszane, dzięki możliwości dodania do nich 
niektórych metod specjalnych, np. __str__(). 
Przykład z wykorzystaniem tejże funkcjonalności poniżej.

Przykład: Sprawdzaj, czy liczba znajduje się w określonym przedziale. 


"""

class ValueTooSmallError(Exception):
 def __str__(self):
   return "Typed value is too small!"

class ValueTooBigError(Exception):
 def __str__(self):
   return "Typed value is too big!"

def get_num_in_range(start: int, end: int):
 num = int(input(f"Type a number in range from {start} to {end}: "))
 if num < start:
   raise ValueTooSmallError
 elif num > end:
   raise ValueTooBigError
 else:
   return num

try:
 print(get_num_in_range(1, 5))
except (ValueTooSmallError, ValueTooBigError) as e:
 print(e)

#Ulepszenie kodu powyżej...

class ValueTooSmallError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return f"Typed value - {self.value} - is too small!"

class ValueTooBigError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return f"Typed value - {self.value} - is too big!"

#praktyka - Zadania ze zszywki:
""" 
Zad. 1
Przygotuj klasę FileHandler, która symulować będzie funkcjonalność obsługiwania plików w Javie. 
Ma ona przechowywać pola takie jak: file_path, no_connectors, max_file_size. Będa one ustawiane 
z poziomu odpowiednich setterów jak i konstruktora. Klasa ta ma dodatkowo przechowywać takie 
metody jak read_content, save_to_file, w których umieścisz, tzw. dummy printy (będziesz drukował dowolny tekst).
Celem tego zadania nie jest stworzenie odpowiedniej logiki biznesowej dla klasy, tylko zaprojektowanie klasy, 
która będzie zwracała odpowiedni user-defined wyjątek w zależności od przekazania do obiektu klasy niewłaściwej 
danej, np. pustego stringa, który będzie miał być umieszczony pod polem file_path. 

Dodatkowe warunki:
Wartość noConnector nie może przekroczyć wartości 10 
maxFileSize musi być zawsze liczbą czterocyfrową


"""



"""
Zad. 2
Mając do dyspozycji poniższy kod: 
Przerób go tak, aby obsługiwać wszystkie możliwe do wystąpienia wyjątki. 
W razie konieczności zdefiniuj własne rodzaje exceptionów.
"""

def example1():
    for i in range(3):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', x / y)


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        sumOfPairs.append(L[i] + L[i + 1])

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example3([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


if __name__ == "__main__":
    main()

