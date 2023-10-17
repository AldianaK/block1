"""
Author: Aldiana Kucevic
date: 11-10-23
function: sowp opdrachten
"""

import random


# opdracht 1 oefenen met lists en tuples (h7)

### Lottery Number Generator ###
def lottery_numbers():
    """
    displays 7 lottery numbers
    :return:
    """
    lottery_num = []

    for num in range(1, 8):
        num += random.randint(1, 100)
        lottery_num.append(num)

    print("These are your lottery numbers: ")

    # for number in lottery_num:
        # print(number) # om te testen of die random nummers print

    return lottery_num


### Number Analysis Program ###
def number_analysis():
    """
    analyse given numbers
    :return:
    """
    number_list = []

    for num in range(20):
        num = int(input("Enter a number: "))
        number_list.append(num)
    print(number_list)

    # highest, lowest, total sum, average

    print("The smallest number:", min(number_list))
    print("The largest number:", max(number_list))
    print("the total sum:", sum(number_list))
    print("average:", sum(number_list)/ len(number_list))





# opdracht 2 oefenen met files (h6)

### file head display ###

def file_head_display():
    """
    make a file and should display the first five lines of a file
    :return: file
    """
    try:
        # first make the file
        with open("file.txt", "w") as file:
            file.write("Hello this is my file\n")
            file.write("I need at least 5 lines\n")
            file.write("Everyone is sleeping\n")
            file.write("I'm the best daughter my parents have\n")
            file.write("Aldiana out ;)\n")

        with open("file.txt", "r") as file:
            lines = file.readlines()
            for line in lines[:5]:
                print(line)

        file.close()


    except IOError:
        print("file cannot be worked with")
    except:
        print("unknown error")

    return line



if __name__ == "__main__":
    print(lottery_numbers())
    print("-" * 80)
    print(number_analysis())
    print("-"*80)
    print(file_head_display())

