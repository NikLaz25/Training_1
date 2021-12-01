'''поворот матрицы'''
def MatrixTurn(Matrix, M, N, T):
    '''метод поворачивает матрицу'''

    # подсчитываем количество кругов
    mn_min = min(M, N)
    circle_quantity = int(mn_min / 2)

    def circ(circle_quantity, Matrix):
        '''циклом переводим круги в строки, и помещаем в список'''
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
        return circles

    circles = circ(circle_quantity, Matrix)

    def tern(circles, T):
        '''поворачиваем круги в цикле T раз'''
        turn = 1
        while turn  <= T:
            for circle_i, circle_val in enumerate(circles):
                last = circle_val[-1]
                circles[circle_i] = circle_val[:-1]
                circles[circle_i] = last + circles[circle_i]

            turn += 1
        return circles

    circles = tern(circles, T)


    def save_turn_matrix(circles):
        '''функция записи кругов в макет матрицы'''

        # переводим список строк в список списков
        circles_list = []
        for val in circles:
            circles_list += [list(val)]

        # создаем макет для повернутой матрицы
        turn_matrix = [['0']*N for x in range(M)]

        # цикл записи кругов в макет матрицы
        for circle_i, circle_val in enumerate(circles_list):
            left_edge = circle_i
            len_edge = (N - circle_i*2)
            right_edge = left_edge + len_edge

            # заносим круг целиком в макет матрицы
            # заносим верхнюю часть круга
            turn_matrix[circle_i][left_edge:right_edge] = circle_val[:len_edge]

            # создаём счётчик для номера цифры которую вставляем из круга в повернутую матрицу
            number_in_circle = len(turn_matrix[circle_i][left_edge:right_edge])

            #  проходимся циклом по правому краю круга для circles_list
            for t_matrix_i, t_matrix_val in enumerate(turn_matrix):# определяем номера строк
                if (M - 1 - circle_i) > t_matrix_i >= (circle_i + 1):

                    # заменяем последнее значение списка на нужный символ
                    # turn_matrix[t_matrix_i][-1-circle_i] = circle_val[number_in_circle]
                    t_matrix_val[-1 - circle_i] = circle_val[number_in_circle]
                    #добавляем значение в счётчик
                    number_in_circle += 1

            # заполняем нижнюю часть круга
            down_str = M - 1 - circle_i
            numb_in_cir_next = number_in_circle + len(turn_matrix[down_str][left_edge:right_edge])
            # для сокращения строки
            t_matr_down_str = circle_val[number_in_circle:numb_in_cir_next][::-1]
            turn_matrix[down_str][left_edge:right_edge] = t_matr_down_str
            number_in_circle = numb_in_cir_next

            # заполняем левую часть круга
            for t_matrix_i in range(len(turn_matrix))[::-1]:  # определяем номера строк
                if (M - 1 - circle_i) > t_matrix_i >= (circle_i + 1):
                    # заменяем последнее значение списка на нужный символ
                    turn_matrix[t_matrix_i][circle_i] = circle_val[number_in_circle]

                    # добавляем значение в счётчик
                    number_in_circle += 1
        return turn_matrix

    turn_matrix = save_turn_matrix(circles)

    #  преобразуем список списков в список строк
    for i, val in enumerate(turn_matrix):
        turn_matrix[i] = ''.join(val)

    for i in range(len(Matrix)):
        Matrix[i] = turn_matrix[i]

    return

