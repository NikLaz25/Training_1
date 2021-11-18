# метод
def SherlockValidString(s):
    # формируем список уникалиных букв
    uniqae_list = []
    for i in s:
        if i not in uniqae_list:
            uniqae_list += i
    
    # подсчитываем количество каждой буквы
    count_list = []
    for i in uniqae_list:
        count_list.append(s.count(i))
    
    # формируем словарь
    my_dict = {}
    for i in count_list:
        if my_dict.get(i) is None:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    
    # проверяем соответствие условиям
    keys = list(my_dict.keys())
    if len(my_dict.keys()) == 1:
        return True
    elif len(my_dict.keys()) <=2 and (keys[0] - keys[1]) == -1 and my_dict.get(keys[1]) == 1:
        return True
    elif len(my_dict.keys()) <=2 and (keys[1]) == 1 and my_dict.get(keys[1]) == 1:
        return True
    elif len(my_dict.keys()) <=2 and (keys[0]) == 1 and my_dict.get(keys[0]) == 1:
        return True
    else:
        pass
    return