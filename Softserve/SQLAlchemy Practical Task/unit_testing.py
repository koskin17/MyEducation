from linguist import *

def test():
    # Create Users
    user1 = User.user_create("Alice", "alice@example.com", "password123")
    user2 = User.user_create("Bob", "bob@example.com", "password456")

    assert user1.name == "Alice"
    assert user2.email == "bob@example.com"

    # Create Decks
    deck1 = Deck.deck_create("English to Ukrainian", user1.id)
    deck2 = Deck.deck_create("Basic Phrases", user2.id)

    assert deck1.name == "English to Ukrainian"
    assert deck2.user_id == user2.id

    # Create Cards
    card1 = Card.card_create(user1.id, "hello", "привіт", "Think of 'private' for 'привіт'")
    card2 = Card.card_create(user1.id, "goodbye", "до побачення", "Similar to 'to see' you again")

    assert card1.translation == "привіт"
    assert card2.tip == "Similar to 'to see' you again"

    # Update User
    User.user_update_name(user1.id, "Alicia")
    assert user1.name == "Alicia"

    # Update Card
    Card.card_update(card1.id, word="hi", translation="здоров")
    assert card1.word == "hi"
    assert card1.translation == "здоров"

    # Filter Cards
    filtered_cards = Card.card_filter("good")
    assert len(filtered_cards) == 1  # "goodbye" contains "good"

    # Delete Deck
    Deck.deck_delete_by_id(deck1.id)
    print(deck1.id)
    assert Deck.deck_get_by_id(deck1.id) is None

    print("All tests passed.")

if __name__ == "__main__":
    test()
