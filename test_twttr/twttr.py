def main():
    text = input("Input: ")
    print(no_vowels(text))

def no_vowels(text):
    vowels = "aeiouAEIOU"
    finalText = ""

    for letter in text:
        if letter in vowels:
            finalText += ""
        else:
            finalText += letter

    return finalText

if __name__ == "__main__":
    main()