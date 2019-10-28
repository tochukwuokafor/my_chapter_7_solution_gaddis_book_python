def main():
    rainfall_list = []
    for month in range(12):
        print('Enter the total rainfall for month #', month + 1, ': ', sep = '', end = '')
        value = float(input())
        rainfall_list.append(value)
    total_rainfall = sum(rainfall_list)
    average_rainfall = total_rainfall / len(rainfall_list)
    year_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    highest = rainfall_list.index(max(rainfall_list)) + 1
    lowest = rainfall_list.index(min(rainfall_list)) + 1
    print(rainfall_list)
    print('The total rainfall for the year is', total_rainfall)
    print('The average monthly rainfall is', average_rainfall)
    print('The month with the highest amount of rainfall is', year_dict[highest])
    print('The month with the lowest amount of rainfall is', year_dict[lowest])

main()