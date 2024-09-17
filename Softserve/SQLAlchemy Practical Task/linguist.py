from random import randint


class User:
    """Class for create new user and implement different methods for process user information"""

    users = []  # List / Database of existing users
    existing_user_id = [] #List for fixation used id

    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def user_create(cls, name, email, password):
        """Function for create a new user and append him to the database of existing users"""

        user_id = randint(0, 1000000000)
        while user_id in cls.existing_user_id:
            user_id = randint(0, 1000000000)

        cls.existing_user_id.append(user_id)
        user = cls(user_id, name, email, password)
        cls.users.append(user)
        return user

    @classmethod
    def user_get_by_id(cls, user_id):
        """Function for getting information about user by user ID"""

        for user in cls.users:
            if user.id == user_id:
                return user
            return f"User with specified ID={user_id} not found."

    @classmethod
    def user_update_name(cls, user_id, new_name):
        """Function for update user's name"""

        user = cls.user_get_by_id(user_id)
        if user:
            user.name = new_name
            return user
        return f"User with specified ID={user_id} not found"

    @classmethod
    def user_change_password(cls, user_id, old_password, new_password):
        """Function for update the user's password"""

        user = cls.user_get_by_id(user_id)
        if user and user.password == old_password:
            user.password = new_password
            return "Password was successfully  changed"
        return f"You have entered an incorrect ID of user = {user_id} or old password = {old_password}."

    @classmethod
    def user_delete_by_id(cls, user_id):
        """Function for delete user by his ID"""

        user = cls.user_get_by_id(user_id)
        if user:
            cls.users.remove(user)
            return f"User with ID={user_id} deleting  successful"
        return f"User with id={user_id} not found."


class Deck:
    """Class for create new desk and implement different methods for process information about desk"""

    users_desks = []  # List / Database of existing desks
    existing_deck_id = []  # List for fixation deck id

    def __init__(self, deck_id, name, user_id):
        self.id = deck_id
        self.name = name
        self.user_id = user_id

    @classmethod
    def deck_create(cls, name, user_id):
        """Function for create deck"""

        deck_id = randint(0, 1000000000)

        while deck_id in cls.existing_deck_id:
            deck_id = randint(0, 1000000000)

        deck = cls(deck_id, name, user_id)
        cls.users_desks.append(deck)
        return deck

    @classmethod
    def deck_get_by_id(cls, deck_id):
        """Function for getting information about deck by deck id"""

        for deck in cls.users_desks:
            if deck.id == deck_id:
                return deck
        return None

    @classmethod
    def deck_update(cls, deck_id, name):
        """"Function for update user's deck"""

        deck = cls.deck_get_by_id(deck_id)
        if deck:
            deck.name = name
            return deck
        return f"Deck with ID = {deck_id} not found."

    @classmethod
    def deck_delete_by_id(cls, deck_id):
        """Function for delete deck by deck id"""

        deck = cls.deck_get_by_id(deck_id)
        if deck:
            cls.users_desks.remove(deck)
            return f"Deck with ID = {deck_id} was successfully delete."
        return None

class Card:
    """Class for create cards for user's deck and implement different methods for process information about card"""

    deck_cards = []  # List / Database of existing cards in deck
    existing_cards_id = []  # List for fixation cards id

    def __init__(self, card_id, user_id, word, translation, tip):
        self.id = card_id
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

    @classmethod
    def card_create(cls, user_id, word, translation, tip):
        """Function for create card"""

        card_id = randint(0, 1000000000)
        while card_id in cls.existing_cards_id:
            card_id = randint(0, 1000000000)

        card = cls(card_id, user_id, word, translation, tip)
        cls.deck_cards.append(card)
        return card

    @classmethod
    def card_get_by_id(cls, card_id):
        """Function for getting information about card by card id"""

        for card in cls.deck_cards:
            if card.id == card_id:
                return card
        return None

    @classmethod
    def card_filter(cls, sub_word):
        result = []
        for card in cls.deck_cards:
            if sub_word in card.word or sub_word in card.translation or sub_word in card.tip:
                result.append(card)
        return tuple(result)

    @classmethod
    def card_update(cls, card_id, word=None, translation=None, tip=None):
        card = cls.card_get_by_id(card_id)
        if card:
            if word:
                card.word = word
            if translation:
                card.translation = translation
            if tip:
                card.tip = tip
        return card

    @classmethod
    def card_delete_by_id(cls, card_id):
        card = cls.card_get_by_id(card_id)
        if card:
            cls.deck_cards.remove(card)
            return True
        return False
