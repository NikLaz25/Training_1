# собираем все части в методе
def TankRush(H1, W1, S1, H2, W2, S2):
    
    # проверяем подходит ли количество строк и столбцов
    if H2 > H1 or W2 > W1:
        result = False
        return result
    
    # разбиваем строку на части
    S1_split = S1.split(' ')
    S2_split = S2.split(' ')

#     определяем все варианты номера начальной строки и столбца, записываем в словарь
    dict_variants = dict()
    for i_1, val_1 in enumerate(S1_split):
        if S2_split[0] in val_1:
            i_string_1 = i_1
            i_column_1 = val_1.index(S2_split[0])
            dict_variants.update({i_string_1: i_column_1})
        else:
            pass


    # цикл по словарю с вариантами начального номера строки и столбца 
    for i_string_1, i_column_1 in dict_variants.items():
        # основной цикл
        i_2 = 0
        general_match = 0

        for i_1, val_1 in enumerate(S1_split):
            try:
                if i_1 >= i_string_1 \
                and S2_split[i_2] in val_1 \
                and val_1.index(S2_split[i_2]) == i_column_1:
                    i_2 += 1
                    general_match += 1
            except:
                pass

        #финальная проверка по всем совпадениям
        if general_match == len(S2_split):
            result = True
            break
        else:
            result = False


    return result