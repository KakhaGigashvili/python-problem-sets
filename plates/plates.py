def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    for i in range(len(s)):
        if s[i].isdigit():
             
            if s[i] == "0":
                return False

            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return False

            break

    return True

main()