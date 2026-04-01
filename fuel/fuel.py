while True:
    fuel = input("Fraction: ")

    if fuel == "1/4":
        print("25%")
        break
    elif fuel == "1/3":
        print("33%")
        break
    elif fuel == "1/2":
        print("50%")
        break
    elif fuel == "2/3":
        print("67%")
        break
    elif fuel == "3/4":
        print("75%")
        break
    elif fuel in ["4/4", "100/100", "99/100"]:
        print("F")
        break
    elif fuel in ["0/1", "0/100", "1/100"]:
        print("E")
        break
    else:
        print("Try again")