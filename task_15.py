# создаем функцию
def TankRush(H1, W1, S1, H2, W2, S2):
    
    # проверяем подходит ли количество строк и столбцов
    if H2 > H1 or W2 > W1:
        result = False
        return result
    
    # разбиваем строку на части
    S1_split = S1.split(' ')
    S2_split = S2.split(' ')

    # основной цикл
    general_match = 0
    removed_lines_matrix1 = []
    for i2, line_2 in enumerate(S2_split): # проходим матрицу 2
        local_match = 0
        for i1, line_1 in enumerate(S1_split): # проходим матрицу 1
            # убираем из цикла строки, где уже были совпадения
            if i1 in removed_lines_matrix1:
                pass
            else:
                # цикл поиска line_2 в line_1
                if line_2 in line_1: # если нашли 
                    general_match += 1
                    local_match += 1
                    removed_lines_matrix1.append(i1)
                    break
                else:  # если не нашли
                    pass

        # проверяем есть ли локальные совпадения по одной строке
        if local_match < 1:
            result = False
            break

        # подстчитываем количество общих совпадений general_match               
        elif general_match >= H2:
            result = True
            break
    return result