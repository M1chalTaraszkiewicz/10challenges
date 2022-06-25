# Write a function in Python that accepts a decimal number and returns the equivalent binary number.
# To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.

def Zad3 (decnum):
    if type(decnum) == int:
        binnum = ''
        while decnum != 0:
            if decnum % 2 == 0:
                binnum = binnum + '0'
                decnum = decnum / 2
            else:
                binnum = binnum + "1"
                decnum = (decnum - 1) / 2
        return binnum[::-1]
    else:
        return "Zły parametr"

print(Zad3(492))