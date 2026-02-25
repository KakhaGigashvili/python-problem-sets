massage = input("Greeting: ").lower().strip()

if massage.startswith("hello"):
    print("$0")
elif massage.startswith("how you doing?"):
    print("$20")
elif massage.startswith("what's happening?") or massage.startswith("what's up"):
    print("$100")