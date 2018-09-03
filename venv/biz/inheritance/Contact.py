'''
Super clase para implementar herencia.
@Autor: Anderson Rodriguez
'''
class Contact:

    all_contacts = []

    def __init__(self, name, email):
        self.__name     = name
        self.__email    = email
        self.all_contacts.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Seteando el nuevo valor!")
        self.__name = new_name

    def count_contacts(self):
        return self.all_contacts.count()