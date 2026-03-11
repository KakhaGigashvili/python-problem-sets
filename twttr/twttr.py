text = input("Input: ")

vowels = "aeiouAEIOU"

finalText = ""

for letter in text:
    if letter in vowels:
        finalText += ""
    else:
        finalText += letter

print(finalText)