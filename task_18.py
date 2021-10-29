# прорабатываем метод
def MisterRobot(N, data):
    # 1-я проверка, только на убывание
    for i in range(len(data) - 2):
        if data[i] > data[i + 1] > data[i + 2]:
            result = False
            return result
        else:
            result = True
            
    # более точная проверка
    for i in range(len(data) - 2):
        increment = 0
        while increment == 0:
            if data[i] > data[i + 1] > data[i + 2]: # убывание
                result = False
                return result
            else:
                if data[i] < data[i + 1] < data[i + 2]: # возрастание
                    increment = 1
                else:
                    # двигаем тройку
                    a = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = data[i + 2]
                    data[i + 2] = a
    
    result = True
    return result