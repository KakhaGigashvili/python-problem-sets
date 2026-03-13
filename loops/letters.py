def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(resiver, sender):
    return f"""
    +-----------------------------------------+
    Dear {resiver}

    you are cordialy invited to a ball at 
    peach`s Castle this evening, 7:00 PM.

    Sincerely
    {sender}
    +-----------------------------------------+
        """

main()