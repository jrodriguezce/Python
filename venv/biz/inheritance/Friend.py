'''
Clase para implementar herencia.
@Autor: Anderson Rodriguez
'''

from inheritance.Contact import Contact

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.__phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        print("Seteando el nuevo celular {}".format(new_phone))
        self.__phone = new_phone