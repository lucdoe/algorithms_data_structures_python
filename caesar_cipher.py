

# Caesar Cipher


MAX_KEY_SIZE = 26


def getMode():

    while True:

        mode = input(' Do you wish to encrypt, decrypt or bash a message? ').lower()

        if mode in ['encrypt', 'e', 'decrypt', 'd', 'brute', 'b']:

            return mode

        else:

            print(' Enter either "encrypt", "e", "decrypt", "d" or "brute", "b"')


def getMessage():

    message = input(' Enter your message: ')

    return message


def getKey():

    key = 0

    checker = True

    while checker:

        key = int(input(' Enter the key number (1-%s): ' % (MAX_KEY_SIZE)))

        if (key >= 1 and key <= MAX_KEY_SIZE):
            checker = False
            return key


def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd': 

        key = -key

    translated = ' '

    for symbol in message:

        if symbol.isalpha():
            
            num = ord(symbol) # return an integer representing the Unicode code point of the symbol
            num += key  # num = num + key

            if symbol.isupper():

                if num > ord('Z'): # Check if num has a value larger than 90 (ord('Z'))
                    num = num - 26 # num -= 26, to keep valid chars

                elif num < ord('A'):
                    num += 26

            elif symbol.islower():

                if num > ord('z'):
                    num -= 26

                elif num < ord('a'):
                    num += 26

            translated += chr(num)

        else:

            translated += symbol

    return translated


mode = getMode()

message = getMessage()


if mode[0] != 'b':
    key = getKey()


if mode[0] != 'b':
    print(' Your translated text is:')
    print(getTranslatedMessage(mode, message, key))

else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
