#Programowanie funkcyjne

"""
Lambdy:
Nazywane są one również funkcjami anonimowymi.
Od tradycyjnych funkcjiróżnią się również tym, że lambdy nie mają nazw oraz ich utworzenie zajmuje dużo mniej
linii kodu.

Kilka cech charakterystycznych:
Funkcje lambda mogą przyjmować dowolną ilość argumentów, ale wykonują tylko jedną konkretną operację.
Lambdy nie modyfikują nigdy przesłanych wartości, tylko zwracają ich zmodyfikowane kopie.
Zapisanie lambdy jest o wiele krótsze niż budowa jej odpowiednika w postaci funkcji

"""
#lambda 1 argument
print("lambda 1 argument")
caster = lambda x: x % 2    #x to agument a x % 2 to wyrażenie lambda nie potrzebuje return aby się odwołać do lambdy
                            #trzeba przypisać zmienną caster

print(caster(7))    # 7 % 2 = 1
print(caster(10))   #10 % 2 = 0

#lambda 2 argumenty
print("Lambda 2 argumenty")
caster = lambda x,y: x % y

print(caster(10,5))
print(caster(6,4))

print("funkcja tradycyjna z returnem dwa argumenty")
def caster(a, b):
    return a % b
print(caster(6,4))


""" 
Kiedy lambda?
Jeśli daną funkcję potrzebujemy tylko na krótki okres czasu, gdy chcemy łączyć ze sobą jakieś funkcjonalności
i dawać użytkownikowi możliwość łatwego sterowania programem np, gdy chcemy kontrolować przebieg funkcji 
higher order (funkcja higher order cechuje się tym, że zwraca lub przyjmuje jako argument inną funkcję lub lambdę).

"""

def calc_result(x, y, op):
    print("Hi")
    print("I am starting computation process")
    return op(x,y)

print(calc_result(1, 2, lambda x, y: x**y))

print(calc_result(1, 2, lambda x, y: x + y))

print(calc_result(1, 2, lambda x, y: x//y))
#czy op jest naszą funkcją lambda?

print("immediately invoked function execution IIFE")

print((lambda x:x +x)(2))

""" 
Filter()
Metoda ta służy do filtrowania elementów dowolnej struktury danych (lista, tuple zbiory etc.) 
według pewnego warunku (możliwego do zdefiniowania w lambdzie). 

Syntax:
filter(func, iterable)

Omawiana metoda przyjmuje 2 argumenty:
—	Funkcję filtrującą (którą będziemy wyrażali przez lambdę)
—	Dowolną sekwencję danych

"""

""" 
Flitrowanie zadanie
Przefiltruj listę w poszukiwaniu liczb większych lub równych 4.
"""

elements = [20, 23, 24, 1, 2, -5, 0, 2, 3, 4]
filtered_result = filter(lambda x: x>=4, elements)

print(list(filtered_result))  #sam print zwraca error <filter object at 0x000002CC1790BC10> musi być print list.

""" 
Metoda filter przyjmuje pierwszy argument w postaci wyrażenia lambda (nazywane też predykatywą, ponieważ służy do zwracania wartości True/False 
w zależności od warunku).Drugim argumentem jest utworzona lista, której wartości chcemy przefiltrować według przekazanej lambdy.
Filter wyciąga z listy elements tylko te liczby, dla których lambda x: x >= 4 zwróci True (wszystkie elementy większe lub równe 4). 
W tym przypadku parametr lambdy nazwaliśmy jako x, ale równie dobrze może ona przyjąć postać lambda val: val >= 4 etc.

"""

""" 
Wybierz z zbioru unikalne imiona kończące się na literę 'a'.

"""
names ={"Kacper" , "Jan", "Elżbieta", "Joanna", "Jakub"}

result = filter(lambda name:name[-1] == "a", names)
print(set(result))


"""
Palindromy
"""
dromes = ("demigod", "rewire", "madam", "freer", "kajak")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

""" 
Map(). 
Do kopiowania i modyfikowania elementów obiektów iterables(np. zmienianie wszystkich liter na wielkie)
Metoda, którą właśnie zaczynamy omawiać ma następujący syntax: map(func, *iterables)
Func to dowolny rodzaj funkcji (my użyjemy lambdy), która zostanie wykonana na rzecz obiektów (lub obiektu) przesłanych w postaci *args - *iterables. 
Tak jak w przypadku metody filter(), map() zwraca obiekt generatorowy, dlatego konieczne będzie jego rzutowanie na odpowiedni typ, 
np. list(map(func, *iterables)).


Metoda, którą właśnie zaczynamy omawiać ma następujący syntax:
map(func, *iterables)

"""

""" 
Zamiana wszystkich liter elementów z listy na wielkie. Standardowe podejście.
"""
my_names = ["Elizabeth", "Sabrina", "Marry"]
uppered_names =[]

for name in my_names:
    name =name.upper()
    uppered_names.append(name)

print(uppered_names)

my_names = ["Elizabeth", "Sabrina", "Marry"]
uppered_names = list(map(lambda x: x.upper(), my_names))
print(uppered_names)

""" 
Map kiedy?

Potencjał map() sprawdzić się może jednak najbardziej w momencie, gdy chcemy przeprowadzić pewne operacje dla kilku obiektów równocześnie.
Ponadto, niekoniecznie musimy definiować własną funkcję (lub lambdę), bo możemy podać referencje do metody wbudowanej, tzw. built-in.

"""

""" 
Mając listę wartości typu float, przeprowadź proces zaokrąglania wartości do jednego miejsca po przecinku dla 1. wartości z listy, 
dwóch miejsc po przecinku dla 2. wartości z listy, trzech miejsc po przecinku dla 3. elementu itd.

"""
#z automatu round zaokrągla do 3 miejsc
areas = [3.1276448, 1.1269897898, 9.747478, 100.98398498, 5.12747348038]       # nie przeiterował mi ...
rounded_areas = list(map(round, areas, range(1,8)))   #losowo do 8 miejsca

print("AREAS")
print(rounded_areas)
print("AREAS")

""" 
Map() w powyższym przykładzie otrzymało w sumie 3 argumenty. Pierwszy argument to referencja do wbudowanej metody round (która na dobrą sprawę 
mogłaby być dowolną inną funkcją 3-argumentową). 
Następne argumenty to *iterables, czyli lista areas oraz range(1, 8). I choć odbywa się to niejawnie, to ich elementy przekazywane są do pierwszego 
argumentu map, czyli metody round. 
Co więcej, iteracja po *iterables następuje automatycznie. Czyli do metody round przekazywany jest kolejno element pierwszy z areas, a wraz z nim 
wartość 1 z range(1, 8). 
Następuje zaokrąglanie, wartość jest zapamiętywana i map przechodzi do następnych elementów - wywołuje metodę round(areas[1], 2), potem round(areas[2],
3) itd.

Na pewno zastanawiasz się, a co w momencie, gdybyśmy przekazali do map obiekty o różnej ilości elementów? 
Jak mogliśmy zauważyć, przechodzenie po elementach odbywało się równolegle i pojawia się zagwostka, co się wydarzy, gdy prześlemy, 
np. niezmienioną listę areas, ale inny przedział, bo w postaci range(1, 3)?

"""

""" 
Map() służące do zaimplementowania własnej funkcji zipującej dwie dowolne listy.

list(zip([1, 2, 3], [‘a’, ‘b’, ‘c’])) == [(1, ‘a’), (2, ‘b’), (3, ‘c’)]
"""
list_a = [1, 2, 3, 4]
list_b =['a', 'b', 'c', 'd']
list(zip(list_a,list_b))
print(list(zip(list_a,list_b)))     #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


chars = ["a", "b", "c"]
nums = [1, 2, 3]
result_zip = list(zip(chars, nums))
my_result = list(map(lambda x,y: (x,y), chars, nums))

print(result_zip)
print(my_result)

""" 

Reduce
I na koniec metoda służąca do redukowania (zamieniania) dowolnego obiektu, po którym możemy iterować, na pojedynczą wartość. 
To wartość obliczana w wyniku dowolnej operacji przeprowadzonej na wszystkich 
elementach redukowanego obiektu (np. sumowanie, odejmowanie, mnożenie).
Ponadto, reduce pozwala określić wartość opcjonalnego argumentu initial i w ten sposób rozpoczynać operacje od dowolnej, 
skumulowanej już, wartości.
konieczne jest zaimportowanie metody reduce z modułu functools.

reduce(func, iterable, initial=optional)


"""
print("reduce zastępujące sum")
from functools import reduce

nums = [1, 2, 3, 4, 30]
result = reduce(lambda x, y:x + y, nums)
print(result)

print('opcja z argumentem initial')


nums = [1, 2, 3, 4, 30]
result = reduce(lambda x, y:x + y, nums, 10)
print(result)

print('opcja z obliczaniem iloczynu')

from functools import reduce

nums =[2, 2, 2, 2, 2, 10000]

result = reduce(lambda x,y: x * y, nums)

print(result)

""" 
Wyjaśnienie:
Reduce pobiera kolejne elementy z listy nums i przekazuje je do lambdy, która sumuje kolejne pary. 
Domyślnie sumowanie rozpoczyna się od zwiększania wartości 0, w przykładzie 1.1 zmieniamy wartość startową wyniku na 10.
Proces pobierania i sumowania kolejnych elementów odbywa się do momentu, 
kiedy nie przejdziemy po wszystkich elementach w rozpatrywanej liście nums. 

"""


""" 
Programowanie funkcyjne
"""
"""
Zad 1.
Napisz funkcję lambda, który doda wartość 15 do przesłanej wartości w postaci argumentu. Stwórz również lambdę, 
która przyjmie dwa argumenty x i y oraz obliczy ich iloczyn. Wyświetl wyniki.
"""
print("Zad 1")



add_15 = lambda x: x + 15
print(add_15(5))

multiply = lambda x, y: x * y
print(multiply(5,5))

"""
Zad 2.
Napisz program, który posortuje listę krotek przy wykorzystaniu funkcji lambda oraz metody .sort(). Lambdę wykorzystuj przy wskazaniu, 
według którego (drugiego) elementu ma odbywać się sortowanie.

to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

"""
to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(to_sort)
for elements in to_sort:
    print(elements)

#sortowanie po drugim elemencie
to_sort.sort(key = lambda x: x[1])
print(to_sort)
#sortowanie po pierwszym elemencie
to_sort.sort(key = lambda x: x[0])
print(to_sort)
#sortowanie po pierwszym elemencie, malejąco
to_sort.sort(key = lambda x: x[0], reverse= True)
print(to_sort)

#więcej przykładów sortowania: https://sparkbyexamples.com/python/sort-list-of-tuples-in-python/ i na końcu pliku
"""
Zad 3.
Stwórz program, który zwróci kwadraty oraz sześciany wartości zapisanych w liście. Wykorzystaj funkcje lambda. 

Oryginalna lista:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Kwadraty liczb:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Sześciany liczb:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""
print("Zad 3")
originals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squares = list(map(lambda x: x**2, originals))
print(squares)

number_cubes = list(map(lambda x: x**3, originals))
print(number_cubes)


"""
Zad 4.
Wykorzystując paradygmat funkcyjny oraz metodę count(), sprawdź ile ciągów nie zawiera w sobie napisu składającego
 się z dwóch 1 obok siebie.

lines = [‘10000101011’, ‘111111’, ‘01010101010010’, ‘011001100001’, ‘001010101011’]


"""
print("Zad4")

lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']
for line in lines:
    print(line)
#print("t")
#two_ones_lines = list(filter(lambda number: number if number[i] == "1" and number[i+1] =="1",line else None))
#print(f"the result is: {two_ones_lines}")

two_ones_lines = list(filter(lambda number: any(number[i] == "1" and number[i+1] == "1" for i in range(len(number)-1)), lines))
print(f"the result is: {two_ones_lines}")
"""
Zad 5.
Napisz program, który obliczy sumę trzech list o tej samej długości i zwróci wynik jednej konkretnej liczby. 
Wykorzystaj map() oraz lambdę.

nums1 = [1, 2, 3] 
nums2 = [4, 5, 6] 
nums3 = [7, 8, 9] 
"""
print("Zad 5")

#https://www.geeksforgeeks.org/sum-2d-array-python-using-map-function/
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

my_array = [nums1, nums2, nums3]
print(my_array)
summary = sum(map(sum, my_array))
print(summary)



"""

Zad 6.
Stwórz program, który przekonwertuje listę krotek na listę stringów. Wykorzystaj map().

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]



['red pink', 'white black', 'orange green']
"""
#https://codefather.tech/blog/tuple-to-string-python/?utm_content=cmp-true
print("Zad 6")
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print(colors)
result = list(map(" ".join, colors))
print(result)
#moje poniżej z bledem
convert = tuple(map(str,colors))
print(f" The result: {convert}")
convert = " ".join(map(str,colors))

print(f" The result: {convert}")

"""
Zad 7.
Mając do dyspozycji poniższą listę liczb całkowitych:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Stwórz listę new_nums, która będzie zawierała kwadraty powyższych liczb, ale tylko takich, które są parzyste. Wykorzystaj lambdy.
"""
print("Zad 7")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#squares = list(map(lambda x: x**2, originals))
#print(squares)
is_even = lambda x: x % 2 == 0
# new_nums = list(map(lambda x:x**2 if x % 2 == 0, nums))
new_nums = [num ** 2 for num in nums if is_even(num)]
new_nums = list(map(lambda x: x**2, filter(is_even, nums)))
print(list(new_nums))



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#squares = list(map(lambda x: x**2, originals))
#print(squares)

new_nums = list(map(lambda x:x**2 if x % 2 == 0 else None, nums))
print(list(new_nums))

for number in new_nums:
    new_nums.remove(None)

print(new_nums)


"""
Zad. 8
Wyobraź sobie, iż masz do dyspozycji następującą listę 4 zamówionych produktów o następujących właściwościach: 
id, nazwa, ilość, cena. 

orders = [
["34587", "Learning Python, Mark Lutz", 4, 40.95], 
["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3,32.95],
["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]

Twoim zadaniem jest stworzenie programu budującego fakturę dla powyższej listy. Lista ta ma zawierać krotki, 
które przechowywać będą kolejno id danego produktu i cenę, jaką należy za niego zapłacić. 
Jednak istnieje pewne dodatkowe utrudnienie - wartość zamówień poniżej 100 zł, musi być zwiększana o 10. 
Czyli wynikiem dla powyższej listy będzie:

invoice = [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001), ('88112', 84.97)]
"""

orders = [
["34587", "Learning Python, Mark Lutz", 4, 40.95],
["98762", "Programming Python, Mark Lutz", 5, 56.80],
["77226", "Head First Python, Paul Barry", 3,32.95],
["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]

for list in orders:
    print(orders)
for order in orders:
    print(order)
order2 =[]

for order in orders:
    order2.append(order[0])
    num = int((order[2]*order[3]))
    if num < 100:
        num += 10
        order2.append(num)
    else:
        num
        order2.append(num)

#https://appdividend.com/2022/05/30/how-to-split-list-in-python/

print(order2)
#'34587', 163, '98762', 284, '77226', 98, '88112', 74]


splitted_list =[ order2[i:i+2] for i in range(0,len(order2),2)]
print(splitted_list)
#splitted_list = [main_list[i:i+split_size] for i in range(0, len(main_list), split_size)]
#split size na ile elementów dzielimy mniejsze lsity

list_of_tuples = [tuple(small_list) for small_list in splitted_list]
print("to była opcja bez mapowania")
print(list_of_tuples)

print("opcja z mapowaniem")
list_of_mapped_tuples = list(map(tuple,splitted_list))
print(list(list_of_mapped_tuples))
invoice = list_of_mapped_tuples
print(list(list_of_mapped_tuples))






#invoice = tuple(map(lambda order: [order], order2 ))
#print(invoice)






""" 

# Quick examples of sort a list of tuples

# Example 1: Sort list of tuples 
# using list.sort()
sort_tuples = [(3, 7), (2, 12), (5, 10), (9, 0)]
sort_tuples.sort(key=lambda x: x[1])

# Example 2: Sort list of tuples 
# using sorted()
tuples = [(3, 7), (2, 12), (5, 10), (9, 0)]
sorted_tuples = sorted(tuples)

# Example 3: Sort the list of tuples by first element descending
tuples = [(2500, 'Hadoop'), (2200, 'Spark'), (3000, 'Python')]
tuples.sort(key=lambda x: x[0], reverse=True)

# Example 4: Sorted the list of tuples by first element descending
tuples = [(2500, 'Hadoop'), (2200, 'Spark'), (3000, 'Python')]
sorted_tuples = sorted(tuples, key=lambda x: x[0], reverse=True)

# Example 5: Sorted the list of tuples by second element
tuples = [(2500, 'Hadoop'), (2200, 'Spark'), (3000, 'Python')]
sorted_list = sorted(tuples, key=lambda x: x[1])

# Example 6: Sort the list of tuples by second element
tuples = [(2500, 'Hadoop'), (2200, 'Spark'), (3000, 'Python')]
tuples.sort(key=lambda x: x[1])

# Example 7: Sort list of tuples by length
tuples= [('Hyperion', 3500), ('Hadoop', 2500),('Spark', 2200), ('Python', 3000)]
tuples.sort(key=lambda x: len(x[0]))

# Example 8: Sorted list of tuples by last element
tuples = [('Hyperion', 3500), ('Hadoop', 2500),('Spark', 2200), ('Python', 3000)]
tuples = sorted(tuples, key=lambda x: x[-1])

# Example 9: Sort list of tuples by last element
tuples = [(2500, 'Spark'), (2200, 'Hadoop'), (3000, 'Python')]
tuples.sort(key=lambda x: x[-1])

# Example 10: Sort list of tuples by multiple elements
tuples = [(2500, 'Spark'), (2200, 'Hadoop'), (3000, 'Python')]
sorted_list = sorted(tuples, key=lambda x: (x[0], x[1]))


"""