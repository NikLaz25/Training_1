def MassVote(N, Votes):
    # получаем максимальные значения и их номера
    Votes_max = 0
    for i in range(N):
        if Votes[i] > Votes_max:
            Votes_max = Votes[i]
    count_max = Votes.count(Votes_max)
    position = [x for x in range(len(Votes)) if Votes[x] == Votes_max]

    # Основные циклы
    # если нет победителей
    if count_max != 1:
        result = ('no winner')
    
    # иначе есть только 1 победитель
    else:
        percent = Votes_max/sum(Votes)
        if percent > 0.50:
            result = (f'majority winner {position[0] + 1}')
        else:
            result = (f'minority winner {position[0] + 1}')
    return result