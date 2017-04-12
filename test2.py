continueQuery = 'Y'
content_value = ''
ord_string = ''
ord_list = []
ord_list_shifted = []
list_scrambled = []
file_name = input('Enter file name: ')

with open(file_name) as f:
    content = f.readlines()
content = [a.replace('\n', ' ') for a in content]

print(content[3])

shift_input = input('Enter shift amounts: ')
shift_list = shift_input.split()

while continueQuery == 'Y':

    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
        encrypt = False

    if encrypt:
        for a in range(0, len(content)):
            content_value = content[a]
            content_value = content_value.replace('E', 'ZW')
            content_value = content_value.replace('e', 'zw')
            content_value_middle = (len(content_value) // 2)
            content_value = 'hokie' + content_value[:content_value_middle] + 'hokie' + \
                            content_value[content_value_middle:] + 'hokie'
            content[a] = content_value
            content_value = ''

        for b in range(0, len(content)):
            component_string = content[b]

            for c in range(0, len(component_string)):
                if str(component_string[c]).isalpha():
                    ord_string += str(ord(str(component_string[c]))) + ' '
                else:
                    ord_string += str(component_string[c]) + ' '
            ord_list.append(ord_string)
            ord_string = ''

        for d in range(0, len(ord_list)):
            convert_list = ord_list[d]
            convert_string_list = convert_list.split()

            for e in range(0, len(convert_string_list)):
                if str(convert_string_list[e]).isnumeric():
                    for z in range(0, len(shift_list)):
                        #print(shift_list[int(z)])
                        print('before ' + chr(int(convert_string_list[e])), int(convert_string_list[e]), int(shift_list[int(z)]))
                        if 97 <= int(convert_string_list[e]) <= 122:
                            convert_string_list[e] = str(int(convert_string_list[e]) + int(shift_list[int(z)]))
                            print('after ' + chr(int(convert_string_list[e])), int(convert_string_list[e]), int(shift_list[int(z)]))
                            if int(convert_string_list[e]) > 122:
                                convert_string_list[e] = str(((int(convert_string_list[e]) % 97) - 26) + 97)

                        elif 65 <= int(convert_string_list[e]) <= 90:
                            convert_string_list[e] = str(int(convert_string_list[e]) + int(shift_list[int(z)]))
                            if int(convert_string_list[e]) > 90:
                                convert_string_list[e] = str(((int(convert_string_list[e]) % 65) - 26) + 65)

                else:
                    convert_string_list[e] = convert_string_list[e]
                    list_scrambled.append(convert_string_list[e])


