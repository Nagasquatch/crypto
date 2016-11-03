#msg = 'Codecraft Lab rocks!'
print ('This is one of those pointless tests that determine some super spiritual')
print ('code that means nothing to anyone!')

msg = raw_input('What is your full name?')

#key = -52

key = int(raw_input('What is your favorite number'))

#mode = 'encrypt'

mode = raw_input('Do you want me to encrypt it? (answer encrypt or decrypt)')

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''

# capitalize the string in msg
msg = msg.upper()

# run the encryption/decryption code on each symbol in the msg string
for symbol in msg:
    if symbol in ALPHABET:
        # get the encrypted (or decrypted) number for this symbol
        num = ALPHABET.find(symbol) # get the number of the symbol 
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
# handle the wrap-around if num is larger than the lengh of ALPHABET or less
# than 0            
        if num >= len(ALPHABET):
            num = num - len(ALPHABET)
        elif num < 0:
            num = num + len(ALPHABET)

        #add encrypted/decrypted number's symbol at the end of result
    
        result = result + ALPHABET[num]

    else:
        # just add the symbol without encrypting/decrypting
        result = result + symbol

#print the encrypted/decrypted string to the string
print(result)
