import re

content = []
output_list = []
text_scrambled = []
text_cleaned = []
ords = []
char_continue = 'Y'

file_name = input('Enter file name: ')

with open(file_name) as f:
    content = f.readlines()
content = [a.replace('\n', ' ') for a in content]
content = [q.rstrip() for q in content]

shift_input = input('Enter shift amounts: ')
shift_list = shift_input.split()



def initScramble (inputList):
    for b in range(0, len(content)):
        #print(content[b] + 'TEST')
        inputList[b] = inputList[b].replace('E', 'ZW')
        inputList[b] = inputList[b].replace('e', 'zw')
        list_middle = len(inputList[b]) // 2
        inputList[b] = inputList[b][:list_middle] + 'hokie' + inputList[b][list_middle:]
        inputList[b] = 'hokie' + inputList[b] + 'hokie' + '$'
    return inputList
    inputList = []

def ordConverter (inputList):
    output_list = []
    input_string = ''
    output_string = ''

    for c in range(0, len(inputList)):
        input_string = inputList[c]
        for d in range(0, len(inputList[c])):
            if input_string[d].isalpha():
                output_string += (str(ord(input_string[d]))) + ' '
            else:
                output_string += (str(input_string[d])) + ' '
        output_list.append(output_string)
        output_string = ''
        holder_string = ''
    return output_list

def ordShifter (inputList):
    input_ord_holder = ''
    output_ord_holder = ''
    output_list = []
    for e in range(0, len(inputList)):
        input_ord_holder = inputList[e]
        space_idx = [j for j, item in enumerate(output_list) if re.search('\s', item)]
        input_ord_holder = input_ord_holder.split(' ')

        for f in range(0, len(input_ord_holder)):
            z = f % 5
            if str(input_ord_holder[f]).isnumeric():
                if 122 >= int(input_ord_holder[f]) >= 97:
                    output_ord_holder = str((int(input_ord_holder[f]) + int(shift_list[z])))
                    if int(output_ord_holder) > 122:
                        output_ord_holder = str(((int(output_ord_holder) % 97) - 26) + 97)
                elif 65 <= int(input_ord_holder[f]) <= 90:
                    output_ord_holder = str((int(input_ord_holder[f]) + int(shift_list[z])))
                    if int(output_ord_holder) > 90:
                        output_ord_holder = str(((int(output_ord_holder) % 65) - 26) + 65)
            else:
                output_ord_holder = input_ord_holder[f]


            output_list.append(output_ord_holder)
    punct_idx = [i for i, item in enumerate(output_list) if re.search('\W', item)]

    print(space_idx, punct_idx)
    for q in range(0, len(space_idx)):
        output_list.insert(space_idx[q], '#')
    for r in range(0, len(punct_idx)):
        output_list.insert(punct_idx[r], '#')
    return output_list


####################################################
while char_continue == 'Y':

    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
       encrypt = False

    if encrypt:
        content = initScramble(content)
        #print('initscramble : ' + ''.join(content))
        content = ordConverter(content)
        #print('ordConverter : ' + ''.join(content))
        content = ordShifter(content)
        #print('ordShifter : ' + ''.join(content))

        for g in range(0, len(content)):
            content[g] = str(content[g]).rstrip()
            if not content[g].isnumeric():
               text_scrambled.append(str(content[g]))
               text_scrambled.append('')
            else:
               text_scrambled.append(chr(int(str(content[g]).rstrip())))

        text_scrambled = ''.join(text_scrambled)
        text_scrambled = text_scrambled.replace('$', '\n')
        text_scrambled = text_scrambled.replace('@@', ' ')
        text_scrambled = text_scrambled.replace('@', '')
        text_scrambled = text_scrambled.strip(' ')
    print(text_scrambled)

