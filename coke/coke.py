coke = 50

while coke > 0:
    print("Amount Due:", coke)
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        coke -= coin

change = -coke
print("Change Owed:", change)
