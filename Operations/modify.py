__author__ = 'Damaris'


class const():
    sum_index = 1
    date_index = 0
    type_index = 2


def modify(lista, day_of_month, spent_sum, expense_type):
    """
    Modify a new expense to the list of lists "lista"
    :param lista:
    :param day_of_month: int
    :param spent_sum: int
    :param expense_type: string
    :return: lists lista and undo_list
    """
    found = False
    for i in range(len(lista)):
        if lista[i][const.date_index] == day_of_month:
            if lista[i][const.type_index] == expense_type:
                lista[i][const.sum_index] = spent_sum
                found = True
        if not found:
            print('Cheltuiala pe care doriti sa o actualizati nu exista inca')
    return lista


def test_modify():
    """
    test modify function
    """
    assert modify([[12, 3, 'food'], [21, 56, 'clothes'], [14, 14, 'phone']], 21, 200, 'clothes') == [[12, 3, 'food'],
                                                                                                     [21, 200,
                                                                                                      'clothes'],
                                                                                                     [14, 14, 'phone']]
