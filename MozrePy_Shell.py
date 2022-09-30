# Python script for print a Symbols ABC and
# their corresponding Signs of Morse Code

import csv


 

def init_morsecode_baselist(): # Загружаем Базовую Таблицу из Директории Аппки
    
    FILENAME = "NewMorseTabletUnicode.csv"

    morsecode_baselist = []

    with open(FILENAME, "r", newline="", encoding="utf8") as file:
        reader = csv.reader(file)
        
        for row in reader:
            morsecode_baselist.append(  [ row[0], row[1], row[2] ]  )
            
    for i in morsecode_baselist:   #['65', 'A', '.-']
        print(i)

    return morsecode_baselist




def init_morsecode_main_list():

    morsecode_main_list = []

    num_i = 0
    
    for i in range(1110):
        #print(type(i), i )

        if i in range(33,127):
            
            if i in (60,62,91,92,93,94,96,123,124,125,126):
                morsecode_main_list.append([f'{i}.',''])
                num_i += 1
                
            else:
                var1 = morsecode_baselist[num_i][1]
                var2 = morsecode_baselist[num_i][2]
                
                morsecode_main_list.append([f'{i}.',var1, var2])
                num_i += 1
                
        elif i in range(1040,1104):
                var1 = morsecode_baselist[num_i][1]
                var2 = morsecode_baselist[num_i][2]
                
                morsecode_main_list.append([f'{i}.',var1, var2])
                num_i += 1
                
        else:
            morsecode_main_list.append([f'{i}.',''])   

    #for i in morsecode_main_list:
        #print(i)


    

         
    return morsecode_main_list





def init_dicts():
    print()
    print()
    print()

    dict_eng_list = []
    
    for i in range(len(morsecode_mainlist)):
        
        if i in range(33,91):
            if i in (60,62,91,92,93,94,96,123,124,125,126):
                pass
            else:
                dict_eng_list.append( [ morsecode_mainlist[i][2], morsecode_mainlist[i][1] ] )    
        


    for i in dict_eng_list:
        print(i)

    print(len(dict_eng_list))

    decode_dict_eng = dict(dict_eng_list)
    print(len(decode_dict_eng))
    
    for i in decode_dict_eng:
        print(i, decode_dict_eng[i])
    
    print()

        

    print()
    print()
    print()
    
    dict_rus_list = []
    
    for i in range(len(morsecode_mainlist)):
        
        if i in range(33,65):
            if i in (60,62):
                pass
            else:
                dict_rus_list.append( [ morsecode_mainlist[i][2], morsecode_mainlist[i][1] ] )    
        
        if i in range(1040,1072):
                dict_rus_list.append( [ morsecode_mainlist[i][2], morsecode_mainlist[i][1] ] )    
        


    for i in dict_rus_list:
        print(i)

    print(len(dict_rus_list))
    print()

    decode_dict_rus = dict(dict_rus_list)
    print(len(decode_dict_rus))
    
    for i in decode_dict_rus:
        print(i, decode_dict_rus[i])
        

    return decode_dict_eng


morsecode_baselist = init_morsecode_baselist() # Загружаем Базовую Таблицу из Директории Аппки
morsecode_mainlist = init_morsecode_main_list() # Преобразуем Базовую Таблицу в Основную Таблицу с Порядковыми Номерами символов
decode_dict_eng = init_dicts() #Создаем Анг и Рус Словари символов

def get_sym():
    get_sym = input('Enter Morse Code Sym -> ')


    print(decode_dict_eng[get_sym])





def encode_morse_message():
    
    message = input('Input your Message>>>')
    
    if message == '0':
        print('back to menu <<<<')
        return

    print()
    
    count_i = 0

    encode_signlist = []
    
    for i in message:
        count_i += 1

        try:
            if i == ' ':
                encode_signlist.append('|')
            else:
                #print(i, ord(i), morsecode_mainlist[ord(i)], morsecode_mainlist[ord(i)][2])
                encode_signlist.append(morsecode_mainlist[ord(i)][2])
        
        except:
            encode_signlist.append('*')
            pass
        
        
    print()

    for i in encode_signlist:
        print( i ,end = ' ')

        
    print()
    print()
    print('count_i:',count_i)    
    print()

    
    #for i in message:
        #print(ord(i) ,end = '  ')    # MAYBE LATER!
    #print()

    encode_morse_message()






def decode_morse_message():


    print(morsecode_mainlist[8])
    print(morsecode_mainlist[42])
    print(morsecode_mainlist[56])
    print(morsecode_mainlist[124])
    
    message = input('Input your MorseCode-mes>>>')

    if message == '0':
        print('back to menu <<<<')
        return

    
    message += ' '
    
    devide_mes = []
    sign = ''
    
    for i in message:


        
        if i == ' ':
            devide_mes.append(sign)
            sign = ''
        
        else:
            sign += i            
        
    print(devide_mes)


    word = ''

    count_i = 0
    for i in devide_mes:  
        print(i)

        count_i += 1
        if i == '|':
        
            word += ' '

            
        else:


        
            try:
                
                for k in range(len(morsecode_baselist)):
                    count_i += 1
                    if i == '':
                        pass
                    else:
                        if morsecode_baselist[k][2] == i:
                            word += morsecode_baselist[k][1]
                            break
            except:
                pass
                    
                

        
    print(word)

        

    print()
    print()
    print('count_i:',count_i)    
    print()






def select_menu():
    print('Select Option:')
    print('1 - ENCODE MESSAGE')
    print('2 - DECODE MESSAGE')
    print('3 - get_sym()')
    #print('3 - International Morse')
    print('4 - Show Coder List  ')    
    print('5 - morse_coder.csv')


    user_select = input('>>>')
    
    try:
        
        user_select = int(user_select)

        if user_select == 1:
            encode_morse_message()


        elif user_select == 2:
            decode_morse_message()            



            
        elif user_select == 3:
            
            print('\nSome function')
            init_morsecode_main_list()
            #init_morsecode_baselist()
            pass


        elif user_select == 4:
            get_sym()

            #print_coder_list()
            
            
        elif user_select == 5:
            
            show_morse_coder()







        elif user_select == 11:
            print_syms()
        elif user_select == 22:
            print_syms1()
        elif user_select == 33:
            init_symbols_list()


            
        else:
            print('\nSorry NOT FOUND!\n')
            return  select_menu()
        
    except:
        print('\nError Input! NOT FOUND!\n')
        return select_menu()




while True:
    print()
    select_menu() 
