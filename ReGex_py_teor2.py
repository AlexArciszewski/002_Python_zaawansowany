"""
REGEX teoria:

Zanim przejdziemy do konkretów, chciałbym zwrócić jeszcze uwagę na to, gdzie najczęściej możemy wykorzystywać wyrażenia regularne:
−	Tworząc uniwersalne i efektywne rozwiązania do problemów bazujących na trudnościach w znalezieniu pewnych wzorców w tekście
−	Przetwarzając długie teksty, np. e-maile i chcąc wyłuskać z nich typowe frazy świadczące o spamie. Technika ta może okazać się niezwykle przydatna przy trenowaniu własnego modelu wykorzystującego algorytmy uczenia maszynowego.
−	Przy web scrapingu podczas procesu rozpoznawczego (w cyberbezpieczeństwie, tzw. rekonesans), szukając luk w serwisach i potencjalnych wycieków danych.

Bardziej przyziemne przykłady:
Analizując natomiast przegląd możliwych zastosowań ReGex przy codziennej pracy z kodem to choćby przypadki, gdy chcemy:
●	Przeanalizować tekst pod kątem obecności pewnych wzorców
●	Porównać cały tekst z dowolnym wzorcem (patternem)
●	Przeprowadzić proces strings slicing’u
●	Gdy chcemy sformatować tekst i zmodyfikować jego części na inne
"""
# 1.kod pocztowy:

# 01-234
# Regex: [0-9]{2}-[0-9]{3}  lub \d{2}-\d{3}


# 2.nr tel
# \d{9} lub [0-9]{9}

# 3Flagi

# global  -  dodanie tej flagi do wyrażenia, umożliwia Nam wyszukanie w tekście wszystkich wystąpień danego pattern’u.
#           Gdybyśmy nie umieścili tej flagi, wówczas wyszukanie łańcucha 'nie', ograniczyłoby się tylko do wyszukania jego pierwszego wystąpienia w tekście.
# multiline - ^ poczatek $ koniec m - multi line do dowolnego wyrażenia, umożliwia sprawdzenie, czy każda linia rozpoczyna się od danego wzoru tekstu.
# insensitive - nie zwraca uwagi na dużą literę szukamy nie i Nie
# Flaga s umożliwia więc dopasowywanie znaków przejścia do nowej linii do odpowiednio stworzonego pattern’u (cały tekst jest traktowany tak, jakby był jednolinijkowy).

# W tej sekcji zajmiemy się znakami ^ oraz $.

# Znak kareta (^) umieszczany przed danym słowem/pattern'em, sprawdza czy dane wyrażenie znajduje się na początku tekstu.
# Znak dolara ($) umieszcza się go na końcu wyrażenia i umożliwia sprawdzenie, czy wyrażenie znajduje się na końcu tekstu.

"""
Wbudowane klasy znaków
Powstały z racji częstego wykorzystywania tych samych grup znaków.

Do dyspozycji mamy:
−	\d - dowolna cyfra
−	\D - dowolny znak niebędący cyfrą
−	\s - dowolny biały znak (np. spacja)
−	\S - dowolny znak niebędący białym znakiem
−	\w - dowolny znak należący do słowa (cyfry, litery i znak _)
−	\W - dowolny znak nie należący do słowa

Pozostałe klasy:
−	[[:digit:]] dowolny znak będący cyfrą
−	[[:alpha:]] dowolny znak będący literą
−	[[:alnum:]] dowolny znak będący literą lub cyfrą
−	[[:lower:]] dowolny znak będący małą literą
−	[[:upper:]] dowolny znak będący dużą literą
−	[[:punct:]] dowolny znak interpunkcyjny
"""

""" 
Klasy umożliwiają tworzenie o wiele krótszych wyrażeń regularnych, Twór ten umożliwia "grupowanie/klasowanie" pewnych powtarzających się zależności 
- czyli, np. zamiast wypisywać wszystkie możliwe do pojawienia się cyfry, zastosujemy token \d.

Silnik ReGex interpretuje kropkę jako dopasowanie do każdego znaku. Każdego! Czyli litery, cyfry, znaki diakrytyczne, spacje, ale... nie przejścia do nowej linii. 
Spójrz:
Chcąc do grona rozpatrywanych znaków, zaliczyć również znak '\n' (przejście do nowej linii), należy zastosować flagę s - single line.

Chcąc znaleźć zatem wszystkie pozostałe znaki, które nie zaliczają się do zbioru [abcdef], zapiszemy [^abcdef].
"""

import re

"""  
Metody modułu re
re.match
Metoda ta dopasowuje wyrażenie do danego tekstu i zwraca dopasowane grupy. 
Jej argumenty to: 
−	pattern (wyrażenie do dopasowania)
−	string (tekst, do którego wyrażenie będzie dopasowane)
−	flags (flagi; poszczególne z nich rozdzielamy za pomocą |)

Syntax:
re.match(pattern, string, flags=0)

Użycie:
match.group() – odczytanie całego dopasowania
match.group(N) – odczytanie N-tej grupy dopasowania

"""
print("1 re.match")
# 1 re.match

import re

txt = "Devs-Mentoring 2023"

match = re.match(r'(.*)(-)(\S*) (\d{4})', txt)

if match:
    print(match.group())  # "Devs-Mentoring 2023"
    print(match.group(1))  # Devs
    print(match.group(2))  # -
    print(match.group(3))  # Mentoring
    print(match.group(4))  # 2023
else:
    print("No match!")

# 2 re.search

""" 
Metoda odnajduje pierwsze wystąpienie dopasowanego przez wyrażenie regularne substringa w obrębie danego tekstu.
Argumenty tej metody są takie same jak w przypadku re.match, stąd sygnatura tej metody to:

re.search(pattern, string, flags=0)

Należy jednak zwrócić uwagę na różnicę między re.search a re.match. Otóż re.match szuka dopasowania tylko od początku 
danego napisu, a re.search dopasowuje dowolny wyraz z tekstu. 
Chcąc więc wyszukać, czy na końcu tekstu znajduje się cyfra, skorzystamy z search. Natomiast w przypadku konieczności zbadania,
czy tekst zaczyna się od 4-literowego wyrazu, możemy użyć zarówno re.match jak i re.search.



"""
print("2 re.search")
import re

txt = "Devs-mentoring 2021"

match_first_word = re.match(r'\S{4}', txt)
search_first_word = re.search(r'\S{4}', txt)
match_number = re.match(r'\d{4}', txt)
search_number = re.search(r'\d{4}', txt)

print(match_first_word.group())  # Devs
print(search_first_word.group())  # Devs

print(match_number)  # None
print(search_number.group())  # 2021

print("3-re_sub")

# re-sub

""" 
re.sub(pattern, repl, string, max=0)

Metoda ta zastępuje wszystkie dopasowania RE pattern w zmiennej string nowym łańcuchem, którym jest repl. Metoda zwraca zmodyfikowanego stringa.

"""

import re

txt = "Devs-mentoring 2021 # To moja nazwa"

plain_txt = re.sub(r'#.*$', "", txt)
print(plain_txt)

print("4 re.split")

""" 
re.split(pattern, str, max=default, flags)

Metoda zwraca listę elementów, według których string został podzielony. Możemy również przez przekazanie 3. argumentu, zdefiniować, ile maksymalnie 
razy ma zostać podzielony napis według podanego wyrażenia.

"""
import re

txt = "1 2 3 4 5 4 3 2 1"
parts = re.split(r'\s', txt)
print(parts)

""" 
Zad. 1
Napisz program, który sprawdzi, czy string zawiera tylko i wyłącznie zbiór następujących znaków: (a-z, A-Z i 0-9).

"""

"""
import re
string = "ABCabc123"
correct = set(string.ascii_letters + string.digits)
if string in correct:
    print(True)

my_pattern = re.compile("[A-Za-z0-9]+")
my_pattern.fullmatch(string)

pattern = bool(re.match("^[A-z0-9]*S",string))
"""
print("Zadanie 1")
import re

string = "ABCabc123"

pattern = bool(re.match("[A-z0-9]", string))
print(pattern)

""" 
Zad. 2
Sprawdź, czy string rozpoczyna się pojedynczą cyfrą: 0 lub literą ‘b’.

"""
print("Zadanie 2")

import re

string = "bABCabc123"
# string = "bABCabc123"

pattern = bool(re.match("[0|b]", string))
print(pattern)

""" 
Zad. 3
Sprawdzaj, czy podany string zawiera ciąg dowolnych małych liter rozdzielonych znakiem _, np. aab_cbbbc

"""

print("Zadanie 3")

import re

string = "aab_cbbc"
# string = "bABCabc123"

pattern = bool(re.match("^([a-z]+)(_[a-z]+)+$", string))
print(pattern)

""" 
Zad. 4
Znajdź słowa, które kończą się co najmniej dwiema literami ‘s’, np.
-	hiss 
-	hisssss 
-	His

"""
print("Zadanie 4")
import re

string = "hissss"

pattern = bool(re.match("^([a-z]+)([ss]+)+$", string))
print(pattern)

""" 
Zad. 5
Znajdź stringa, który zawiera co najmniej sześć liter i nie zawiera litery ‘A’, np.

-	unique New York 
ale niepasujące:
-	Regular Expressions 
-	ALOHA 
-	Python should match

"""
print("Zadanie 5")
import re

string = "Regular Expressions"  # unique New York
# pattern = bool(re.match("^([B-z]{6,}+)|([^Aa]+)+$", string))
pattern = r"^(?!.*A).*\b\w{6,}\b.*$"
print(bool(re.search(pattern, "unique New York")))
#pattern = bool(re.match("^([B-z]{6,})+$", string))  # "Regular Expressions"

# print(pattern)


""" 
Zad. 6
W stringu HTML, wszystkie elementy otoczone są pewnymi znacznikami HTML (<p>Twój tekst</p>, <h1>Twój tekst2</h1> itd.).
Każdy znacznik ma następującą postać: <znacznik>Tekst</znacznik>.

Twoje zadanie to określić, czy podany tekst jest prawidłowym elementem kodu HTML, czyli czy składa się z odpowiednio skonstruowanych znaczników 
wraz z dowolnym tekstem pomiędzy nimi. Trudność, jaką możesz tutaj napotkać, to konieczność ominięcia, tzw. chciwego przeszukiwania, 
które omówiliśmy w szkoleniu.





Przykłady:
<span>Yowza! That’s a great regular expression.</span> - powinno wyszukać cały tekst
<p>Learn about regular expressions here.</p> <p>You\'re going to love them!</p> - powinno wyszukać:
-	<p>Learn about regular expressions here.</p>
-	<p>You\'re going to love them!</p> 

Nieprawidłowe przykłady:
I'm not HTML!! 
<p>Incomplete HTML 

"""

""" 
Zad 7.
Zakładając, że masz dostęp do adresu w formacie: username@companyname.com, napisz program, który wydrukuje nazwę firmy z takiego adresu. 
Zarówno nazwa użytkownika jak i nazwa firma może składać się tylko i wyłącznie z liter.


"""

""" 
Zad 8.
Napisz program, który przyjmować będzie dowolny ciąg znaków oddzielonych spacją. Wyodrębnij z niego tylko i wyłącznie te wyrazy, które są liczbami.

Przykładowo dla poniższych danych wejściowych:
2 cats and 3 dogs

Zwróć:
[‘2’, ‘3’]

"""

""" 
Zad. 9
Napisz wyrażenie, które sprawdza, czy liczba zmiennoprzecinkowa podana przez użytkownika ma poprawny format. 
Na przykład liczba 123,2341515132135 lub -10 są poprawne, ale 18-12 czy 123, (przecinek na końcu) już nie.

"""

""" 
Zad. 10
Efektem zbierania pomiarów temperatury okazał być się plik tekstowy, który zawiera datę pomiaru oraz wartość. W jaki sposób możliwe jest wydzielenie tylko dat w takiej sytuacji? Poniżej znajduje się fragment przykładowych danych wejściowych.

"2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"


"""

"""
Zad. 11
Sprawdź, czy podany string jest zapisem koloru w systemie szesnastkowym (HEX).
-	string musi się zaczynać znakiem #
-	następnie musi zawierać 3 lub 6 (ale nie 4 lub 5) znaki kodu szesnastkowego pisane małą lub wielką literą; 

Przykłady:
#ab4 
#AB4B72 

Błędne przykłady:
#ab43 
#aaaaaaaaa 
#ahl 



"""
"""
 Complete the solution so that it splits the string into pairs of two characters. If the string contains an 
 odd number of characters then it should replace the missing second character of the final pair with an 
 underscore ('_').
Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def split_pairs(s):
    if len(s) % 2 != 0:
        s += "_"
    result = []
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result



def split_pairs(s):
    if len(s) % 2 != 0:
        s += "_"
    result = []
    pair = ""
    for char in s:
        pair += char
        if len(pair) == 2:
            result.append(pair)
            pair = ""
    return result

print(split_pairs('hello'))
print(split_pairs('helloo'))


import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! it has been an hour!",
            timeout = 10
        )
        time.sleep(3600)