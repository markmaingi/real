import random


# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


# Main program starts here

# search for ASCII on if you will not understand the following code

uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
number1 = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
symbol1 = chr(random.randint(33, 47))
symbol2 = chr(random.randint(33, 47))

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + number1 + number2 + symbol1 + symbol2
password = shuffle(password)

# Ouput
print(password)
