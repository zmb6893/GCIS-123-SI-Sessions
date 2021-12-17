"""
Session 9B: Tuples, Lists, and Slicing
@author: Zoe Bingham
"""

def tuple_tuple_tuple():
    # What will happen if we try to modify a tuple?
    tup = ("hello", 4, 6.0)
    print(tup[0])
    tup[0] = "new value"
    print(tup)
    print()

def list_list_list():
    # What will happen if we try to modify a list?
    lis = ["hello", 4, 6.0]
    removed = lis.pop()
    lis.append("new value")
    print(lis)
    print()

def sort_string(string):
    """
    Sort a string to be in alphabetical order. Return the sorted string.
    """
    return

def chess_key(piece):
    """
    Make a sort_key for chess pieces.
    """
    return

def main():
    # uncomment these in the appropriate order
    '''
    print("tuple function:")
    tuple_tuple_tuple()
    '''

    '''
    print("list function")
    list_list_list()
    '''
    
    '''
    string = "What is the crabby patty formula?"

    print("sort string function")
    sort_string(string)
    '''

    '''
    chess_pieces = ["pawn", "rook", "bishop", "king", "queen", "knight", "pawn", "knight", "pawn"]
    chess_pieces.sort() # <-- What goes is here?
    '''

    # How do we slice a string?
    

main()