def Keymaker(k):
    '''формируем список закрытых дверей - doors'''
    doors = [1] * k

    def step_doors(step, doors):
        '''метод цикл для каждого шага'''
        for i in range(k):
            if (i + 1) % step == 0 and doors[i] == 0:
                doors[i] = 1
            elif (i + 1) % step == 0 and doors[i] == 1:
                doors[i] = 0
        return doors
    
    '''цикл для каждого шага'''
    for step in range(k+1)[2:]:
        doors = step_doors(step, doors)
    
    '''переводим список в строку'''
    doors_str = ''
    for i in doors:
        doors_str += f'{i}'
        
    return doors_str
