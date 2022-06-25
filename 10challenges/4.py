# Create a function in Python that accepts a single word and returns the number of vowels in that word.
# In this function, only a, e, i, o, and u will be counted as vowels — not y.\

def Zad4(string):
    if type(string) == str:
        count = 0
        for y in string:
            if y in "aeiouAEIOU":
                count = count + 1
        return count
    else:
        return "Zły parametr"

print(Zad4("tescik"))