fruit = input("Fruit: ").lower()

fruits = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    "kiwifruit": 90,
    "pear": 100
}


if fruit in fruits:
    print("Calories:", fruits[fruit])