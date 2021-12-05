def Football(F, N):
    '''проверка возможности упрорядочить массив 2мя способами'''
    standard = sorted(F)

    def comparison(F, standard):
        '''сравнение'''
        i_list = []
        for i in range(len(F)):
            if F[i] != standard[i]:
                i_list += [i]
        return i_list

    i_list = comparison(F, standard)

    '''если на входе упорядоченный массив'''
    if i_list == []:
        return False

    '''если поменяли 2 буквы, то True'''
    if len(i_list) == 2:
        return True

    '''если поменяли более 3х букв, и не по порядку то False'''
    for index in range(len(i_list) - 1):
        if (i_list[index + 1] - i_list[index] != 1) \
        and len(i_list) > 3:
            return False
            break

    '''проверка обратного порядка'''
    if standard[(i_list[0]) : (i_list[-1] + 1)] \
        == F[(i_list[0]) : (i_list[-1] + 1)][::-1]:
        return True

    return
