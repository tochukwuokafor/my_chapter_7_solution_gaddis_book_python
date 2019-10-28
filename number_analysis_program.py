def main():
    series_list = []
    print('You will enter a series of 20 numbers')
    print('-------------------------------------')
    for idx in range(20):
        print('Enter number #', idx + 1, ': ', sep = '', end = '')
        number = float(input())
        series_list.append(number)
    lowest = min(series_list)
    highest = max(series_list)
    total = sum(series_list)
    average = total / len(series_list)
    print('The lowest number in the list is', lowest)
    print('The highest number in the list is', highest)
    print('The total of the numbers in the list is', total)
    print('The average of the numbers in the list is', average)

main()