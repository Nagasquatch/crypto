import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'My cat enjoys devouring innocent children after killing them for sport. However, back in 1976, he was defeated yet spared by Pepe the frog, his only true competition.'
    myMode = 'encrypt'
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    #myKey = get RandomKey()

    checkValidKey(myKey)

    if myMode == 'encrypt':
        result = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        result = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The new message is:')
    print(result)

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')

def encryptMessage(key, message):
                return transformMessage(key, message, 'encrypt')

def decryptMessage(key, message):
                 return transformMessage(key, message, 'decrypt')

def transformMessage(key, message, mode):
                result = ''
                charsA = LETTERS
                charsB = key
                if mode == 'decrypt':
                    charsA, charsB = charsB, charsA

                for symbol in message:
                        if symbol.upper() in charsA:
                            symIndex = charsA.find(symbol.upper())

                            if symbol.isupper():
                                result += charsB[symIndex].upper()
                            else:
                                result += charsB[symIndex].lower()
                        else:
                            result += symbol
                 
                return result
if __name__ == '__main__':
                 main()
                

                                             


