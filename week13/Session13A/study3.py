"""
Practicum Review
@author: Zoe Bingham
"""

def make_tuple(a,b,c):
    """
    Returns a tuple containing all three parameters.
    """
    pass

def reverse_tuple(sequence):
    """
    Returns a tuple containing the values in the sequence in reverse order.
    """
    pass

def make_list(a,b,c):
    """
    Returns a list containing all three parameters
    """
    pass

def nth_list(sequence, n):
    """
    Return a list that has every nth value from the sequence
    """
    pass

def splice(a,b):
    """
    The function should permanently add all of the elements from list b to list a. Do not return a value.
    """
    pass

def odds_before_evens(a_list):
    """
    Rearrange the elements in the list so that all of the odd values come before the even values. Otherwise, the values should remain in the same relative order.Do not return a value - modify the list inplace
    """
    pass

def bisect(a_list):
    """
    Returns the list bisected into two halves. If the list has an odd number of elements, do not include the middle element in either half.
    """
    pass

def equivalent(a, b):
    """
    Return True if the sequences contain all of the same values, even if they are in a different order, and False otherwise
    """
    pass

class Domino:
    """
    Create a Python class to represent a domino. Be sure to include slots and a constructor. 
    """
    __slots__ = ["__a","__b"]
    def __init__(self,a,b):
        """
        It's a constructor my man [a|b]
        """
        self.__a = a
        self.__b = b
        
    def __str__(self):
        return "[%d|%d]"%(self.__a,self.__b)
        

def domino_to_string(domino):
    """
    Turns a domino into a string
    """
    return str(domino)

def is_match(dom1,dom2):
    """
    Return True if the dominos have the same number of pips at either end, and False otherwise.
    """
    pass

def list_range(m,n):
    """
    Uses list comprehension to return the list containing all of the values from m to n-1
    """
    pass

def multiples(sequence, n):
    """
    Use list comprehension to create a list that has all of the values from the sequence that are evenly divisible by n
    """
    pass

def only_vowels(a_string):
    """
    Use list comprehension to return a list containing only the vowels in the string. Your function should run in O(n) where n is the length of the string.
    """
    pass

def random_count(n):
    """
    Return the number of times the random.randint function must be called before all of the values from 0 to n are generated randomly
    """
    pass

def disjoint(a,b):
    """
    Returns True if the sets are disjoint and False otherwise
    """
    pass

def random_counts(n):
    """
    Returns a dictionary that counts how many times each unique value is generated by random.randint before all of the values from 0 to n are generated at least once.
    """
    pass

def frequencies(counts):
    """
    Print each count andits frequency in sorted order.
    """
    pass

def format_string(string):
    """
    Formats the print of an activity
    """
    print("\t%s"%(str(string)))

def main():
    # Call your make_tuple function at least twice with different arguments and print the tuples that are returned.
    print("Activity 1:")
    format_string(make_tuple(1,3,2))
    format_string(make_tuple(4,3,5))
    print()

    # Call reverse_tuple from main with at least two different kinds of sequences and print the tuple that is returned
    print("Activity 2:")
    format_string(reverse_tuple([1,2,3,4,5]))
    format_string(reverse_tuple((1,2,4,5,8,2)))
    print()
    # Call your make_list function from main at least twice with different arguments and print the lists that are returned
    print("Activity 3:")
    format_string(make_list(3,6,2))
    format_string(make_list('3',6,2.0))
    print()
    # Call your function from main with at least two different sequences and print the lists that are returned
    print("Activity 4:")
    format_string(nth_list([0,1,2,3,4,5,6,7,8,9],3))
    format_string(nth_list([1,2,3,4,5,6,7,8,9,0],3))
    print()
    
    # Print list a before and after the splice function is called
    print("Activity 5:")
    a = [1,2,3]
    b = ["a","b","c"]
    format_string(a)
    splice(a,b)
    format_string(a)
    print()
    
    # Call your odds_before_evens function and print before and after
    print("Activity 6:")
    a_list = [1,2,3,4,5,6,7]
    format_string(a_list)
    odds_before_evens(a_list)
    format_string(a_list)
    print()

    # Call the bisect function and print the results
    print("Activity 7:")
    format_string(bisect([1,2,3,4,5,6]))
    format_string(bisect([1,2,3,4,5,6,7]))
    print()

    # Call equivalent and print the results
    print("Activity 8:")
    a = "hello"
    b = "elloh"
    format_string(equivalent(a,b))
    a = "hllo"
    b = "elloh"
    format_string(equivalent(a,b))
    print()

    # Call domino_to_string on two different dominos
    print("Activity 9:")
    d1 = Domino(1,5)
    d2 = Domino(3,6)
    d3 = Domino(1,5)
    format_string(domino_to_string(d1))
    format_string(domino_to_string(d2))
    print()
    
    # Call is match on a few dominos
    print("Activity 10:")
    format_string(is_match(d1,d2))
    format_string(is_match(d1,d3))
    print()

    # Call list_range and print
    print("Activity 11:")
    format_string(list_range(0,13))
    print()

    # Call multiples on a sequence
    print("Activity 13:")
    format_string(multiples([1,2,3,4,5,6,7,8,9],3))
    print()

    # Call only_vowels 
    print("Activity 14:")
    format_string(only_vowels("oiuhjkjsdkfo"))
    print()

    # Call random_count
    print("Activity 15:")
    format_string(random_count(5))
    print()

    # Call disjoint
    print("Activity 16:")
    format_string(disjoint({1,2,3},{3,2,1}))
    format_string(disjoint({1,2,3},{4,5,6}))
    print()

    # Use the dictionary in your main function to determine the total number of times random.randint was called, the maximum number of times that any value was generated, and the sorted list of values that were generated the maximum number of times. 
    print("Activity 17:")
    print()

    pass

if __name__ == "__main__":
    main()