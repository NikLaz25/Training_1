def ConquestCampaign(N, M, L, battalion):
    target_squea = N * M
    seized_n = []
    seized_m = []
    count_day = 0
    '''разделяем списки'''
    for i in range(len(battalion)):
        if i % 2 == 0:
            seized_n.append(battalion[i] - 1)
        else:
            seized_m.append(battalion[i] - 1)
    '''Генерим матрицу'''
    matrix = [[0 for x in range(M)] for x in range(N)]
    # захватываем зоны высадки
    for i in range(len(seized_n)):
        matrix[seized_n[i]][seized_m[i]] = 1
    count_day += 1
    seized_squae = 0
    #     основной цикл
    while seized_squae < target_squea:
        seized_n = []
        seized_m = []
        seized_squae = 0
        for n in range(N):
            for m in range(M):
                if matrix[n][m] == 1:
                    seized_n.append(n)
                    seized_m.append(m)
                    #                 подсчитываем захваченные зоны
                    seized_squae += 1
                    #                 проверка на окончание
                    if seized_squae >= target_squea:
                        return count_day
        # захватываем соседние зоны
        count_day += 1
        for a in range(len(seized_n)):
            if (seized_n[a] - 1) >= 0:
                matrix[seized_n[a] - 1][seized_m[a]] = 1
            if (seized_n[a] + 1) < N:
                matrix[seized_n[a] + 1][seized_m[a]] = 1
            if (seized_m[a] - 1) >= 0:
                matrix[seized_n[a]][seized_m[a] - 1] = 1
            if (seized_m[a] + 1) < M:
                matrix[seized_n[a]][seized_m[a] + 1] = 1

    return