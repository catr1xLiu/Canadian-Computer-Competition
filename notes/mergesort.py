'''
a quick way to sort items

example: sort items in increasing order
there are n values in the dictionsary values
the list indecies stores the n indicies of these values
sort the indicies in the order of increasing value
'''

def merge(indicies1:list, indicies2:list, values:dict) -> list:
    """
    merge the two indicies list, make them one big indicies list and in increasing order
    
    : param indicies1 : one indicies list, in increasing order of their corresponding values
    : param indicies2 : the other indicies list, in increasing order of their corresponding values
    : param values : the corresponding values of the indicies
    : return : the merged list of indicies, in increasing order
    """
    indicies_sorted = [] # the merged list of indicies, in increasing order
    while (len(indicies1) and len(indicies2)): # repeat until one of the indicies list gets empty
        if values[indicies1[0]] < values[indicies2[0]]: # compare the first, and therefore the smallest values in the two lis; change < to > if you are sorting it in decreasing order
            indicies_sorted.append(indicies1.pop(0))
        else:
            indicies_sorted.append(indicies2.pop(0)) # insert the smaller one into the merged list, remove it from the original list
    # at this point, one of the two lists are empty
    indicies_sorted = indicies_sorted + indicies1 + indicies2 # put the indicies remaining to the end of the merged list as they are all greater than the last value in the merged list
    return indicies_sorted


def mergesort(indicies, values:dict):
    """
    sort the indicies in increasing order of their corresponding values
    : param indicies : the indicies, unsorted
    : param values : the dictionary that stores the corresponding values of the indicies
    : return the sorted indicies, in increasing order of their values in param "values"
    """
    if len(indicies) == 1:
        # if the indicies is only in the length of one, just leave it there
        return indicies
    
    # seperate the list of indicies into two parts in equal length, and sort each of them
    left = mergesort(indicies[0:len(indicies)//2], values)
    right = mergesort(indicies[len(indicies)//2: len(indicies)], values)

    return merge(left, right, values) # merge the two sorted list and get one whole sorted list

values = {
    3 : 0,
    4 : 1,
    2 : 2,
    1 : 3,
    6 : 4,
    0 : 5,
    5 : 6
}
indicies = [0,1,2,3,3,4,5,6]

print(mergesort(indicies, values))