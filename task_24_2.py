# метод
def MatrixTurn(Matrix, M, N, T):

    # подсчитываем количество кругов
    min_M_N = min(M, N)
    circle_quantity = int(min_M_N / 2)
    
    # циклом переводим круги в строки, и помещаем в список
    circles = []
    for circle_i in range(circle_quantity):
        left_edge = circle_i
        len_edge = (N  - circle_i*2)
        right_edge = left_edge + len_edge
        circle = Matrix[circle_i][left_edge:right_edge]

        for i in Matrix[(circle_i + 1):(M - 1- circle_i)]:
            circle += i[left_edge:right_edge][-1]

        circle += Matrix[M - 1 - circle_i][left_edge:right_edge][::-1]

        for i in Matrix[(circle_i + 1):(M - 1- circle_i)][::-1]:
            circle += i[left_edge:right_edge][0]

        circles += [circle]
        
    # поворачиваем круги в цикле T раз
    turn = 1
    while turn  <= T:
        for circle_i in range(len(circles)):
            last = circles[circle_i][-1]
            circles[circle_i] = circles[circle_i][:-1]
            circles[circle_i] = last + circles[circle_i]
        turn += 1

    # переводим список строк в список списков
    circles_list = []
    for i in range(len(circles)):
        circles_list += [list(circles[i])]
     
    # создаем макет для повернутой матрицы
    turn_matrix = [['0']*N for x in range(M)] 

    # цикл записи кругов в макет матрицы
    for circle_i in range(len(circles_list)):
        left_edge = circle_i
        len_edge = (N  - circle_i*2)
        right_edge = left_edge + len_edge
        
        # заносим круг целиком в макет матрицы
        # заносим верхнюю часть круга
        turn_matrix[circle_i][left_edge:right_edge] = circles_list[circle_i][:len_edge]

        # создаём счётчик для номера цифры которую вставляем из круга в повернутую матрицу 
        number_in_circle = len(turn_matrix[circle_i][left_edge:right_edge])

        #  проходимся циклом по правому краю круга для circles_list
        for t_matrix_i in range(len(turn_matrix)): # определяем номера строк
            if t_matrix_i >= (circle_i + 1) and t_matrix_i < (M - 1 - circle_i):

                # заменяем последнее значение списка на нужный символ
                turn_matrix[t_matrix_i][-1-circle_i] = circles_list[circle_i][number_in_circle]

                #добавляем значение в счётчик
                number_in_circle += 1

        # заполняем нижнюю часть круга
        down_str = M -1 - circle_i
        number_in_circle_next = number_in_circle + len(turn_matrix[down_str][left_edge:right_edge])
        turn_matrix[down_str][left_edge:right_edge] = circles_list[circle_i][number_in_circle:number_in_circle_next][::-1]
        number_in_circle = number_in_circle_next

        # заполняем левую часть круга
        for t_matrix_i in range(len(turn_matrix))[::-1]: # определяем номера строк
            if t_matrix_i >= (circle_i + 1) and t_matrix_i < (M - 1 - circle_i):

                # заменяем последнее значение списка на нужный символ
                turn_matrix[t_matrix_i][circle_i] = circles_list[circle_i][number_in_circle]

                #добавляем значение в счётчик
                number_in_circle += 1
                
    #  преобразуем список списков в список строк
    for i in range(len(turn_matrix)):
        turn_matrix[i] = ''.join(turn_matrix[i])
        
    def ya_pripuh():
        global Matrix
        Matrix = turn_matrix
    
    ya_pripuh()
    return 