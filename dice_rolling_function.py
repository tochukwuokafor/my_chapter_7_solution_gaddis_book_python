import random

def roll(number_of_throws):
    roll_result = [random.randint(1, 6) for i in range(number_of_throws)]
    roll_result.sort()
    print(roll_result)

def main():
    number_of_throws = int(input('Enter a positive integer: '))
    roll(number_of_throws)

main()