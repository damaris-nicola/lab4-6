__author__ = 'Damaris'


def add(lista, day_of_month, spent_sum, expense_type):
    """
    Add a new expense to the list of lists "lista"
    :param day_of_month: int
    :param spent_sum: int
    :param expense_type: string
    :return: lists lista and undo_list
    """
    lista.append([day_of_month, spent_sum, expense_type])
    return lista


def test_add():
    """
    test add function
    """
    assert add([[12, 3, 'food'], [4, 13, 'phone']], 21, 200, 'clothes') == [[12, 3, 'food'], [4, 13, 'phone'],
                                                                            [21, 200, 'clothes']]