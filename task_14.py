def Unmanned(L, N, track):
    # задаём пременные
    time = 0 #время в пути
    travel = 0 #пройденный путь

    # сформируем карту сфетофоров
    way_traffick_light = [x[0] for x in track]

    # расчет максимального времени,если все светофоры будут красными максимально долго
    time_max = L
    for i in range(N):
        time_max += track[i][2]

    # формируем график работы для каждого светофора
    work_light = [[] for x in range(N)]
    for number_light in range(N):
        cycle = track[number_light][1] + track[number_light][2]
        step = 0
        while len(work_light[number_light]) < (time_max):
            for x in range(cycle):
                if x <= (track[number_light][1] - 1) and step <= (time_max - 1):
                    work_light[number_light].append(0)
                    step += 1
                elif x > (track[number_light][1] -1) and step <= (time_max - 1):
                    work_light[number_light].append(1)
                    step += 1
                else:
                    step += 1
    # собираем основной алгоритм, вариант 1

    while travel < L:
        if travel not in way_traffick_light:
            travel +=1
            time += 1
        else:
            # определяем номер светофора
            for i, val in enumerate(way_traffick_light):
                if travel == val:
                    numb_light = i
                else:
                    pass

            # смотрим какой свет сейчас горит на данном светофоре color =  work_light[numb_light][time]
            # если зеленый, то едем
            if work_light[numb_light][time] == 1:
                travel += 1
                time += 1
            # Иначе стоим, а время идет
            else:
                time += 1

    return(time)
