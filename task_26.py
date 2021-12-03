def white_walkers(village):
    '''определяем ходоков в конкретной деревне'''

    def index_list(village):
        '''определяем индекс и список чисел'''
        index_num = []
        num_list = []
        for i, val in enumerate(village):
            try:
                num = int(val)
                index_num += [i]
                num_list += [num]
            except:
                pass
        return index_num, num_list

    def check_sum(num_list):
        '''проверка сумм соседних чисел'''
        target_index = []
        for i in range(len(num_list) - 1):
            if (num_list[i] + num_list[i + 1] == 10):
                target_index += [[index_num[i], index_num[i + 1]]]
            else:
                pass
        return target_index

    def count_walkers(target_index):
        '''подсчет ходоков'''
        for target_i in target_index:
            count_walk = 0
            for val in village[(target_i[0] + 1): (target_i[1])]:
                if val == "=":
                    count_walk += 1
            if count_walk != 3:
                return False
                break

        if count_walk == 3:
            return True
        return

    # запускаем методы
    index_num, num_list = index_list(village)
    if len(index_num) < 2:
        return False
    target_index = check_sum(num_list)

    result = count_walkers(target_index)

    return result
