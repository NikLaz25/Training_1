def BigMinus(s1, s2):
    target = ''
    if len(s1) < len(s2):
        a1 = s2[::-1]
        a2 = s1[::-1]
    else:
        a1 = s1[::-1]
        a2 = s2[::-1]
    flag = 0
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

    return (target[::-1])

