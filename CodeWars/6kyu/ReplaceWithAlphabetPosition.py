# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )


def alphabet_position(text):
    result = []
    for char in text:
        # print(char)
        if char.isalpha():
            # print(char)
            # Convert the character to its position in the alphabet
            position = ord(char.lower()) - ord('a') + 1
            print(str(position))
            result.append(str(position))

    return ' '.join(result)
    

alphabet_position("The sunset sets at twelve o' clock.")
print(alphabet_position("The sunset sets at twelve o' clock."))