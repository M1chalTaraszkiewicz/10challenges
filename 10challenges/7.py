# Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or .
# The third parameter will also be an integer.
# The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.

def Zad7 (firstInt,operator,secondInt):
    if type(firstInt) == int and type(secondInt) == int and operator in "+-/.":
        if operator == "+":
            return firstInt + secondInt
        elif operator == "-":
            return firstInt - secondInt
        elif operator == "/":
            return firstInt / secondInt
        elif operator == ".":
            return firstInt * secondInt
    else:
        return "Złe parametry"
print(Zad7(6,"-",4))

