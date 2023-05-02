
"""
Zad. 1
Przygotuj klasę FileHandler, która symulować będzie funkcjonalność obsługiwania plików w Python.
Ma ona przechowywać pola takie jak: file_path, no_connectors, max_file_size. Będa one ustawiane
z poziomu odpowiednich setterów jak i konstruktora. Klasa ta ma dodatkowo przechowywać takie metody
 jak read_content, save_to_file, w których umieścisz, tzw. dummy printy (będziesz drukował dowolny tekst).

Celem tego zadania nie jest stworzenie odpowiedniej logiki biznesowej dla klasy, tylko zaprojektowanie
klasy, która będzie zwracała odpowiedni user-defined wyjątek w zależności od przekazania do obiektu klasy
niewłaściwej danej, np. pustego stringa, który będzie miał być umieszczony pod polem file_path.

Dodatkowe warunki:
Wartość noConnector nie może przekroczyć wartości 10
maxFileSize musi być zawsze liczbą czterocyfrową
"""

"""

def set_file_path(self, file_path):
    self.__file_path = file_path
    try:
        len(self.__file_path) >8
    except TypeError:
        print("Wrong data format")

    else:
        print(f"{file_path} is correct")

"""

class FileHandler:

    def __init__(self, file_path: str, no_connectors: int, max_file_size: int):
        self.file_path = file_path # __ setter nie działa przy wywoływaniu kosntruktora.
        self.__no_connectors = no_connectors
        self._max_file_size = max_file_size
#noConnector max 10
#maxFileSize musi być zawsze liczbą czterocyfrową

    #getter for __file_path
    @property
    def file_path(self):
        return self._file_path

    # setter for __file_path
    @file_path.setter
    def file_path(self, value):
        if not len(value) != 0:
            self._file_path = value
        raise TypeError('file_path cannot be emtpy.')

    #
    # def validate_file(self, value):
    #     if not len(value) != 0:
    #         self._file_path = value
    #     raise TypeError('file_path cannot be emtpy.')

    #
    #
    # def __str__(self) -> str:
    #     return f"That's a helluuaa filehandler"
    #
    # # getter for __no_connectors
    # def get_no_connectors(self):
    #     return self.__no_connectors
    #
    # # setter for __no_connectors
    # def set_no_connectors(self, no_connectors):
    #     self.__no_connectors = no_connectors
    #     if self.__no_connectors > 10:
    #         raise ValueTooHighError
    #     else:
    #         return f"no_conenctors value is {self.__no_connectors} and it's fine"


    #getter for __max_file_size = max_file_size
    # def get_max_file_size(self):
    #     return self.__max_file_size
    #
    # #setter for __max_file_size
    # def set_max_file_size(self, max_file_size):
    #     self.__max_file_size = max_file_size
    #     try:
    #         self.__max_file_size = max_file_size
    #     except:
    #         print("Invalid value Dummy")
    #     else:
    #         if self.__max_file_size > 9999:
    #             print("The file is to heavy")
    #         else:
    #             return print('File is ok')
    #

    # @staticmethod
    # def read_content():
    #     print("This is some string from static method")
    #
    #
    # def save_to_file(self):
    #     return f" U saved it Baby"


def main():
    file_001 = FileHandler("C:\Dane\2_programowanie python\26_Devs_Mentoring", 5, 9900)
    file_002 = FileHandler("", 5, 9900)
    # print(File_001)#zamiast tego wywoła się str lub repr
    # #print(File_001.get_file_path())
    # print(File_001.set_file_path("C:\Dane\2_programowanie python\26_Devs_Mentoring"))
    # #File_001.set_file_path("")  #działa dopiero przy wywołaniu samego setera
    # #print(File_001.set_no_connectors(11)) #gdzie zdefiniowac error jak w przykładzie ze strony 16 w zszywce Tu cos nie tak
    # File_001.read_content()
    # print(File_001.save_to_file())
    # print(File_001.set_max_file_size(9900))

if __name__ == "__main__":
    main()

    #dlaczego musze wywołać settery na obiektach aby sprawdzać załozenia dotyczące path i wagi pliku...
