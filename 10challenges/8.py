# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer.
# The second should be the discount percentage as an integer. The function should return the price of the item after the discount has been applied.
# For example, if the price is 100 and the discount is 20, the function should return 80.

def Zad8 (price, discount):
    if type(price) == int and type(discount) == int:
        discount = discount/100
        return price - price * discount
    else:
        return "Złe parametry"

print(Zad8(137,15))