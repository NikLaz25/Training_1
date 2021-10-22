# учимся работать со списком списков. Финал
def TankRush(H1, W1, S1, H2, W2, S2):
    # проверяем подходит ли количество строк и столбцов
    if H2 > H1 or W2 > W1:
        result = False
        return result

    # разбиваем строку на части
    S1_split = S1.split(' ')
    S2_split = S2.split(' ')

    #   !!! определяем все варианты номера начальной строки и столбца, записываем их в список списков
    start_variants = []
    i_column_1 = -1
    for i_1, val_1 in enumerate(S1_split):
        while 1:
            i_column_1 = val_1.find(S2_split[0], i_column_1 + 1)
            if i_column_1 == -1:
                break
            start_variants += [[i_1, i_column_1]]

    # цикл по вариантам начального номера строки и столбца
    for start in start_variants:
        i_string_1 = start[0]
        i_column_1 = start[1]

        # основной цикл
        i_2 = 0
        general_match = 0

        for i_1, val_1 in enumerate(S1_split):
            try:
                if i_1 < i_string_1:
                    pass

                elif i_1 >= i_string_1 \
                        and (val_1[i_column_1:(i_column_1 + len(S2_split[i_2]))] == S2_split[i_2]):
                    i_2 += 1
                    general_match += 1

                else:
                    break

            except:
                break

        # финальная проверка по всем совпадениям
        if general_match == len(S2_split):
            result = True
            break
        else:
            result = False

    return result

