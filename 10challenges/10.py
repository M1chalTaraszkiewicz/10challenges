# Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled.
# If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

def Zad10(string):
    if type(string) == str:
        newstring = ""
        for x in string:
            newstring = newstring + x + x
        return newstring
    else:
        return "Zły parametr"

print(Zad10("ak-47"))