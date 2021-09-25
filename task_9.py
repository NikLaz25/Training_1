# собираю воедино
def TheRabbitsFoot(s, encode):
    if encode == True:
        # убираем пробелы из строки.
        s_cut = ''.join(s.split(' '))

        # вычисляем N, line, column
        N = len(s_cut)
        sqr = N ** (0.5)
        sqr_str = str(sqr)
        line = int(sqr_str[0])
        column = int(sqr_str[2])

        # проверяем количество строк Только для шифрования
        if column == 0:
            column = 1
        while (line * column) < N:
            line += 1

        # разбиваем строку по line элементов
        my_matrix = []
        for i in range(line):
            if i < (line):
                my_matrix += [s_cut[i * column:(i + 1) * column]]
            else:
                my_matrix += [s_cut[i * column:]]

        # выдает результат
        translate_1 = [''] * column
        for i in range(column):
            for j in my_matrix:
                try:
                    translate_1[i] += j[i]
                except:
                    a = 1

        # печатаем результат
        result = ' '.join(translate_1)

    else:
        # разбиваем по линиям, смотрим матрицу
        s_split = s.split()

        # вычисляем line, column
        line = len(s_split)
        column_len = []
        for i in s_split:
            column_len += [len(i)]
        column = max(column_len)

        # РАСШИФРОВКА выдает результат
        result = ''
        for i in range(column):
            for j in s_split:
                try:
                    result += j[i]
                except:
                    a = 1
    return result
