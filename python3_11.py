# Python 2, lots of syntax/functions
#       incompatible with Python 3.*

name: str = "Peter"

match name:
    case "Peter":
        print("This is an English name.")
    case "Pedro":
        print("This is a Hispanic name.")
    case "Netp":
        print("This is a Russian name.")
    case _:
        print("Unknown origin")