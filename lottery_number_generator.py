import random

# using list comprehension ...

"""def main():
    lottery_number = [random.randint(0, 9) for i in range(7)]
    for number in lottery_number:
        print(number)

main()"""

# here is another solution ...

def main():
    lottery_number = []
    for i in range(7):
        lottery_number.append(random.randint(0, 9))
    for number in lottery_number:
        print(number)

main()