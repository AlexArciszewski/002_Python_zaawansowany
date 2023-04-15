"""
Zad 1
Napisz funkcję generatora, która generować będzie kilka dowolnych wartości. Pobierz te wartości przy użyciu globalnej metody next() oraz metody generatora __next__().
Rzuć wyjątkiem wewnątrz generatora (po jego kilkukrotnym wywołaniu) i zbadaj stack trace.

"""
# seed the pseudorandom generator
# źródło: https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
from random import seed
from random import random

# losowo małe cyfry
seed(1)
print(random(), random(), random(), random(), random())

# losowo liczby

from random import seed
from random import randint

for _ in range(10):  # ile liczb
    value = randint(0, 100)  # zakres
    print(value)

# ciąg dalszy z__next__ pod linkiem stacka: https://stackoverflow.com/questions/40255096/next-in-generators-and-iterators-and-what-is-a-method-wrapper
print("Zad 1")

from random import randint


def first_task_generator():
    num = 0
    while True:
        for _ in range(10):
            value = randint(0, 100)
        yield value


generator = first_task_generator()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# odhashować aby ukończyć zad 1
# for number in generator:
#    if number == 51:
#        generator.throw(ValueError("The f *** aliens"))
#    else:
#        print(number)


""" 
Zad 2.
Stwórz generator, który generował będzie kolejne liczby pierwsze. 

"""
# czemu listing ze zszywki 11 działa a tu nie....czemu tam x nie jest problermem
# prime_numbers_gen = (numberx for i in range(2, number +1) if number % i != 0 )
# print(next(prime_numbers_gen))
"""
def second_task_generator():
    flag = 0
    number = 0
    if number == 0 or number == 1:
        flag = 0
    for i in range(2, number + 1):
        if number % i == 0:
            flag =0
        else:
            flag = 1
    if flag == 1:
        print(f"Prime")
        yield flag
    else:
        print("not a Prime")
generator = second_task_generator()
print(next(generator))
print(next(generator))   
"""
print("Zad2 sito Erastothenes")


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


generator = gen_primes()
print(next(generator))
print(next(generator))
print(next(generator))

print("zadanie 2 kolejne podejscie")
from math import sqrt

"""
i = 2
while True:
    for x in range(2, int(sqrt(i) + 1)):
        if i%x==0:
            break
    else:
        print(i)
    i += 1
"""

"""

from math import sqrt

def gen_primes2():

    number = 2

    while True:
        for i in range(2, int(sqrt(number) +1)):
            if number % i ==0:
                break
            else:
                print(number)
            yield number    
            number += 1

generator = gen_primes2()
print(next(generator))

"""

print("zadanie nr 3")

""" 
examp = (i for i in range(10))
print(examp)

"""

examp = (i for i in range(10))
print(examp)
# Wyprintowalismy generator trzeba zrobić next'a <generator object <genexpr> at 0x000001A6ABC08040>

examp = (i for i in range(0, 10, 1))
# print(next(examp)) # i tak 9 razy
for _ in range(10):
    print(next(examp))

"""" 
Zad 3.
Stwórz generator zwracający kolejne wartości ciągu Fibonacciego. Do obliczania kolejnych wyrazów, 
wykorzystaj poniższy zapis:

a = 1
b = 2
a, b = b, a + b

"""
print("Zadanie nr 3")
def fibonacci_numbers(numbers):
    a,b = 1,2
    for _ in range(numbers):
        a, b = b, a + b
        yield b

gen = fibonacci_numbers(5)
print(next(gen))
print(next(gen))
print(next(gen))



"""
Zad 4.
Mając tak utworzoną listę liczb:
numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
Wykorzystując, list comprehension, utwórz nową o nazwie filtered_numbers, w której znajdą się tylko liczby niedodatnie z numbers
"""
print("Zad 4")
numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]
filtered_numbers = [number for number in numbers if number <= 0]
print(filtered_numbers)

""" 
Zad 5.
Bazując na następującym tekście: “The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the English alphabet”, 
wydziel go na listę przechowującą długości kolejnych wyrazów z pominięciem słowa “the”, np.

length_of_words = [5, 5, 3, 5, ...], co odpowiada kolejno długościom wyrazów: quick, brown, fox, jumps

"""
list_box = []
list_box_len = []
txt = "The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the English alphabet"
txt.split(" ")
for word in txt.split(" "):
    list_box.append(word)
print(list_box)
list_box.pop(0)
print(list_box)

for word in list_box:
    print(len(word))
    list_box_len.append(len(word))
print(list_box_len)
# [[5, 5, 3, 5, 4, 3, 4, 3, 2, 2, 16, 9, 8, 4, 8, 3, 2, 3, 7, 2, 3, 7, 8]]
length_of_words = [len(word) for word in list_box]
print(length_of_words)
# [5, 5, 3, 5, 4, 3, 4, 3, 2, 2, 16, 9, 8, 4, 8, 3, 2, 3, 7, 2, 3, 7, 8]

length_of_words = [len(txt[i]) for i in range(1, len(txt))]
print(length_of_words)

# długość słowa =  [długość słowa dla słow w stringu jeśli w stringu są słowa od 1 do ostatniego}
length_of_words = [len(txt[i]) for i in range(1, len(txt))]

length_of_words = [len(word) for word in txt.split() if word != "The"]
print(length_of_words)

"""
Zad. 6
Mając do dyspozycji poniższą listę trójwymiarową: 

three_d = [
[[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]], 
[[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
]

przefiltruj ją tak, by znalazły się tylko te najbardziej wewnętrzne listy, których ilość elementów przekracza 4.

Wynikiem powinna być lista:

[[0, -1, -2, -3, -4, -5, -6], [1, 10, 15, 1, 20, 20, 20], [-15, -13, 14, 20, -1]]
"""

print("Zad 6")

three_d = [
    [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]], [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]]
normal_list = []
for outer_lists in three_d:
    print(outer_lists)
    for inner_list in outer_lists:
        print(inner_list)
        normal_list.append(inner_list)
normal_list.pop(0)
print(normal_list)
