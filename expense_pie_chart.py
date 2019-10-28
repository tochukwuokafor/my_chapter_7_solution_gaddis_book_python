# use the expense_pie_chart.txt file to practise this piece of code
import matplotlib.pyplot as plt

def create_text_file():
    expense_file = open('expense_pie_chart.txt', 'w', encoding = 'utf-8')
    rent = 'Rent' + '\n'
    expense_file.write(rent)
    rent_money = input('Enter your rent expense: ') + '\n'
    expense_file.write(rent_money)
    gas = 'Gas' + '\n'
    expense_file.write(gas)
    gas_money = input('Enter your gas expense: ') + '\n'
    expense_file.write(gas_money)
    food = 'Food' + '\n'
    expense_file.write(food)
    food_money = input('Enter your food expense: ') + '\n'
    expense_file.write(food_money)
    clothing = 'Clothing' + '\n'
    expense_file.write(clothing)
    clothing_money = input('Enter your clothing expense: ') + '\n'
    expense_file.write(clothing_money)
    car_payment = 'Car payment' + '\n'
    expense_file.write(car_payment)
    car_payment_money = input('Enter your car payment expense: ') + '\n'
    expense_file.write(car_payment_money)
    misc = 'Misc' + '\n'
    expense_file.write(misc)
    misc_money = input('Enter your misc expense: ') + '\n'
    expense_file.write(misc_money)
    expense_file.close()
    print('The file has been created and the expenses have been written to the file')

def read_from_file():
    open_expense_file = open('expense_pie_chart.txt', 'r', encoding = 'utf-8')
    my_expense_list = []
    my_expense_label = []
    expense_title = open_expense_file.readline()
    while expense_title != '':
        expense_title = expense_title[:-1]
        my_expense_label.append(expense_title)
        expense_amount = open_expense_file.readline()
        expense_amount = int(expense_amount[:-1])
        my_expense_list.append(expense_amount)
        expense_title = open_expense_file.readline()
    return my_expense_list, my_expense_label

def main():
    create_text_file()
    expense_list, expense_label = read_from_file()
    plt.pie(expense_list, labels = expense_label)
    plt.title('Expense pie chart')
    plt.legend()
    plt.show()

main()
