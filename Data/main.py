from __future__ import print_function
import sys
import datetime
from calendar import monthrange

from Operations.add import add
from Operations.modify import modify
from Operations.read import read_data
from Operations.remove import remove_expenses_in_day, remove_expenses_between_days, remove_expenses_of_type
from Operations.reports import print_expense_sum_for_type, print_greatest_spent_sum, print_expanses_equal_sum, \
    print_sorted_expenses_by_type
from Operations.search import print_expanses_greater_than_sum, print_before_day_less_than_sum, print_expenses_of_type


__author__ = 'Damaris'


class const():
    sum_index = 1
    date_index = 0
    type_index = 2

now = datetime.datetime.now

def display_menu(option):
    if option == 'a':
        print("1. Adauga o noua cheltuiala\n2. Actualizeaza o cheltuiala(se specifica ziua, suma, tipul)\n")
    elif option == 's':
        print("1. Sterge toate cheltuielile pentru ziua data\n" +
              "2. Sterge toate cheltuielile pentru un interval de timp(se da ziua de inceput si sfarsit\n" +
              "3. Sterge toate cheltuielile de un anumit tip\n")
    elif option == 'c':
        print("1. Tipareste toate cheltuielile mai mari decat o suma data\n" +
              "2. Tipareste toate cheltuielile efectuate inainte de o zi si mai mi decat o suma data)\n" +
              "3. Tipareste toate cheltuielile de un anumit tip\n")
    elif option == 'r':
        print("1. Tipareste suma totala pentru un anumit tip de cheltuiala\n" +
              "2. Gaseste ziua in care suma cheltuita este maxima\n" +
              "3. Tipareste toate cheltuielile ce au o anumita suma\n" +
              "4. Tipareste cheltuielile sortate dupa tip\n")
    elif option == 'f':
        print("1. Elimina toate cheltuielile de un anumit tip\n" +
              "2. Elimina toate cheltuielile mai mici decat o suma data\n")
    elif option == 'u':
        print("1. Se reface ultima operatie\n")
    elif option == 'x':
        print("La revedere")


def main():
    lista = []
    current_month = now.month
    current_year = now.year
    days = monthrange(current_year,current_month)
    print(days)
    should_run = True
    dict_menu = {'a': add_menu,
                 's': erase_menu,
                 'c': search_menu,
                 'r': reports_menu,
                 'f': filter_menu,
                 'u': undo_menu,
                 'x': exit_menu}
    while should_run:
        try:
            print("a.Adaugare\n"
                  "s.Stergere\n"
                  "c.Cautare\n"
                  "r.Rapoarte\n"
                  "f.Filtrare\n"
                  "u.Undo\n"
                  "x.Exit")
            print(lista)
            option = (input("Introduceti optiunea dumneavoastra: "))
            if option in dict_menu:
                display_menu(option)
                operation = int(input("Ce doriti sa faceti?"))
                should_run = dict_menu[option](operation, lista)
            else:
                raise KeyError("Optiune invalida")
        except Exception as e:
            print("ERROR: {}\n".format(e), file=sys.stderr)


def raise_key_error(operation):
    raise KeyError("Operatiunea {} este invalida!".format(operation))


def add_menu(operation, lista):
    if operation == 1:
        day_of_month, spent_sum, expense_type = read_data()
        lista = add(lista, day_of_month, spent_sum, expense_type)
    elif operation == 2:
        day_of_month, spent_sum, expense_type = read_data()
        lista = modify(lista, day_of_month, spent_sum, expense_type)
    else:
        raise_key_error(operation)
    return True


def erase_menu(operation, lista):
    if operation == 1:
        day = int(input("Ziua: "))
        remove_expenses_in_day(lista, day)
    elif operation == 2:
        first_day = int(input("Ziua de inceput: "))
        last_day = int(input("Ziua de sfarsit: "))
        remove_expenses_between_days(lista, first_day, last_day)
    elif operation == 3:
        expense_type = input("Tipul: ")
        remove_expenses_of_type(lista, expense_type)
    else:
        raise_key_error(operation)
    return True


def search_menu(operation, lista):
    if operation == 1:
        suma = int(input("Suma: "))
        print_expanses_greater_than_sum(lista, suma)
    elif operation == 2:
        # pb cu asta
        # pb cu asta
        # pb cu asta
        # pb cu asta# pb cu asta
        # pb cu asta

        suma = int(input("Suma:"))
        day = int(input("Ziua:"))
        print_before_day_less_than_sum(lista, suma, day)
    elif operation == 3:
        expense_type = input("Tipul: ")
        print_expenses_of_type(lista, expense_type)
    else:
        raise_key_error(operation)
    return True


def reports_menu(operation, lista):
    if operation == 1:
        spent_type = input("Tipul:")
        print_expense_sum_for_type(lista, spent_type)
    elif operation == 2:
        print_greatest_spent_sum(lista)
    elif operation == 3:
        spent_sum = int(input("Suma"))
        print_expanses_equal_sum(lista, spent_sum)
    elif operation == 4:
        print_sorted_expenses_by_type(lista)
    else:
        raise_key_error(operation)
    return True


def filter_menu(operation, lista):
    pass


def undo_menu(operation, lista):
    pass


def exit_menu(operation, lista):
    return False


if __name__ == "__main__":
    main()