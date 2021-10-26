# метод
def LineAnalysis(line):

    # проверка первого и последнего символа
    if line[0] != '*' or line[-1] != '*':
        return False
    
    # разбиваем строку
    line_split = line.split('*')
    
    # удаляем первый и последний символ
    del line_split[0]
    del line_split[-1]
    
    #     проверка для пустого списка (когда на воде один символ *)
    if line_split == []:
        return True
    
    # проверяем равенство символов
    for i in range(len(line_split) - 1):
        if line_split[i] == line_split[i + 1]:
            result = True
        else:
            result = False
            return result
            break
            
    # проверяем то, что первый символ это точка или пусто 
    try:
        if line_split[0][0] == '.':
            result = True
        else:
            result = False
    except:
        if line_split[0] == '':
            result = True
        else:
            result = False

    return result