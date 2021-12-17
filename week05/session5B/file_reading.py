"""
Session 5B: File Reading activities.
@author: Zoe Bingham
"""

def print_line_by_line(filename):
    '''
    Open a file and print each line. Between each line, print a '...'

    Parameters:
    :param string filename: the name of the file to be opened
    '''
    pass

def print_character_by_character(filename):
    '''
    Open a file and print each line. Print each character in this format "(C)"

    Parameters:
    :param string filename: the name of the file to be opened
    '''
    pass

def print_word_by_word(filename):
    '''
    Open a file and print each line. Print each word in the file separated by a new line

    Parameters:
    :param string filename: the name of the file to be opened
    '''
    pass

def make_text_emoji(filename):
    '''
    Open a file and use each character to make an emoji. (Ex: O becomes (O_O) or P becomes (P_P). You can get more creative too). Ignore whitespace

    Parameters:
    :param string filename: the name of the file to be opened'''
    pass

def main():
    file1 = "data/o_o.txt"
    file2 = "data/who_am_I.txt"
    file3 = "data/huh.txt"
    file4 = "data/hmmm.txt"
    print_line_by_line(file1)
    print_character_by_character(file2)
    print_word_by_word(file3)
    make_text_emoji(file4)

if __name__ == "__main__":
    main()