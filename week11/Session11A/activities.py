"""
Session 11A: Dictionaries and some hash stuff
@author: Zoe Bingham
"""

import csv

# What are 3 things to consider while making a good hash?
# :) Nice job guys.
# Why do we use hashes?
# unique key.

def make_word_dictionary():
    """
    Make a dictionary using a word as a key and it's definition as the value.
    """
    return

def make_chess_pieces(csv_file):
    """
    Return a dictionary for chess pieces. The key should be the name, the value should be the count from a given csv_file
    """
    pieces = dict()
    with open(csv_file) as AJ:
        csv_reader = csv.reader(AJ)
        next(AJ)
        for element in csv_reader:
            name = element[0]
            number = element[1]
            pieces[name] = number
    return pieces

def place_pieces_on_board(dictionary):
    """
    Challenge: Use list comprehension to make an 8X8 board and place the chess pieces in their respective locations.
    Return the 2D list.
    """
    board = list()
    row = list()

    [board.append([row.append(i) for i in range(0,8)]) for j in range(0,8)]

    board.append([["pawn" for value in dictionary] for _ in range(0, int(dictionary["pawn"]))])

    return board

def chess_hash(piece):
    """
    Make a hash for a chess piece with no conditional statements
    """ 

    return ord(piece[0])

def main():
    """dictionary = make_chess_pieces("chess.csv")
    print(board:=place_pieces_on_board(dictionary))

    for row in range(0,7):
        for col in range(0,7):
            print("%s\t"%(board[row][col]))
        print("\n")"""

    numbers = dict()
    numbers= {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
    print(numbers)
    print(numbers[1])
    if(1 in numbers):
        print("one is in numbers")
    pass

if __name__ == "__main__":
    main()

