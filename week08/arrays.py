"""
A fixed-length data structure; created to contain a specific number of elements
that does not change. Analogous to a native array in most languages.
@author GCCIS Faculty
"""

class Array:
    def __init__(self, length, prototype=None):
        """
        Creates a new array of the specified size. The new array is filled
        with the prototype value.
        """
        self.__length = length
        self.__data = [prototype] * length
    
    def __len__(self):
        """
        Returns the length of the vector. This value does not change.
        """
        return self.__length

    def __getitem__(self, index):
        """
        Returns the value at the specified index in thevector.
        """
        self.__index_check(index)

        return self.__data[index]

    def __setitem__(self, index, value):
        """
        Sets the value at the specified index.
        """
        self.__index_check(index)

        self.__data[index] = value

    def __index_check(self, index):
        """
        Validates the index; raises and index error if it is not in range.
        """
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of range: " + str(index))

    def __repr__(self):
        """
        Returns a string representation of the vector.
        """
        return self.__data.__repr__()

    def __str__(self):
        """
        Returns a string representation of the vector.
        """
        return self.__data.__str__()

    def __iter__(self):
        """
        Arrays are not iterable.
        """
        raise TypeError("'Array' object is not iterable")