# use the file_line_viewer.txt to practise this piece of code

def main():
    try:
        enter_file_name = input('Please enter the file name: ')
    except IOError:
        print('The filename cannot be found or opened.')
    opened_file = open(enter_file_name, 'r')
    read_into_list = []
    for line in opened_file:
        line = line[:-1]
        read_into_list.append(line)
    print('The file_line_viewer.txt file contains', len(read_into_list), 'lines.')
    try:
        line_to_view = int(input('Enter the line that you will like to view: '))
    except ValueError:
        print('Please enter an integer value.')
    try:
        print('Line #', line_to_view, ' reads as: ', read_into_list[line_to_view - 1], sep = '')
    except IndexError:
        print('The line number is outside the range of the data list.')

main()
