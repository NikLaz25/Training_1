# метод
def TreeOfLife(H, W, N, tree):
    # меняем значения дерева на 1 и 0
    for i in range(len(tree)):
        tree[i] = tree[i].replace('.', '0')
        tree[i] = tree[i].replace('+', '1')
    
    # цикл прохождения по годам
    for year in range(N+1)[1:]:
        
        # добавляем 1 к каждому значению во всех строках матрицы
        for i in range(len(tree)):
            tree[i] = tree[i].replace('3', '4')
            tree[i] = tree[i].replace('2', '3')
            tree[i] = tree[i].replace('1', '2')
            tree[i] = tree[i].replace('0', '1')
        
        if year %2 == 0:

            # отмечаем ветки на удаление
            list_delete = []
            for i in range(len(tree)):
                for j in range(len(tree[i])):
                    if int(tree[i][j]) >= 3:
                        list_delete += [[i, j]]
                        list_delete += [[(i + 1), j]]
                        list_delete += [[(i - 1), j]]
                        list_delete += [[i, (j + 1)]]
                        list_delete += [[i, (j - 1)]]
            
            # удаляем лишние в списке на удаление
            for i, val in enumerate(list_delete):
                for j in range(len(val)):
                    if val[j] < 0:
                        list_delete[i] = list_delete[0]
                if val[0] >= H:
                    list_delete[i] = list_delete[0]
                elif val[1] >= W:
                    list_delete[i] = list_delete[0]
         
            # обнуляем всех, кто есть есть в списке на удаление
            for i in list_delete:
                str_list = list(tree[i[0]])
                str_list[i[1]] = '0'
                str_list = ''.join(str_list)
                tree[i[0]] = str_list
        
        else:
            pass
            
    # меняем значения дерева на + и .
    for i in range(len(tree)):
        tree[i] = tree[i].replace('0', '.')
        tree[i] = tree[i].replace('1', '+')
        tree[i] = tree[i].replace('2', '+')
        tree[i] = tree[i].replace('3', '+')
    
    return tree
