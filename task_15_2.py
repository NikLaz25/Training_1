def TankRush(H1, W1, S1, H2, W2, S2):
    
    # проверяем подходит ли количество строк и столбцов
    if H2 > H1 or W2 > W1:
        result = False
        return result
    
    # разбиваем строку на части
    S1_split = S1.split(' ')
    S2_split = S2.split(' ')

    # основной цикл, проходим каждым элементом 2й матрицы по каждому элементу 1й матрицы
    match_list_1, match_list_2 = [], []
    for i_2, val_2 in enumerate(S2_split):
        for i_1, val_1 in enumerate(S1_split):
            if val_2 in val_1:
                match_list_1.append(val_1)
                match_list_2.append(val_2)

            else:
                pass
        

    #финальная проверка по всем совпадениям
    if len(set(S2_split)) == len(set(match_list_2)) and len(set(S1_split)) == len(set(match_list_1)):
        result = True

    else:
        result = False

    return result