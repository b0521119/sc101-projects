"""
File: anagram.py
Name: Jennifer Chueh
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global variable
dic_lst = []


def main():
    """
    This program recursively finds all the anagram(s) for the word.
    """
    start = time.time()
    read_dictionary()
    print('Welcome to stanCode "Anagram  Generator" (or -1 to quit)')
    while True:
        word = input('Find anagram for: ')
        if word == EXIT:
            break
        else:
            find_anagrams(word)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            w = line.strip()
            dic_lst.append(w)


def find_anagrams(s):
    """
    :param s: str, the word that user type in
    :return: str, all possible anagram(s)
    """
    num_ana = find_anagrams_helper(s, '', list(s), len(s), [])
    print(str(len(num_ana))+' anagrams ' + str(num_ana))


def find_anagrams_helper(s, current_s, unused_s, len_ans, ans_lst):
    # Base case
    if len(current_s) == len_ans and current_s in dic_lst:
        if current_s not in ans_lst:
            print('Searching...')
            ans_lst.append(current_s)
            print(f"Found:  {current_s}")
    else:
        for w in s:
            if w in unused_s:
                # Choose
                unused_s.remove(w)
                current_s += w
                if has_prefix(current_s):
                    # Explore
                    find_anagrams_helper(s, current_s, unused_s, len_ans, ans_lst)
                # Un-choose
                unused_s.append(current_s[-1])
                current_s = current_s[0:-1]
    return ans_lst


def has_prefix(sub_s):
    """
    Find the word that is start with sub_s
    :param sub_s: str, the sub_s that find_anagrams_helper arranged
    :return: bool, True if find the sub_s in dictionary
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
