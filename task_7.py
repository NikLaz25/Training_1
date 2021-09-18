def WordSearch(len_, s, subs):
    '''При необходимости разбиваем слова'''
    s_split = s.split()
    s_small = []
    for i in s_split:
        if len(i) > len_:
            s_small += [i[:len_]]
            s_small += [i[len_:]]
        else:
            s_small += [i]

    '''Основной цикл - генерим строки заданной длины'''
    s_split = s_small
    new_split = []
    skip = 0
    count_sum = 1
    while count_sum != 0:
        count_sum = 0
        for i in range(len(s_split)):

            if skip == 1:

                skip = 0
            else:
                if i < (len(s_split)-1):
                    if len(s_split[i] + ' ' + s_split[i+1]) < len_:
                        new_split += [s_split[i] + ' ' + s_split[i+1]]

                        skip = 1
                        count_sum += 1
                    else:
                        new_split += [s_split[i]]

                else:
                    if len(s_split[i-1] + ' ' + s_split[i]) < len_:
                        break
                    else:
                        new_split += [s_split[i]]
        s_split = new_split
        new_split = []

    '''В каждой строке ищем слово'''
    subs = 'строк'
    target_list = []

    for i in s_split:
        target_count = 0
        for j in (i.split( )):
            if j == subs:
                target_count += 1
        if target_count > 0:
            target_list.append(1)
        else:
            target_list.append(0)
    return target_list



