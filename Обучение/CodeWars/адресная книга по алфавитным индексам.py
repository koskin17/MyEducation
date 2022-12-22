import string


class AddressBook:
    def __init__(self):
        self.addresses = []

    def add_address(self, name, address):
        self.addresses.append((name, address))

    def get_addresses_by_first_letters(self, letters):
        letters = letters.upper()
        return [(name, address) for name, address in self.addresses
                if any(name.upper().startswith(letter) for letter in letters)]

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.get_addresses_by_first_letters(key)
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            letters = (
            string.ascii_uppercase[string.ascii_uppercase.index(start):string.ascii_uppercase.index(stop) + 1:step])
            return self.get_addresses_by_first_letters(letters)


address_book = AddressBook()
address_book.add_address("Sherlock Holmes", "221B Baker St., London")
address_book.add_address("Wallace and Gromit", "62 West Wallaby Street, Wigan, Lancashire")
address_book.add_address("Peter Wimsey", "110a Piccadilly, London")
address_book.add_address("Al Bundy", "9764 Jeopardy Lane, Chicago, Illinois")
address_book.add_address("John Dolittle", "Oxenthorpe Road, Puddleby-on-the-Marsh, Slopshire, England")
address_book.add_address("Spongebob", "124 Conch Street, Bikini Bottom, Pacific Ocean")
address_book.add_address("Hercule Poirot", "Apt. 56B, Whitehaven Mansions, Sandhurst Square, London W1")
address_book.add_address("Bart Simpson", "742 Evergreen Terrace, Springfield, USA")

print(string.ascii_uppercase)
print(string.ascii_uppercase.index("A"))
print(string.ascii_uppercase.index("Z"))

print(address_book["A"])
print(address_book["B"])
print(address_book["S"])
print(address_book["A":"H"])

'''
Разбираемся в созданном классе AddressBook.
Метод get_addresses_by_first_letters():

Этот метод фильтрует все адреса, принадлежащие имени, которые начинаются с любой буквы в аргументе letters. Во-первых, эта функция нечувствительна к регистру, так как преобразует буквы в верхний регистр. Затем используется генератор списка поверх внутреннего списка адресов. Условие внутри генератора списка проверяет, соответствует ли какая-либо из предоставленных букв первой букве, соответствующее значению имени.

Метод __getitem__:

Чтобы сделать объекты адресной книги доступными для использования среза, необходимо переопределить магический метод Python __getitem__.

Сначала проверяется, является ли ключ строкой. Это будет иметь место, если получаем доступ к объекту с помощью одной буквы в квадратных скобках, например так: address_book['A']. Для этого тривиального случая можно просто вернуть любые адреса, имя которых начинается с данной буквы.

Интересная часть, когда ключ является объектом среза. Например, этому условию будет соответствовать обращение типа address_book['A':'H']. Во-первых, идентифицируются все буквы в алфавитном порядке между буквами A и H. Модуль string перечисляет все латинские буквы в string.ascii_uppercase. Далее используется срез для извлечения букв между заданными буквами. Обратите внимание на +1 во втором параметре среза. Таким образом, гарантируется, что последняя буква является включающей, а не исключающей.

После того, как определили все буквы в последовательности, используется метод get_addresses_by_first_letters(), о котором говорилось выше.
'''
