my_list = []
my_str = ''
step = -1
flag = False # вводим переменную flag для number = 4

# метод
def BastShoe(command):
    # задаём глобальные переменные
    global my_str
    global step 
    global my_list
    global flag
    
    # проверка на адекватность
    if command[0] == '1' or command[0] == '2' or command[0] == '3' or command[0] == '4' or command[0] == '5':
        pass
    else:
        return my_str
    
    # разделяем строку на 1й символ и всё остальное
    number = int(command.split(' ')[0])
    new_str = ' '.join(command.split(' ')[1:])
    try:
        while new_str[0] == ' ':
            new_str = new_str[1:]
    except:
        pass
   

    
    # условие 1
    if number == 1 and flag == False:
        my_str += new_str
        my_list.append(my_str)
        step += 1
        flag = False # вводим переменную flag для number = 4
        

            
    # условие 2 удаляем N символов в конце строки
    elif number == 2 and flag == False:
        try:
            N = int(new_str)
            my_str = my_list[-1]
            my_str = my_str[:(len(my_str) - N)]
            my_list.append(my_str)
            flag = False # вводим переменную flag для number = 4
            step += 1
        except:
            my_str = ''
            my_list.append(my_str)
            flag = False 
            step += 1

    # условие 3 
    elif number == 3 and flag == False:
        try:
            N = int(new_str)
            my_str = my_list[-1]
            my_str = my_str[N]
            my_list.append(my_str)
            step += 1
        except:
            my_str = ''
            my_list.append(my_str)
            flag = False 
            step += 1
        
    # условие 4 and step >= 1
    elif number == 4 and step >= 1:
        try:
            flag = True
            step -= 1
            my_str = my_list[step]
        except:
            my_str = ''
            return my_str
    
    # условие 4 and step = 0
    elif number == 4 and step < 1:
        try:
            flag = True
#             step -= 1
            my_str = my_list[step]
        except:
            my_str = ''
            return my_str
        
    # условие 1 после условия 4
    elif number == 1 and flag == True:
#         my_list = my_list[:(step+1)]
        my_list = my_list[(step):(step+1)]
        step = 1
        my_str += new_str
        my_list.append(my_str)
        flag = False 
    
    # условие 2 после условия 4
    elif number == 2 and flag == True:
        my_list = my_list[(step):(step+1)]
        step = 1
        flag = False 
        N = int(new_str)
        try:
            my_str = my_list[-1]
            my_str = my_str[:(len(my_str) - N)]            
            my_list.append(my_str)
        except:
            my_str = ''
            my_list.append(my_str)
    # условие 3 после 4
    elif number == 3 and flag == True:
        my_list = my_list[(step):(step+1)]
        N = int(new_str)
        try:
            my_str = my_list[-1]
            my_str = my_str[N]
            my_list.append(my_str)
            flag = False
            step += 1
        except:
            my_str = ''
            my_list.append(my_str)
            flag = False 
            step += 1  
        
    # условие 5
    elif number == 5:
        try:
            step += 1
            my_str = my_list[step]
        except:
            step -= 1
            my_str = my_list[step]
            
    else:
        my_str = ''


    return my_str