__author__ = 'Damaris'

expenses = ['food', 'clothes', 'phone', 'rent', 'others']


class const():
    sum_index = 1
    date_index = 0
    type_index = 2


def compute_expense_sum_for_type(lista, expense_type):
    suma = 0
    if expense_type in expenses:
        for cheltuiala in lista:
            if cheltuiala[const.type_index] == expense_type:
                suma += cheltuiala[const.sum_index]
    else:
        raise KeyError("Tipul introdus invalid")
    return suma


def print_expense_sum_for_type(lista, expense_type):
    """
    Print the total spent sum for an expense type.
    :param lista: list
    :param expense_type: string
    :return:none
    """
    suma = compute_expense_sum_for_type(lista, expense_type)
    print("Suma = ", suma)


def compute_greatest_spent_sum(lista):
    cheltuiala_maxima = [0, 0, '']
    for cheltuiala in lista:
        if cheltuiala[const.sum_index] > cheltuiala_maxima[const.sum_index]:
            cheltuiala_maxima = cheltuiala
    return cheltuiala_maxima


def print_greatest_spent_sum(lista):
    """
    Print the greatest spent sum and the day when it was spent.
    :param lista: list
    :return:none
    """
    cheltuiala_maxima = compute_greatest_spent_sum(lista)
    if cheltuiala_maxima[const.sum_index] > 0:
        print("Cheltuiala maxima s-a efectuat in ziua {} cu suma de {}".format(cheltuiala_maxima[const.date_index],
                                                                               cheltuiala_maxima[const.sum_index]))
    else:
        print("Nu exista nicio zi cu cheltuiala maxima")


def find_expenses_equal_sum(lista, spent_sum):
    if spent_sum > 0:
        cheltuieli_gasite = []
        for cheltuiala in lista:
            if spent_sum == cheltuiala[const.sum_index]:
                cheltuieli_gasite.append(cheltuiala)
    else:
        raise KeyError("Suma introdusa nu este valida")
    return cheltuieli_gasite


def print_expanses_equal_sum(lista, spent_sum):
    """
    Print expenses for a certain spent sum.
    :param lista: list
    :param spent_sum: int
    :return: none
    """
    cheltuieli_gasite = find_expenses_equal_sum(lista, spent_sum)
    for chelt in cheltuieli_gasite:
        print(chelt)


def sort_expenses_by_type(lista):
    if lista != []:
        lista.sort(key=lambda x: x[1])
    else:
        raise KeyError("Nu exista o lista introdusa")
    return lista


def print_sorted_expenses_by_type(lista):
    """
    Print expenses sorted by type
    :param lista: list
    :return: none
    """
    sorted_list = sort_expenses_by_type(lista)
    print(sorted_list)


def test_compute_expense_sum_for_type():
    """
    Test the print_expense_sum_for_type function
    """
    assert compute_expense_sum_for_type([[12, 3, 'food'], [15, 21, 'food'], [9, 14, 'phone']], 'food') == 24


def test_compute_greatest_spent_sum():
    """
    Test the print_greatest_spent_sum function
    """
    assert compute_greatest_spent_sum([[12, 3, 'food'], [15, 21, 'food'], [9, 14, 'phone']]) == [15, 21, 'food']


def test_find_expanses_equal_sum():
    """
    Test the print_expanses_equal_sum function
    """
    assert find_expenses_equal_sum([[12, 3, 'food'], [15, 21, 'food'], [9, 14, 'phone']], 3) == [12, 3, 'food']


def test_sort_expenses_by_type():
    """
    Test the print_sorted_expenses_by_type function
    """
    assert sort_expenses_by_type([[12, 3, 'food'], [15, 21, 'food'], [9, 14, 'phone']]) == [[12, 3, 'food'],
                                                                                            [15, 21, 'food'],
                                                                                            [9, 14, 'phone']]
