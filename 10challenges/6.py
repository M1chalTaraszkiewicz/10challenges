# Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string.
# It should then return a boolean value of either True or False.
# If the count of Xs and Os are equal, then the function should return True. If the count isn't the same, it should return False.
# If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.

def Zad6 (string):
    if type(string) == str:
        if string.count("X") == string.count("O"):
            return True
        else:
            return False
    else:
        return "Zły parametr"

print(Zad6("SA 4 X I 3 O XXXOO"))
print(Zad6("SA 5 X I 5 O XOXOXOXO"))