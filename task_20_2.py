my_list = []
my_str = ''
step = -1
flag = False # вводим переменную flag для number_command = 4

# метод
def BastShoe(command):
    # задаём глобальные переменные
    global my_str
    global step 
    global my_list
    global flag
    
    # проверка на адекватность команд, чтобы начинались с нужных цифр
    if command[0] == '1' or command[0] == '2' or command[0] == '3' or command[0] == '4' or command[0] == '5':
        pass
    else:
        return my_str

    # проверка на порядок команд, все команды до первой 1 должны пролетать мимо
    if command[0] == '2' and len(my_list) == 0 or command[0] == '3' and len(my_list) == 0 or command[0] == '4' and len(my_list) == 0 or command[0] == '5' and len(my_list) == 0:
        return my_str
    
    # разделяем строку на 1й символ и всё остальное
    number_command = int(command.split(' ')[0])
    new_str = ' '.join(command.split(' ')[1:])
    try:
        while new_str[0] == ' ':
            new_str = new_str[1:]
    except:
        pass
 
    # условие 1,  если уже что-то записано в my_list
    if number_command == 1 and flag == False and len(my_list) > 0:
        my_str = my_list[-1] + new_str
        my_list.append(my_str)
        step += 1
        
        # условие 1,  если my_list пустой
    elif number_command == 1 and flag == False and len(my_list) == 0:
        my_str += new_str 
        my_list.append(my_str)
        step += 1
                    
    # условие 2 удаляем N символов в конце строки, если уже что-то записано в my_list
    elif number_command == 2 and flag == False and len(my_list) > 0:
        try:
            N = int(new_str)
            my_str = my_list[-1]
            my_str = my_str[:(len(my_str) - N)]
            my_list.append(my_str)
            flag = False 
            step += 1
        except:
            my_str = ''
            my_list.append(my_str)
            flag = False 
            step += 1

    # условие 3, если уже что-то записано в my_list
    elif number_command == 3 and len(my_list) > 0:
        try:
            N = int(new_str)
            my_str = my_list[step]
            my_str = my_str[N]

        except:
            my_str = ''

    # условие 4 and step >= 1
    elif number_command == 4 and step >= 1:
        try:
            flag = True
            step -= 1
            my_str = my_list[step]
        except:
            my_str = ''
    
    # условие 4 and step = 0
    elif number_command == 4 and step < 1:
        try:
            flag = True
            my_str = my_list[step]
        except:
            my_str = ''
        
    # условие 1 после условия 4, если уже что-то записано в my_list
    elif number_command == 1 and flag == True and len(my_list) > 0:
        my_list = my_list[(step):(step+1)]
        step = 1
        my_str += new_str
        my_list.append(my_str)
        flag = False 
    
    # условие 2 после условия 4, если уже что-то записано в my_list
    elif number_command == 2 and flag == True and len(my_list) > 0:
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
            flag = False
        
    # условие 5, если step не последний
    elif number_command == 5 and step < (len(my_list) - 1):
        step += 1
        my_str = my_list[step]
        flag = False

    # условие 5, если step самый последний
    elif number_command == 5 and step == (len(my_list) - 1):
        my_str = my_list[step]
        flag = False

    else:
        my_str = ''
    
    return my_str