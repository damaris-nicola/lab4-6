__author__ = 'Damaris'

expenses = ['food', 'clothes', 'phone', 'rent', 'others']


class const():
    sum_index = 1
    date_index = 0
    type_index = 2


def find_expenses_in_day(lista, day_of_month):
    if day_of_month in range(1, 32):
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if day_of_month == cheltuiala[const.date_index]:
                cheltuieli_gasite.append(cheltuiala)
    else:
        raise KeyError("Ziua introdusa nu este valida")
    return cheltuieli_gasite


def remove_expenses_in_day(lista, day_of_month):
    """
    Remove expenses from specified day
    :param lista: list
    :param day_of_month: int
    :return:none
    """
    cheltuieli_gasite = find_expenses_in_day(lista, day_of_month)
    for chelt in cheltuieli_gasite:
        lista.remove(chelt)


def find_expenses_between_days(lista, first_day, last_day):
    if (first_day in range(1, 32)) & (last_day in range(1, 32)):
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if first_day < cheltuiala[const.date_index] < last_day:
                cheltuieli_gasite.append(cheltuiala)
    else:
        raise KeyError("Ziua introdusa nu este valida")
    return cheltuieli_gasite


def remove_expenses_between_days(lista, first_day, last_day):
    """
    Remove expenses between specified days
    :param lista: list
    :param first_day: int
    :param last_day: int
    :return:none
    """
    cheltuieli_gasite = find_expenses_between_days(lista, first_day, last_day)
    for chelt in cheltuieli_gasite:
        lista.remove(chelt)


def find_expenses_of_type(lista, expense_type):
    if expense_type in expenses:
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if cheltuiala[const.date_index] == expense_type:
                cheltuieli_gasite.append(cheltuiala)
    else:
        raise KeyError("Tipul introdus nu este valid")
    return cheltuieli_gasite


def remove_expenses_of_type(lista, expense_type):
    """
    Remove expenses of specified type
    :param lista: list
    :param expense_type: string
    :return:none
    """
    cheltuieli_gasite = find_expenses_of_type(lista, expense_type)
    for chelt in cheltuieli_gasite:
        lista.remove(chelt)


def test_find_expenses_in_day():
    """
    Test the remove_expenses_in_day function
    """
    assert find_expenses_in_day([[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent']], 12) == [[12, 3, 'food'],
                                                                                               [12, 45, 'rent']]


def test_find_expenses_between_days():
    """
    Test the remove_expenses_between_days function
    """
    assert find_expenses_between_days([[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent'], [17, 2, 'others']], 12,
                                      16) == [[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent']]


def test_find_expenses_of_type():
    """
    Test the remove_expenses_of_type function
    """
    assert find_expenses_of_type([[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent']], 'rent') == [12, 45, 'rent']