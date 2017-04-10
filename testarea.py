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

def shiftOrd(listName, shift):
    for y in range(0, len(ordList)):
        # conversion check for utf-8 values
        if not ordList[y].isnumeric():
            ordList[y] = ordList[y]
        # shifting utf-8 values...
        else:
            if int(ordList[y]) >= 97 and int(ordList[y]) <= 122:
                ordList[y] = str(int(ordList[y]) + shift)
                if int(ordList[y]) > 122:
                    ordList[y] = str(((int(ordList[y]) % 97) - 26) + 97)

            elif int(ordList[y]) >= 65 and int(ordList[y]) <= 90:
                ordList[y] = str(int(ordList[y]) + shift)
                if int(ordList[y]) > 90:
                    ordList[y] = str(((int(ordList[y]) % 65) - 26) + 65)
    # re-appending
    for z in range(0, len(ordList)):
        if not ordList[z].isnumeric():
            scrambledText.append(str(ordList[z]))
        else:
            scrambledText.append(chr(int(ordList[z])))

    print(''.join(scrambledText))

while continueQuery == 'Y':

    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
       encrypt = False
    #####
    if encrypt:
        #adding 'hokie' to beginning, middle, and end of ciphertext.
        plainText = plainText.replace('E', 'zw')
        plainText = plainText.replace('e', 'zw')
        plainText_middle_index = len(plainText) // 2
        plainText = plainText[:plainText_middle_index] + 'hokie' + plainText[plainText_middle_index:]
        plainText = 'hokie' + plainText + 'hokie'

        #storing alpha characters as their utf-8 code, rest are stored as-is.
        for x in range(0, len(plainText)):
            if plainText[x].isalpha():
                ordList.append(str(ord(plainText[x])))
            else:
                ordList.append(str(plainText[x]))

        shiftOrd(ordList, shift1)


    