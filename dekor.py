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
    def inner(*args,**kwargs):
        print("Got decorated")
        return func(*args, *kwargs)
    
    return inner


@make_universal
def ordinary_no_params():
    print("no params")

@make_universal
def ordinary_two_params(param1, param2):
    print(f"Two params: {param1} {param2}")

ordinary_no_params()
ordinary_two_params("one","two")

