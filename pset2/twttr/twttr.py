def main():
    user_input = input("Input: ")
    print(del_vowels(user_input))


def del_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = ""
    for character in string:
        if character.lower() not in vowels:
            no_vowels += character
    return no_vowels

main()