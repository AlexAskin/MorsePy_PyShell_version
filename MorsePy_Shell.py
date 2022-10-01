
# Python Shell app of MorseCode Converter


import csv


def init_morsecode_baselist(): # Create Base-List
    
    FILENAME = "NewMorseTabletUnicode.csv"

    morsecode_baselist = []

    with open(FILENAME, "r", newline="", encoding="utf8") as file:
        reader = csv.reader(file)
        
        for row in reader:
            morsecode_baselist.append(  [ row[0], row[1], row[2] ]  )
            
    #for i in morsecode_baselist:   #['65', 'A', '.-']...
        #print(i)
        
    return morsecode_baselist



def init_encode_dict():

    encode_dict_list = []
    
    for i in range(len(morsecode_baselist)):
        if morsecode_baselist[i][2] == '':
            pass
        else:
            encode_dict_list.append( [ morsecode_baselist[i][1], morsecode_baselist[i][2] ] )
            
    #for i in encode_dict_list: print(i)

    encode_dict = dict(encode_dict_list)

    #print('\nEncode Dictionary:')
    #for i in encode_dict: print( i, encode_dict[i])
    
    return encode_dict
        

def init_dict():
    
    dict_eng_list = []
    
    for i in range(0,58):
        if i in (27,29):pass
        else: dict_eng_list.append( [ morsecode_baselist[i][2], morsecode_baselist[i][1] ] )    
        
    decode_dict_eng = dict(dict_eng_list)
    
    #print('\nEnglish Dict:')
    #for i in decode_dict_eng: print(i, ' == ',decode_dict_eng[i])
        
    return decode_dict_eng


def init_dict_rus():
    dict_rus_list = []

    for i in range(0,32):
        if i in (27,29):pass
        else: dict_rus_list.append( [ morsecode_baselist[i][2], morsecode_baselist[i][1] ] ) 

    
    for i in range(94,126):
        dict_rus_list.append( [ morsecode_baselist[i][2], morsecode_baselist[i][1] ] )    
 
    decode_dict_rus = dict(dict_rus_list)

    #print('\nRussian Dict:')
    #for i in decode_dict_rus: print(i, ' == ',decode_dict_rus[i])
        
    return decode_dict_rus



morsecode_baselist = init_morsecode_baselist() # Loading values from CSV-file to Base-List    

encode_dict = init_encode_dict()


decode_dict_eng = init_dict()
decode_dict_rus = init_dict_rus()



def show_morsecode():
    FILENAME = "universal_mosre.csv"
    with open(FILENAME, "r", newline="", encoding="utf8") as file:
        reader = csv.reader(file)
        
        for i in reader:
            x = 10 - len(i[1])
            space = ' '* x
            
            y = 10 - len(i[3])
            space1 = ' '* y
            
            output = f'{i[0]}  {i[1]}{space}{i[2]}  {i[3]}{space1}{i[4]}{i[5]}'
            print( output )




def encode_morse_message():

    message = input('Input your Message>>>')
    
    if message == '0':
        print('back to menu <<<<')
        return

    count_i = 0
    
    encode_signlist = []
    
    for i in message:
        count_i += 1

        if i == ' ':
            encode_signlist.append('|')
        else:
            encode_signlist.append(encode_dict[i])   
      
    print()

    encode_message = ''
    
    for i in encode_signlist:
        #print( i ,end = ' ')
        encode_message += i + ' '
        
    print(encode_message )
    
    print('\ncount_i:',count_i, '\n')    

    #   add to Report:
    message += '\n'
    encode_message += '\n'
    with open("reports\\encode_morse.txt", "a", encoding='utf-8') as file:
        file.write('\n')
        file.write(message)
        file.write(encode_message)


    encode_morse_message()
    



eng_dict = True

def decode_morse_message():
    global eng_dict
    
    message = input('Input your MorseCode-Message>>>')    

    if message == '0':
        print('back to menu <<<<')
        return

    if message == 'eng':
        print('Eng Dict On!')
        eng_dict = True
        
        decode_morse_message()
        return
        
    if message == 'rus':
        print('Rus Dict On!')
        eng_dict = False
        
        decode_morse_message()
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
    
    count_i = 0
    
    decode_message = ''
    
    if devide_mes[-1] == '': devide_mes.pop()

    for i in devide_mes:  
        count_i += 1
         
        try:
            if eng_dict == True:
                try:
                    
                    if i == '|': decode_message += ' '
                    else: decode_message += decode_dict_eng[i]
                    
                except:
                    
                    decode_message_rus = '' # bypath of case mystake
                    for i in devide_mes:  
                        count_i += 1
                        if i == '|': decode_message_rus += ' '
                        else: decode_message_rus += decode_dict_rus[i]
                    decode_message = decode_message_rus
                    break
            else:
                    if i == '|': decode_message += ' '
                    else: decode_message += decode_dict_rus[i]
                                
        except:
            print(i, '- Unknown Sign!')
            decode_message += '*'

    print()
    print(decode_message)
    print('count_i:',count_i)
    print()

    #   add to Report:
    message += '\n'
    decode_message += '\n'
    with open("reports\\decode_morse.txt", "a", encoding='utf-8') as file:
        file.write('\n')
        file.write(message)
        file.write(decode_message)

        
    decode_morse_message()



def show_reports():
    show_rep = input('Show Encode or Decode Reports(1/2):')
    print()
    if show_rep == '1':
        print('ENCODE backup:\n')
        with open('reports\\encode_morse.txt', "r", newline="", encoding="utf8") as file:
            for line in file:
                print(line, end="")
        
    elif show_rep == '2':
        print('DECODE backup:\n')
        with open('reports\\decode_morse.txt', "r", newline="", encoding="utf8") as file:
            for line in file:
                print(line, end="")
    print()

    

def select_menu():
    
    print('Select Option:')
    print('1 - ENCODE MESSAGE')
    print('2 - DECODE MESSAGE')

    print('3 - Show MorseCode')
    print('4 - Show Reports')
    print()    
    print('9 - Exit')


    user_select = input('>>>')
    
    try:
        
        user_select = int(user_select)

        if user_select == 1:
            print("(input '0' - back to Menu)\n")
            encode_morse_message()

        elif user_select == 2:
            print("(input '0' - back to Menu)\n")
            decode_morse_message()            
            
        elif user_select == 3:
            show_morsecode()

        elif user_select == 4:
            show_reports()

        elif user_select == 9:
            global run_flag
            print('Exit')
            run_flag = False
            
        else:
            print('\nSorry COMMAND NOT FOUND!\n')
            return  select_menu()

    except:
        print('\nError Input! INVALID VALUE!\n')
        return select_menu()




#    Run App:   |
run_flag = True

while run_flag == True:
    print()
    select_menu() 
