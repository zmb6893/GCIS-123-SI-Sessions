"""
EXAMPLE: Raising and handling exceptions.
@author: Zoe Bingham
"""

def function(x):
    """
    What is this going to do?
    """
    if (x > 10):
        raise IndexError("Index out of bounds")

def main():
    """
    What is this going to do?    
    """
    try:
        function(11)
    except FileNotFoundError:
        print("there was a file not found error here!")
    except IndexError:
        print("there is an indexerror here")
    except:
        print("there is another type of error")

main()