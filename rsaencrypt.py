#! /usr/bin/env python3

# This one just does not work int encrypts and then is unable to decrypt the cipher it has generated

import random

def encrypt(plain):

    prime1    = 0
    prime2    = 0
    repeator  = 1
    primelist = [prime1, prime2]

    while (repeator==1):

        prime1 = random.randint(0, 2048)
        prime2 = random.randint(0, 2048)
        count1 = 0
        count2 = 0

        for i in range (1, prime1 + 1):

            modfactor = prime1 % i

            if modfactor == 0:

                count1 = count1 + 1

        for i in range (1, prime2 + 1):

            modfactor = prime2 % i

            if modfactor == 0:

                count2 = count2 + 1

        if count1 == 2 and count2 == 2:

            primelist = [prime1, prime2]
            print     ("prime numbers", end=" ")
            print     (primelist)
            repeator  = 0

        else:

            repeator = 1


    phi_n    = prime1 * prime2
    lambda_n = (prime1 - 1) * (prime2 - 1)

    print ("lambda(n) " + str(lambda_n) + " phi(n) " + str(phi_n))

    exponent  = 0
    repeator1 = 1

    while (repeator1 == 1):

        count    = 0
        exponent = random.randint(1, 256)

        for factor in range (1, phi_n):

            modfactor1 = phi_n % factor
            modfactor2 = exponent % factor

            if modfactor1 == 0 and modfactor2 == 0:

                count = count + 1

        if count == 1:

            print     ("exponent value " + str(exponent))
            repeator1 = 0

        else:

            repeator1 = 1

    # d=(1+(phi_n))/e
    # x is any positive integer
    print(" ")
    repeator2 = 1
    while (repeator2 == 1):
        x = random.randint(0, 50)
        d = (1 + x * (lambda_n)) / exponent
        print("\r D value", d)

        if d.is_integer():
            repeator2 = 0

        else:

            repeator2 = 1

    print ("public key  :({}, {})".format(phi_n, exponent))
    print ("private key :({}, {})".format(phi_n, d))

    print (plain)
    ASCII = [ ord(x) for x in plain ]
    print (ASCII)

    rsa_encrypt_ascii = [ ((ord(x) ** exponent) % phi_n) for x in plain ]
    print             (rsa_encrypt_ascii)
    
    rsa_encrypt = ''.join(chr(i) for i in rsa_encrypt_ascii)
    print       (rsa_encrypt)

    rsa_decrypt   = [ ((ord(x) ** d) % phi_n) for x in rsa_encrypt]
    rsa_decrypted = ''.join(chr(i) for i in rsa_decrypt)

plain_text   = input("plain text to be encrypted >> ")
string_value = str(plain_text)
encrypt      (string_value)