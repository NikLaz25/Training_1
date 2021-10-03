def BigMinus(s1, s2):
    target = ''
#     определяем какое число больше
    if len(s1) > len(s2):
        bigger = 's1'
    elif len(s1) < len(s2):
        bigger = 's2'
    else:
        for i1, i2 in zip(s1, s2):
            if i1 > i2:
                bigger = 's1'
                break
            elif i2 > i1:
                bigger = 's2'
                break
            else:
                pass
            bigger = 's1'

#     если нужно муняем местами

    if bigger == 's1':
        a1 = s1[::-1]
        a2 = s2[::-1]
    else:
        a1 = s2[::-1]
        a2 = s1[::-1]

    flag = 0
#     основной цикл
    for i in range(len(a1)):
        try:
            if flag == 0 and (int(a1[i]) - int(a2[i])) < 0:
                difference = 10 + int(a1[i]) - int(a2[i])
                flag = 1

            elif flag == 0 and (int(a1[i]) - int(a2[i])) >= 0:
                difference = int(a1[i]) - int(a2[i])
                flag = 0


            elif flag == 1 and (int(a1[i]) - 1 - int(a2[i])) < 0:
                difference = int(10 + a1[i])- 1 - int(a2[i])
                flag = 1

            elif flag == 1 and (int(a1[i]) - 1 - int(a2[i])) >= 0:
                difference = int(a1[i]) - 1 - int(a2[i])
                flag = 0

            target += str(difference)

        except:
            if flag == 1 and (int(a1[i]) -1) < 0:
                target += str(9)
                flag = 1

            elif flag == 1 and (int(a1[i]) -1) >= 0:
                target += str(int(a1[i]) -1)
                flag = 0

            else:
                target += str(a1[i])

    # убираем первые нули
    number = target[::-1]
    flag_2 = 0
    new_number = ''
    for i in number:
        if i == '0' and flag_2 == 0:
            pass
        else:
            flag_2 = 1
            new_number += i
    return new_number
