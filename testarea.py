content = []
text_scrambled = []
text_cleaned = []
ords = []
char_continue = 'Y'

file_name = input('Enter file name: ')

with open(file_name) as f:
    content = f.readlines()
content = [a.replace('\n', ' ') for a in content]

shift_input = input('Enter shift amounts: ')
shift_list = shift_input.split()
shift1 = int(shift_list[0])
shift2 = int(shift_list[1])
shift3 = int(shift_list[2])
shift4 = int(shift_list[3])
shift5 = int(shift_list[4])


def initScramble (inputList):
    for b in range(0, len(content)):
        inputList[b] = inputList[b].replace('E', 'ZW')
        inputList[b] = inputList[b].replace('e', 'zw')
        list_middle = len(inputList[b]) // 2
        inputList[b] = inputList[b][:list_middle] + 'hokie' + inputList[b][list_middle:]
        inputList[b] = 'hokie' + inputList[b] + 'hokie'
    return inputList
    inputList = []

def ordConverter (inputList):
    output_list = []
    holder_string = ''
    for c in range(0, len(inputList)):
        holder_string = inputList[c]
        for d in range(0, len(inputList[c])):
            if holder_string[d].isalpha():
                output_list.append(ord(holder_string[d]))
            else:
                output_list.append(holder_string[d])
    return output_list

def ordShifter (inputList):
    output_list = []
    holder_string = ''
    for e in range(0, len(inputList)):
        holder_string = inputList[e]
        print(inputList[e])
        for g in range(0, len(inputList[e])):
            if not holder_string[g].isnumeric():
                output_list.append(holder_string[g])
            else:
                for h in range(0, len(shift_list)):
                    if int(holder_string[g]) >= 97 and int(holder_string[g]) <= 122:
                        holder_string[g] = str(int(holder_string[g]) + int(shift_list[h]))
                        if int(holder_string[g]) > 122:
                            holder_string[g] = str(((int(holder_string[g]) % 97) - 26) + 97)
    
                    elif int(holder_string[g]) >= 65 and int(holder_string[g]) <= 90:
                        holder_string[g] = str(int(holder_string[g]) + int(shift_list[h]))
                        if int(holder_string[g]) > 90:
                            holder_string[g] = str(((int(holder_string[g]) % 65) - 26) + 65)
    
    return inputList


####################################################
while char_continue == 'Y':

    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
       encrypt = False

    if encrypt:
        content = initScramble(content)
        content = ordConverter(content)
        content = ordShifter(content)

        print(content)
