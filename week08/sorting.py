"""
SOLUTION: Session 8B: Sorting activities. Visualize the sory
@author: Zoe Bingham
"""

import array_utils as au
import arrays as a

def swap(array, a, b):
    """
    Swaps the values at two indexs in an array.
    """
    temp_value = array[a]
    array[a] = array[b]
    array[b] = temp_value
    return array

def shift(array, i):
    # If the value at the index is less, swap the two values and decrement index.
    # Continue until the value is no longer less than the value to its left

    while (i > 0) and (array[i]<array[i-1]):
        
        print("index: " +str(i) + " values: " + str(array[i])+"<"+str(array[i-1]))
        swap(array, i, i-1)
        i+=1
        if(i==len(array)):
            break

def insertion_sort(array):
    for i in range(1,len(array)):
        shift(array, 1)
        print("i is %d\n\t array: %s"%(i,str(array)))

def merge_sort(array):
    if(len(array) == 1):
        return array
    else:
        half1, half2 = split(array)
        return merge(merge_sort(half1), merge_sort(half2))

def split(array):
    evens = None
    odds = None

    if(len(array) % 2 != 0):
        evens = a.Array((len(array)//2)+1)
        odds = a.Array(len(array)//2)
    else: 
        evens = a.Array(len(array)//2)
        odds = a.Array(len(array)//2)

    evens_index = 0
    odds_index = 0
    for index in range(len(array)):
        if index % 2 == 0:
            evens[evens_index] = array[index]
            evens_index += 1
        else:
            odds[odds_index] = array[index]
            odds_index += 1 
    return evens, odds

def merge(half1, half2):
    result = a.Array(len(half1) + len(half2))
    i1 = 0
    i2 = 0

    i = 0
    while i1 < len(half1) and i2 < len(half2):  
        
        if half1[i1] <= half2[i2]:
            result[i] = half1[i1]
            #print("half1[%d] <= half2[%d]: result[%d] = half1[%d]"%(i1,i2,i,i1)) 
            i1 += 1
            
        else:
            result[i] = half2[i2]
            #print("half1[%d] > half2[%d]: result[%d] = half2[%d]"%(i1,i2,i,i2)) 
            i2 += 1 
        
        i+=1
    return result

def main():
    array = au.range_array(10,0,-1)
    print(insertion_sort(array))

if __name__ == "__main__":
    main()
