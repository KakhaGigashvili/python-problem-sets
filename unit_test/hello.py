def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="word"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()