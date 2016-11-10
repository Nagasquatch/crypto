msg = 'PBQRPENSG YNO EBPXF!'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = raw_input('What is a word that might be in the encrypted code(capitalize it)?')

for key in range(len(ALPHABET)):
    result  =  ''

    for symbol in msg:
        if symbol in ALPHABET:
            num = ALPHABET.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(ALPHABET)

            result = result + ALPHABET[num]

        else:
            result = result  + symbol

    if word in result:
        print(result)
