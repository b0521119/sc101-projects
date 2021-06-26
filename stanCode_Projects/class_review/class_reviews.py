"""
File: class_reviews.py
Name: Jennifer Chueh
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    This program is to calculate the maximum, minimum, and average among all the inputs
        for each SC001 and SC101 class.
    """
    class_n = input('Which class? ')
    class_name = class_n.upper()

    total_score001 = 0
    count001 = 0
    avg_score001 = 0
    total_score101 = 0
    count101 = 0
    avg_score101 = 0

    if class_name == '-1':
        print('No class scores were entered')
    else:
        high_score001 = 0
        low_score001 = 100
        high_score101 = 0
        low_score101 = 100
        while True:
            if class_name == '-1':
                break
            elif class_name == 'SC001':
                score001 = int(input('Score: '))
                if score001 > high_score001:
                    high_score001 = score001
                if score001 < low_score001:
                    low_score001 = score001
                total_score001 += score001
                count001 += 1
                avg_score001 = float(total_score001/count001)
            elif class_name == 'SC101':
                score101 = int(input('Score: '))
                if score101 > high_score101:
                    high_score101 = score101
                if score101 < low_score101:
                    low_score101 = score101
                total_score101 += score101
                count101 += 1
                avg_score101 = float(total_score101/count101)

            class_n = input('Which class? ')
            class_name = class_n.upper()
        print('=============SC001=============')
        if count001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(high_score001))
            print('Min (001): ' + str(low_score001))
            print('Avg (001): ' + str(avg_score001))
        print('=============SC101=============')
        if count101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(high_score101))
            print('Min (101): ' + str(low_score101))
            print('Avg (101): ' + str(avg_score101))







#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
