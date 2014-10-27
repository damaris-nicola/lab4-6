__author__ = 'Damaris'

expenses = ['food', 'clothes', 'phone', 'rent', 'others']


class const():
    sum_index = 1
    date_index = 0
    type_index = 2


def find_expenses_greater_than_sum(lista, min_sum):
    """
    Search expenses that have sum greater than specified sum. All found expenses are added to list "cheltuieli_gasite".
    The function return list of found expenses
    :param lista: list
    :param min_sum: int
    :return: list
    """
    if min_sum > 0:
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if min_sum < cheltuiala[const.sum_index]:
                cheltuieli_gasite.append(cheltuiala)
    else:
        raise KeyError("Suma introdusa nu este valida")
    return cheltuieli_gasite


def print_expanses_greater_than_sum(lista, min_sum):
    """
    Print expenses grater than specified sum.
    :param lista: list
    :param min_sum: int
    :return:none
    """
    cheltuieli_gasite = find_expenses_greater_than_sum(lista, min_sum)
    for chelt in cheltuieli_gasite:
        print(chelt)


def find_expenses_before_day_less_than_sum(lista, max_sum, day):
    """
    Search expenses registered before specified date and that have sum less than specified sum. All found expenses are
    added to list "cheltuieli_gasite". The function return list of found expenses
    :param lista:
    :param max_sum:
    :param day:
    :return:
    """
    if max_sum > 0 & (1 <= day < 32):
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if (cheltuiala[const.date_index] < day) & (cheltuiala[const.sum_index] < max_sum):
                cheltuieli_gasite.append(cheltuiala)
    else:
        raise KeyError("Suma sau ziua introdusa nu este valabila")
    return cheltuieli_gasite


def print_before_day_less_than_sum(lista, max_sum, day):
    """
    Print expenses before specified day and sum less then given amount.
    :param lista: list
    :param max_sum: int
    :param day: int
    :return:none
    """
    cheltuieli_gasite = find_expenses_before_day_less_than_sum(lista, max_sum, day)
    for chelt in cheltuieli_gasite:
        print(chelt)


def find_expenses_of_type(lista, expense_type):
    """
    Search expenses of specified type. All found expenses are added to list "cheltuieli_gasite".
    The function return list of found expenses.
    :param lista:
    :param expense_type:
    :return:
    """
    if expense_type in expenses:
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if cheltuiala[const.type_index] == expense_type:
                cheltuieli_gasite.append(cheltuiala)
        for chelt in cheltuieli_gasite:
            print(chelt)
    else:
        raise KeyError("Tipul introdus nu este valid")
    return cheltuieli_gasite


def print_expenses_of_type(lista, expense_type):
    """
    Print expenses of specified type
    :param lista: list
    :param expense_type: string
    :return: none
    """
    cheltuieli_gasite = find_expenses_of_type(lista, expense_type)
    for chelt in cheltuieli_gasite:
        print(chelt)


def test_find_expanses_greater_than_sum():
    """
    Test find_expanses_greater_than_sum function
    """
    assert find_expenses_greater_than_sum([[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent']], 10) == [
        [15, 25, 'food'], [12, 45, 'rent']]


def test_find_expenses_before_day_less_than_sum():
    """
    Test find_expenses_before_day_less_than_sum function
    """
    assert find_expenses_before_day_less_than_sum([[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent']], 10, 15) == [12,
                                                                                                                     45,
                                                                                                                     'rent']


def test_print_expenses_of_type():
    """
    Test find_expenses_of_type function
    """
    assert find_expenses_of_type([[12, 3, 'food'], [15, 25, 'food'], [12, 45, 'rent']], 'food') == [[12, 3, 'food'],
                                                                                                    [15, 25, 'food']]
