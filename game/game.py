import random

def main():   
    n = get_level()
    num = random.randint(1, n)

    while True:
        try:
            guess = int(input("guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue

        if guess == num:
            print("Just right!")
            break
        elif guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            num = int(level)
            if num > 0:
                return num
        except:
           pass

main()