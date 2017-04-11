plainText = []

file_name = input('Enter file name: ')

with open(file_name) as fileObj:
    plainText = fileObj.read().replace('\n', ' ')

ordList = []
scrambledText = []
continueQuery = 'Y'

shiftHolder = input('Enter shift amounts: ')
alpha = shiftHolder.split()
shift1 = int(alpha[0])
shift2 = int(alpha[1])
shift3 = int(alpha[2])
shift4 = int(alpha[3])
shift5 = int(alpha[4])

while continueQuery == 'Y':

    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
       encrypt = False

    if encrypt:
        plainText = plainText.replace('E', 'ZW')
        plainText = plainText.replace('e', 'zw')
        plainTextMiddle = len(plainText) // 2
        plainText = plainText[:plainTextMiddle] + 'hokie' + plainText[plainTextMiddle:]
        plainText = 'hokie' + plainText + 'hokie'
        
        for x in range(0, len(plainText)):
            if plainText[x].isalpha():
                ordList.append(str(ord(plainText[x])))
            else:
                ordList.append(str(plainText[x]))
        for y in range(0, len(ordList)):
            if not ordList[y].isnumeric():
                ordList[y] = ordList[y]
            else:
                for z in range(0, len(alpha)):
                    #print(alpha[int(z)])

                    if int(ordList[y]) >= 97 and int(ordList[y]) <= 122:
                        ordList[y] = str(int(ordList[y]) + int(alpha[z]))
                        if int(ordList[y]) > 122:
                            ordList[y] = str(((int(ordList[y]) % 97) - 26) + 97)

                    elif int(ordList[y]) >= 65 and int(ordList[y]) <= 90:
                        ordList[y] = str(int(ordList[y]) + int(alpha[z]))
                        if int(ordList[y]) > 90:
                            ordList[y] = str(((int(ordList[y]) % 65) - 26) + 65)
        for w in range(0, len(ordList)):
            if not ordList[w].isnumeric():
                scrambledText.append(str(ordList[w]))
            else:
                scrambledText.append(chr(int(ordList[w])))

        print(''.join(scrambledText))
        
    else:
        for a in range(0, len(plainText)):
            if plainText[a].isalpha():
                ordList.append(str(ord(plainText[a])))
            else:
                ordList.append(str(plainText[a]))
                
        for b in range(0, len(ordList)):
            if not ordList[b].isnumeric():
                ordList[b] = ordList[b]
            else:
                for q in range(0, len(alpha)):
                    
                    if int(ordList[b]) >= 97 and int(ordList[b]) <= 122:
                        ordList[b] = str(int(ordList[b]) - int(alpha[q]))
                        if int(ordList[b]) < 97:
                            ordList[b] = str(122 - (97 - int(ordList[b])) + 1)
    
                    elif int(ordList[b]) >= 65 and int(ordList[b]) <= 90:
                        ordList[b] = str(int(ordList[b]) - int(alpha[q]))
                        if int(ordList[b]) < 65:
                            ordList[b] = str(90 - (65 - int(ordList[b])) + 1)

        for c in range(0, len(ordList)):
            if not ordList[c].isnumeric():
                scrambledText.append(str(ordList[c]))
            else:
                scrambledText.append(chr(int(ordList[c])))

        decrypt_string = (''.join(scrambledText))
        decrypt_string = decrypt_string[5:(len(decrypt_string) - 5)]
        decrypt_middle_index = len(decrypt_string) // 2
        delim = decrypt_string.find('hokie', decrypt_middle_index - 3, decrypt_middle_index + 3)
        decrypt_string = decrypt_string[:delim] + decrypt_string[(delim + 5):]
        decrypt_string = decrypt_string.replace('zw', 'e')
        decrypt_string = decrypt_string.replace('ZW', 'E')
        print(decrypt_string)

        decrypt_string = ''
        message = ''
        val_list = []
        ####
        var_continue = str(input('Go again? (Y/N): '))

    if continueQuery == 'Y':
        file_name = input('Enter a file name: ')
        shiftHolder = input('Enter shift amounts: ')
        alpha = shiftHolder.split()
        shift1 = int(alpha[0])
        shift2 = int(alpha[1])
        shift3 = int(alpha[2])
        shift4 = int(alpha[3])
        shift5 = int(alpha[4])

    ordList = []
    scrambledText = []
    plainText = []

    with open(file_name) as fileObj:
        plainText = fileObj.read().replace('\n', ' ')
    #print(plainText)
    #print(shift1, shift2, shift3, shift4, shift5)

    

