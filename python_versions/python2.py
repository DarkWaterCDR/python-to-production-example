# Python 2, lots of syntax/functions
#       incompatible with Python 3.*

name = "Peter"

if name == "Peter":
    print("This is an English name.")
elif name == "Pedro":
    print("This is a Hispanic name.")
elif name == "Netp":
    print("This is a Russian name.")
else:
    print("Unknown origin")

def add_numbers(a: float, b: float) -> int:
    return a + b

result = add_numbers(a=1, b=2)

def do_some_math():
    sum = 1 + 2 + 3

do_some_math()

def calc_difference(a, b):
    return a - b