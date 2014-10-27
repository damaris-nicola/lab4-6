from enum import Enum

__author__ = 'Damaris'


expenses = ['food', 'clothes', 'phone', 'rent', 'others']


def read_data():
    run = True
    while run:
        day_of_month = int(input("Ziua: "))
        spent_sum = int(input("Suma: "))
        expense_type = input("Pentru: ")
        if day_of_month not in range(1,32):
            raise Exception("Zi incorecta")
        if spent_sum<0:
            raise Exception("Suma invalida")
        if expense_type not in expenses:
            raise Exception("Tip invalid")
        run = False
    return day_of_month, spent_sum, expense_type
