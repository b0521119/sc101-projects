"""
File: similarity.py
Name: Jennifer Chueh
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program is to find the sub DNA which the short sequence DNA
    match the long sequence DNA the most.
    """
    long = input("Please give me a DNA sequence to search: ")
    short = input("What DNA sequence would you like to match? ")
    long_upper = long.upper()
    short_upper = short.upper()
    print('The best match is ' + check_dna(long_upper, short_upper))


def check_dna(long_dna, short_dna):
    result_sub = ''
    count_correct = 0
    max_correct = count_correct
    for i in range(len(long_dna)-len(short_dna)+1):
        dna_sub = long_dna[i:i+len(short_dna)]  # How many times should they check
        count_correct = 0
        for s in range(len(dna_sub)):
            if dna_sub[s] == short_dna[s]:
                count_correct += 1
            if count_correct > max_correct:
                max_correct = count_correct
                result_sub = dna_sub
    return result_sub







###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
