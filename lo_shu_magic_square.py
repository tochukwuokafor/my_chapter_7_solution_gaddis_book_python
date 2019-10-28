def is_magic_square(two_dimen_list):
    if sum(two_dimen_list[0]) == 15:
        if sum(two_dimen_list[1]) == 15:
            if sum(two_dimen_list[2]) == 15:
                if two_dimen_list[0][0] + two_dimen_list[1][0] + two_dimen_list[2][0] == 15:
                    if two_dimen_list[0][1] + two_dimen_list[1][1] + two_dimen_list[2][1] == 15:
                        if two_dimen_list[0][2] + two_dimen_list[1][2] + two_dimen_list[2][2] == 15:
                            if two_dimen_list[0][0] + two_dimen_list[1][1] + two_dimen_list[2][2] == 15:
                                if two_dimen_list[0][2] + two_dimen_list[1][1] + two_dimen_list[2][0] == 15:
                                    return True
    else:
        return False

def main():
    two_dimen_list = []
    row_one = list(map(int, input().split()))
    two_dimen_list.append(row_one)
    row_two = list(map(int, input().split()))
    two_dimen_list.append(row_two)
    row_three = list(map(int, input().split()))
    two_dimen_list.append(row_three)
    result = is_magic_square(two_dimen_list)
    print('Is the list a Lo Shu Magic Square?', result)

main()