# Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings.
# The function should return a list with only the integers in the original list in the same order.

def Zad9(list):
    numlist = []
    for x in list:
        if type(x) == int:
            numlist.append(x)
    return numlist

list = [3,"cos",7,14,"a","10",5]
print(Zad9(list))