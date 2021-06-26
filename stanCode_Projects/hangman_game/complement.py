"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program is to built the complement of the DNA.
    """
    dna = input("Please give me a DNA strand and I'll fine the complement: ")
    dna_change = dna.upper()
    new_dna = built_complement(dna_change)
    print('The complement of ' + str(dna) + ' is ' + str(new_dna))


def built_complement(dna):
    ans = ""
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
