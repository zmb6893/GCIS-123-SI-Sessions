import arrays as a
import array_utils as au

"""
Visualization of Quicksort
@author: Zoe Bingham
"""

def partition(pivot, array):
    """
    Breaks an array down into 3 partitions
    """
    less_count = 0
    more_count = 0
    same_count = 0

    for i in range(len(array)):
        if array[i] < pivot:
            less_count += 1
        elif array[i] > pivot:
            more_count += 1
        else:
            same_count += 1

    less = a.Array(less_count)
    same = a.Array(same_count)
    more = a.Array(more_count)

    less_index = 0
    more_index = 0
    same_index = 0

    for i in range(len(array)):
        if array[i] < pivot:
            less[less_index] = array[i]
            less_index += 1
        elif array[i] > pivot:
            more[more_index] = array[i]
            more_index += 1
        else:
            same[same_index] = array[i]
            same_index += 1

    return less, same, more

def quick_sort(array, iteration=0, iteration2=0):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less, same, more = partition(pivot, array)
        sorted_less = quick_sort(less, iteration+1, iteration2)
        print("i1=%d\ti2=%d\tsame: %s" %(iteration, iteration2, str(same)))
        print("i1=%d\ti2=%d\tsorted_less: %s" %(iteration, iteration2, str(sorted_less)))
        sorted_more = quick_sort(more, iteration, iteration2+1)
        print("i1=%d\ti2=%d\tsorted_more: %s" %(iteration, iteration2, str(sorted_more)))

        final_array = a.Array(len(less)+len(same)+len(more))

    return au.array_cat(au.array_cat(sorted_less, same), sorted_more)

def quick_sort_mid(array, iteration=0, iteration2=0):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array)//2]
        less, same, more = partition(pivot, array)
        sorted_less = quick_sort_mid(less, iteration+1, iteration2)
        print("i1=%d\ti2=%d\tsame: %s" %(iteration, iteration2, str(same)))
        print("i1=%d\ti2=%d\tsorted_less: %s" %(iteration, iteration2, str(sorted_less)))
        sorted_more = quick_sort_mid(more, iteration, iteration2+1)
        print("i1=%d\ti2=%d\tsorted_more: %s" %(iteration, iteration2, str(sorted_more)))

        final_array = a.Array(len(less)+len(same)+len(more))

    return au.array_cat(au.array_cat(sorted_less, same), sorted_more)

def main():
    array = au.range_array(10,0,-1)
    array2 = au.random_array(10,0,10)
    print("Quick sort start:")
    print(array)
    print(quick_sort(array))
    print("\n\n\nQuick sort mid:")
    print(array2)
    print(quick_sort_mid(array2))

    # can call with other arrays

main()