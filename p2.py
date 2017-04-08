#@package p2.py
#<This program encodes and decodes text using a custom Caesar Cypher system>

#@author Alex Hapgood
#@date 2017/04/03
#
#Virginia Tech Honor Code Pledge
#On my honor:
#I have not discussed the Python language code in my program with
#anyone other than my instructor or the teaching assistants
#assigned to this course.
#I have not used Python language code obtained from another student,
#or any other unauthorized source, either modified or unmodified.
#If any Python language code or documentation used in my program
#was obtained from another source, such as a text book of course
#notes, that has been clearly noted with a proper citation in
#the comments of my program.
#I have not designed this program in such a way as to defeat or
#interfere with the normal operation of the WebCat Server.
#
#<Alex Hapgood>
############################################################################
file_name = input('Enter file name: ')
file_obj = open(file_name, "w")

message = input('Enter a string: ')
val_list = []
scrambled = []
unscrambled = []
var_continue = 'Y'
shift = input('Enter shift amounts: ')
x = shift.split(' ')
shift1 = int(x[0])
shift2 = int(x[1])
shift3 = int(x[2])
shift4 = int(x[3])
shift5 = int(x[4])

while var_continue == 'Y':

    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
       encrypt = False
    #####
    if encrypt:
        #adding 'hokie' to beginning, middle, and end of ciphertext.
        message = message.replace('E', 'zw')
        message = message.replace('e', 'zw')
        message_middle_index = len(message) // 2
        message = message[:message_middle_index] + 'hokie' + message[message_middle_index:]
        message = 'hokie' + message + 'hokie'

        #storing alpha characters as their utf-8 code, rest are stored as-is.
        for x in range(0, len(message)):
            if message[x].isalpha():
                val_list.append(str(ord(message[x])))
            else:
                val_list.append(str(message[x]))

        for y in range(0, len(val_list)):
            #conversion check for utf-8 values
            if not val_list[y].isnumeric():
                val_list[y] = val_list[y]
            #shifting utf-8 values...
            else:
                 if int(val_list[y]) >= 97 and int(val_list[y]) <= 122:
                   val_list[y] = str(int(val_list[y]) + shift)
                   if int(val_list[y]) > 122:
                       val_list[y] = str(((int(val_list[y])%97)-26)+97)

                 elif int(val_list[y]) >= 65 and int(val_list[y]) <= 90:
                    val_list[y] = str(int(val_list[y]) + shift)
                    if int(val_list[y]) > 90:
                       val_list[y] = str(((int(val_list[y])%65)-26)+65)
        #re-appending
        for z in range(0, len(val_list)):
            if not val_list[z].isnumeric():
                scrambled.append(str(val_list[z]))
            else:
               scrambled.append(chr(int(val_list[z])))

        print(''.join(scrambled))
    #####
    else:
        for a in range(0, len(message)):
            if message[a].isalpha():
                val_list.append(str(ord(message[a])))
            else:
                val_list.append(str(message[a]))

        for b in range(0, len(val_list)):
            if not val_list[b].isnumeric():
               val_list[b] = val_list[b]
            else:
                if int(val_list[b]) >= 97 and int(val_list[b]) <= 122:
                    val_list[b] = str(int(val_list[b]) - shift)
                    if int(val_list[b]) < 97:
                        val_list[b] = str(122 - (97 - int(val_list[b])) + 1)

                elif int(val_list[b]) >= 65 and int(val_list[b]) <= 90:
                    val_list[b] = str(int(val_list[b]) - shift)
                    if int(val_list[b]) < 65:
                        val_list[b] = str(90 - (65 - int(val_list[b])) + 1)

        for c in range(0, len(val_list)):
            if not val_list[c].isnumeric():
               scrambled.append(str(val_list[c]))
            else:
               scrambled.append(chr(int(val_list[c])))

        decrypt_string = (''.join(scrambled))
        decrypt_string = decrypt_string[5:(len(decrypt_string) - 5)]
        decrypt_middle_index = len(decrypt_string) // 2
        delim = decrypt_string.find('hokie', decrypt_middle_index - 3, decrypt_middle_index + 3)
        decrypt_string = decrypt_string[:delim] + decrypt_string[(delim+5):]
        decrypt_string = decrypt_string.replace('zw', 'e')
        print(decrypt_string)

        decrypt_string = ''
        message = ''
        val_list = []
    #####
    var_continue = str(input('Go again? (Y/N): '))
    if var_continue == 'Y':
        message = input('Enter a string: ')
        shift = int(input('Enter the shift amount: '))
        val_list = []
        scrambled = []
        unscrambled = []






