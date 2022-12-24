class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    """Метод проверки на равенство с различными значениями"""

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if self.rating == other:
                return True
            else:
                return False
        elif isinstance(other, ChessPlayer):
            if self.rating == other.rating:
                return True
            else:
                return False
        else:
            return "Невозможно выполнить сравнение."

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            if self.rating > other:
                return True
            else:
                return False
        elif isinstance(other, ChessPlayer):
            if self.rating < other.rating:
                return True
            else:
                return False
        else:
            return "Невозможно выполнить сравнение."

    """Метод проверки на больше, как противоположное значение метода проверки на меньше __lt__"""

    def __qt__(self, other):
        return self > other


magnus = ChessPlayer("Carlsen", "Magnus", 2847)
ian = ChessPlayer("Ian", "Nepomniachtchi", 2789)
print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus == "Player")
print(magnus > ian)
print(magnus < ian)
print(magnus < [1, 2])
