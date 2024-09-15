class User:
    def __init__(self, username):
        self.username = username
        self.decks = []

    def create_deck(self, deck_name):
        deck = Deck(deck_name)
        self.decks.append(deck)
        return deck

    def get_deck(self, deck_name):
        for deck in self.decks:
            if deck.name == deck_name:
                return deck
        return None

    def delete_deck(self, deck_name):
        self.decks = [deck for deck in self.decks if deck.name != deck_name]

    def update_deck(self, old_name, new_name):
        deck = self.get_deck(old_name)
        if deck:
            deck.name = new_name
            return deck
        return None

    def list_decks(self):
        return [deck.name for deck in self.decks]


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def create_card(self, english_word, ukrainian_word, tip):
        card = Card(english_word, ukrainian_word, tip)
        self.cards.append(card)
        return card

    def get_card(self, english_word):
        for card in self.cards:
            if card.english_word == english_word:
                return card
        return None

    def update_card(self, english_word, new_english_word=None, new_ukrainian_word=None, new_tip=None):
        card = self.get_card(english_word)
        if card:
            if new_english_word:
                card.english_word = new_english_word
            if new_ukrainian_word:
                card.ukrainian_word = new_ukrainian_word
            if new_tip:
                card.tip = new_tip
            return card
        return None

    def delete_card(self, english_word):
        self.cards = [card for card in self.cards if card.english_word != english_word]

    def list_cards(self):
        return [(card.english_word, card.ukrainian_word, card.tip) for card in self.cards]


class Card:
    def __init__(self, english_word, ukrainian_word, tip):
        self.english_word = english_word
        self.ukrainian_word = ukrainian_word
        self.tip = tip


# Example Usage

# Create a user
user = User("john_doe")

# Create a deck for the user
deck = user.create_deck("Basic Ukrainian")

# Add cards to the deck
deck.create_card("Hello", "Привіт", "Sounds like 'Privet' in Russian")
deck.create_card("Thank you", "Дякую", "Imagine you're thanking someone with a 'Yak'")
deck.create_card("Please", "Будь ласка", "Think of 'bud' as in a flower bud")

# List cards in the deck
print("Cards in deck:", deck.list_cards())

# Update a card
deck.update_card("Hello", new_ukrainian_word="Вітаю", new_tip="Sounds more formal like 'Vitayu'")

# List updated cards in the deck
print("Updated cards in deck:", deck.list_cards())

# Delete a card
deck.delete_card("Please")

# List cards after deletion
print("Cards after deletion:", deck.list_cards())

# List all decks of the user
print("User's decks:", user.list_decks())

"""

Here is the structure of the linguist application in Python using object-oriented programming (OOP) principles, which includes three models: User, Deck, and Card. Each model supports CRUD (Create, Read, Update, Delete) operations.

python
Копировать код
class User:
    def __init__(self, username):
        self.username = username
        self.decks = []

    def create_deck(self, deck_name):
        deck = Deck(deck_name)
        self.decks.append(deck)
        return deck

    def get_deck(self, deck_name):
        for deck in self.decks:
            if deck.name == deck_name:
                return deck
        return None

    def delete_deck(self, deck_name):
        self.decks = [deck for deck in self.decks if deck.name != deck_name]

    def update_deck(self, old_name, new_name):
        deck = self.get_deck(old_name)
        if deck:
            deck.name = new_name
            return deck
        return None

    def list_decks(self):
        return [deck.name for deck in self.decks]


class Deck:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def create_card(self, english_word, ukrainian_word, tip):
        card = Card(english_word, ukrainian_word, tip)
        self.cards.append(card)
        return card

    def get_card(self, english_word):
        for card in self.cards:
            if card.english_word == english_word:
                return card
        return None

    def update_card(self, english_word, new_english_word=None, new_ukrainian_word=None, new_tip=None):
        card = self.get_card(english_word)
        if card:
            if new_english_word:
                card.english_word = new_english_word
            if new_ukrainian_word:
                card.ukrainian_word = new_ukrainian_word
            if new_tip:
                card.tip = new_tip
            return card
        return None

    def delete_card(self, english_word):
        self.cards = [card for card in self.cards if card.english_word != english_word]

    def list_cards(self):
        return [(card.english_word, card.ukrainian_word, card.tip) for card in self.cards]


class Card:
    def __init__(self, english_word, ukrainian_word, tip):
        self.english_word = english_word
        self.ukrainian_word = ukrainian_word
        self.tip = tip


# Example Usage

# Create a user
user = User("john_doe")

# Create a deck for the user
deck = user.create_deck("Basic Ukrainian")

# Add cards to the deck
deck.create_card("Hello", "Привіт", "Sounds like 'Privet' in Russian")
deck.create_card("Thank you", "Дякую", "Imagine you're thanking someone with a 'Yak'")
deck.create_card("Please", "Будь ласка", "Think of 'bud' as in a flower bud")

# List cards in the deck
print("Cards in deck:", deck.list_cards())

# Update a card
deck.update_card("Hello", new_ukrainian_word="Вітаю", new_tip="Sounds more formal like 'Vitayu'")

# List updated cards in the deck
print("Updated cards in deck:", deck.list_cards())

# Delete a card
deck.delete_card("Please")

# List cards after deletion
print("Cards after deletion:", deck.list_cards())

# List all decks of the user
print("User's decks:", user.list_decks())
Breakdown of Models:
User:
Has a username and a list of decks.
CRUD operations for managing decks (creating, reading, updating, deleting).
Deck:
Has a name and a list of cards.
CRUD operations for managing cards within the deck.
Card:
Represents a flashcard with an English word, its Ukrainian translation, and a memory tip.
"""

"""
Example Output:
Cards in deck: [('Hello', 'Привіт', "Sounds like 'Privet' in Russian"), ('Thank you', 'Дякую', "Imagine you're thanking someone with a 'Yak'"), ('Please', 'Будь ласка', "Think of 'bud' as in a flower bud")]
Updated cards in deck: [('Hello', 'Вітаю', "Sounds more formal like 'Vitayu'"), ('Thank you', 'Дякую', "Imagine you're thanking someone with a 'Yak'"), ('Please', 'Будь ласка', "Think of 'bud' as in a flower bud")]
Cards after deletion: [('Hello', 'Вітаю', "Sounds more formal like 'Vitayu'"), ('Thank you', 'Дякую', "Imagine you're thanking someone with a 'Yak'")]
User's decks: ['Basic Ukrainian']
"""