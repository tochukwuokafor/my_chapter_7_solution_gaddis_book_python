def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    valid_numbers = []
    for number in numbers:
        if 0 < number < 100:
            valid_numbers.append(number)
    total = sum(valid_numbers)
    average = total / len(valid_numbers)
    print('The total of the numbers in the valid_numbers list is', total)
    print('The average of the numbers in the valid_numbers list is', average)

main()