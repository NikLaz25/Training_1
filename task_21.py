# метод
def BiggerGreater(input):

    # делаем реверс
    revers_word = input[::-1]
    
    # ищем первое убывающее значение decreasing
    count_degreasing = 0
    for i in (range(len(revers_word) - 1)):
        if revers_word[i] > revers_word[i + 1]:
            index_decreasing = i + 1
            decreasing = revers_word[i + 1]
            count_degreasing = 1
            break
    
    #отбрасываем варианты, когда передвинуть буквы невозможно
    if count_degreasing == 0:
        return ''
    
    # найти справа(слева) значение minimum_from_more = минимальное, но больше decreasing
    str_minimum_from_more = ''
    for i in range(len(revers_word[:(index_decreasing)])):
        if revers_word[i] > decreasing:
            str_minimum_from_more += revers_word[i]
    minimum_from_more = min(str_minimum_from_more)
    
    # ищем справа(слева) минимальное значение minimum
    minimum = min(revers_word[:(index_decreasing + 1)])
    
    # формируем новую строку - переворачиваем обратно, в ней убраны значения minimum_from_more и minimum
    # decreasing заменен на 1
    new_word = revers_word.replace(decreasing, '1', 1)[::-1]
    new_word = new_word.replace(minimum_from_more, '', 1)
    new_word = new_word.replace(minimum, '', 1)
     
    # собираем итоговое значение
    result_word = ''
    for i in range(len(new_word)):
        if new_word[i] == '1' and decreasing != minimum:
            result_word += minimum_from_more
            result_word += minimum
            result_word += decreasing
        elif new_word[i] == '1' and decreasing == minimum:
            result_word += minimum_from_more
            result_word += minimum
        else:
            result_word += new_word[i]
    return result_word