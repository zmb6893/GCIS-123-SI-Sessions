"""
Useful array functions
@author: Zoe Bingham
"""

import arrays as a

def range_array(start, end, step=1):
    """
    Returns an array with values from start to end
    """
    size = 0
    s=0
    b=0
    if step < 0:
        size = start-end+1
        s = start
        e = end-1
    else:
        size = (end+1)-start
        s = start
        e = end + 1
        

    array = a.Array(size)
    index = 0
    for value in range(s,e,step):
        array[index] = value
        index+=1
    return array

def main():
    print(range_array(0,10))
    print(range_array(10,0,-1))

if __name__ == "__main__":
    main()