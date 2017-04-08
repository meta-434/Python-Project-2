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
        plainText = plainText.replace('E', 'zw')
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

        #print(plainText)
        #print(shift1, shift2, shift3, shift4, shift5)
            
    

