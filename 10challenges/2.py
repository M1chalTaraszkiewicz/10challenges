# Create a function in Python that accepts two parameters. The first will be a list of numbers.
# The second parameter will be a string that can be one of the following values: asc, desc, and none.
# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order,
# and if it's "none," it should return the original list unaltered.

def Zad2 (list, x):
    if x == 'asc':
        list.sort()
        return list
    elif x == 'desc':
        list.sort(reverse=True)
        return list
    elif x == 'none':
        return list
    else:
        return "Zły parametr"

list = [23,5,35,26,6,23,5,67,42,131,5,6]
print(Zad2(list,'asc'))