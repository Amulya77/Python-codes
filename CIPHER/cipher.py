'''Cipher with the ascii values'''



while True:
    nc = input("Type 'encode' to encrypt, 'decode' to decrypt: ")

    if nc == "encode":
        msg = input("Type your Message: ")
        n = int(input("Type the shift number: "))
        msg2 = ""
        for i in msg:
            k = ord(i) + n
            if k > 122:
                i = chr(ord('a') + k - 122)
            elif k > 90 and k < 97:
                i = chr(k - 25)
            else:
                i = chr(ord(i) + n)
            msg2 += i
        print("Encoded Message:", msg2)

    elif nc == "decode":
        msg = input("Type your Cipher Text: ")
        n = int(input("Type the shift number: "))
        msg2 = ""
        for i in msg:
            k = ord(i) - n
            if k < 97:
                i = chr(ord('z') - (96 - k))
            elif k < 65:
                i = chr(90 - (64 - k))
            else:
                i = chr(ord(i) - n)
            msg2 += i
        print("Decoded Message:", msg2)

    repeat = input("Type 'yes' to repeat, 'no' to exit: ")
    if repeat.lower() == "no":
        break




# alpha+
# msg=input("Type your Message: ")
# n=int(input("Type the shift number: "))
# msg2=""