# метод task_19
def ShopOLAP(N, items):
    # разбиваем по парам, чтобы второй элемент был int
    my_list = []
    for val in items:
        element = val.split(' ')
        element[1] = int(element[1])
        my_list += [element]
        
    # отсортируем список по названиям строк
    my_list.sort()
    
    # суммируем одинаковые названия
    my_dict = {}
    for elem in my_list:
        if elem[0] not in my_dict:
            my_dict[elem[0]] = elem[1]
        else:
            my_dict[elem[0]] += elem[1]
            
    # отсортируем словарь по значениям
    sorted_key = sorted(my_dict, key = my_dict.get, reverse = True)
    sorted_dict = {}

    for i in sorted_key:
        sorted_dict[i] = my_dict.get(i)
    
    # переводим снова в строки
    result = []
    for key, val in sorted_dict.items():
        result += [' '.join([key, str(val)])]
        
    return result