def WordSearch(len_, s, subs):
    '''При необходимости разбиваем слова'''
    s_split = s.split()
    s_small = []
    for i in s_split:
        s_small += [i[x:x+len_] for x in range(0, len(i), len_)]
    '''Основной цикл - генерим строки заданной длины'''
    new_split = []
    element = str()
    for i in range(len(s_small)):
        if i == 0 and len(s_small[i]) == len_:
            new_split.append(s_small[i]) # s_small[i] идёт в список

        elif ((len(element)+ 1 + len(s_small[i])) <= len_) and i != (len(s_small) - 1):
            element = element + ' ' + s_small[i] # элетент прирастает

        elif ((len(element)+ 1 + len(s_small[i])) > len_) and i != (len(s_small) - 1):
            if element != '':
                new_split.append(element) # элетент идёт в список
            element = s_small[i] # s_small[i] становиться новым элементом

        elif ((len(element)+ 1 + len(s_small[i])) <= len_) and i == (len(s_small) - 1):
            element = element + ' ' + s_small[i] # элетент прирастает
            new_split.append(element)  # элетент идёт в список

        else:
            new_split.append(element)  # элетент идёт в список
            new_split.append(s_small[i]) # s_small[i] идёт в список
    '''В каждой строке ищем слово'''
    target_list = []

    for i in new_split:
        target_count = 0
        for j in (i.split( )):
            if j == subs:
                target_count += 1
        if target_count > 0:
            target_list.append(1)
        else:
            target_list.append(0)
    return target_list







