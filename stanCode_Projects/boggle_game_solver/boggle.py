"""
File: boggle.py
Name: Jennifer Chueh
----------------------------------------
This program recursively finds all the anagram(s)
for the word input by user in the 4 * 4 alphabets.

For example:
            f y c l
            i o m g
            o r i l
            h j h u
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dic_lst = []


def main():
    start = time.time()

    read_dictionary()
    all_row = ''
    for i in range(4):
        row = input(f'{i + 1} row of letters: ')
        if len(row) != 7:
            print('Illegal input')
            break
        else:
            all_row += row
            all_row += ' '
    all_row = all_row.split()
    boggle(all_row)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(lst):
    """
    :param lst: list, 16 alphabets which user type in
    :return:
    """
    ans_lst = []
    unused_index = list(range(len(lst)))

    for current_y in range(4):
        for current_x in range(4):
            unused_index .remove(current_x + 4 * current_y)
            boggle_helper(lst, current_x, current_y, unused_index, lst[current_x + 4 * current_y], 4, ans_lst)
            unused_index .append(current_x + 4 * current_y)
    print('There are', len(ans_lst), 'words in total.')


def boggle_helper(lst, cur_x, cur_y, unused, cur_str, length, ans):
    if len(cur_str) >= length and cur_str in dic_lst:
        if cur_str not in ans:
            print(f"Found: {cur_str}")
            ans.append(cur_str)
            return True
        return False

    else:
        for y in range(-1, 2, 1):  # -1,0,1
            for x in range(-1, 2, 1):  # -1,0,1
                if cur_x + x < 0 or cur_y + y < 0 or cur_x + x > 3 or cur_y + y > 3 or (x == 0 and y == 0):
                    pass
                else:
                    if cur_x + x + 4 * (cur_y + y) in unused:
                        # Choose
                        cur_str = cur_str + lst[cur_x + x + 4 * (cur_y + y)]
                        unused.remove(cur_x + x + 4 * (cur_y + y))
                        # Explore
                        if has_prefix(cur_str):  # return True 找到頭
                            found_w = boggle_helper(lst, cur_x + x, cur_y + y, unused, cur_str, length, ans)
                            if found_w:  # return True 找到整串字
                                length += 1
                                boggle_helper(lst, cur_x + x, cur_y + y, unused, cur_str, length, ans)
                        # Un-choose
                        unused.append(cur_x + x + 4 * (cur_y + y))
                        cur_str = cur_str[:-1]
                        length = 4


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            w = line.strip()
            dic_lst.append(w)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
