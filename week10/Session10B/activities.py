"""
Session 10B: List comprehension and sets
@author: Zoe Bingham
"""

from functools import cmp_to_key

FACE_CARDS = ["Jack", "Queen", "King", "Ace"]
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]

def create_card(suit, value):
    """
    Return a card of suit and value as a list of the name. Example: create_card("Hearts", 12) -> "Queen of Hearts"

    parameters:
    :param string suit: The suit
    :param int value: The value of the card
    """

    return 

def fill_deck_set():
    """
    Create a full deck of cards using list comprehension. Return this list as a set.
    """

    return 

def fill_deck_list():
    """
    Create a full deck of cards using list comprehension. Return this list as a set.
    """

    return 

def sort_deck(deck):
    """
    Sort a deck of cards. Can you sort a set?

    parameters:
    :param set deck: a deck of cards
    """
    return 

def card_comparator(a, b):

    return 

def split_deck(deck, n):
    """
    Split a deck into n sections.

    parameters:
    :param list deck: list of cards
    :param int n: The number of sections the deck will be split into
    """

    return 

def find_card_in_list(card, deck):
    """
    Find a card in the deck.

    parameters:
    :param list card: A card with name and value
    :param list deck: A deck of cards
    """
    return 

def find_card_in_set(card, deck):
    """
    Find a card in the deck.

    parameters:
    :param list card: A card with name and value
    :param set deck: A deck of cards
    """

    return 

def main():
    print(create_card("Hearts", 5))
    print()

    deck_set = fill_deck_set()
    deck_list = fill_deck_list()

    print(deck_set)
    print(sort_deck(deck_set))
    print(find_card_in_set("Queen of Hearts", deck_set))
    print(find_card_in_list("Queen of Hearts", deck_list))
    print(split_deck(deck_list, 3))

    # make the split_deck results into sets

    # look for subsets and supersets from the deck_set and the sections of split_deck


if __name__ == "__main__":
    main()