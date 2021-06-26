"""
File: caesar.py
Name: Jennifer Chueh
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program is to decipher the alphabets.
    """
    secret_num = int(input("Secret number: "))
    string = input("What's the cipher string? ")
    string_upper = string.upper()
    print('The deciphered string is: ' + decipher(secret_num, string_upper))


def decipher(num, string):
    ans = ''
    for i in range(len(string)):
        ch = string[i]
        ch_place = ALPHABET.find(ch)
        if ch_place != -1:
            ch_decipher = ch_place + num
            if ch_decipher > 25:
                ch_decipher = ch_decipher - 26  # Decipher the index number of the ALPHABET
            ans = ans + ALPHABET[ch_decipher:ch_decipher + 1]
        else:                                   # The string which cannot find in ALPHABET
            ans = ans + ch
    return ans












#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
