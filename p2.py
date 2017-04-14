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
###########################################################################
#!!!all of the variables with meaningless names are loop variables or counters of some kind.
output_list = []
text_scrambled = []
text_cleaned = []
char_continue = 'Y'
#query and store file name
file_name = input('Enter file name: ')
#opening and reading file into list "content"
with open(file_name) as f:
    content = f.readlines()
content = [q.rstrip() for q in content]
#querying and storing shifts into list "shift_list"
shift_input = input('Enter shift amounts: ')
shift_list = shift_input.split()

###########################################################################
#@input = inputList - the desired list for scrambling
#@return = inputList - the returned scrambled (modified) list
def initScramble (inputList):
    #for every line in quote...
    for b in range(0, len(content)):
        #scramble by replacing e with zw and adding "hokie" to beg, mid, end
        inputList[b] = inputList[b].replace('E', 'ZW')
        inputList[b] = inputList[b].replace('e', 'zw')
        list_middle = len(inputList[b]) // 2
        inputList[b] = inputList[b][:list_middle] + 'hokie' + inputList[b][list_middle:]
        inputList[b] = 'hokie' + inputList[b] + 'hokie'
    return inputList
#@input = inputList - the desired list for ordinate conversion
#@return = output_list - the returned converted list
def ordConverter (inputList):
    output_list = []
    #add newline characters every other index for correct formatting
    for u in range(0, 2*len(inputList)):
        if u % 2 == 1:
            inputList.insert(u, '\n')
    #for every line, for every character, check if char is alphabetical
    for c in range(0, len(inputList)):
        for d in range(0, len(inputList[c])):
            input_string = inputList[c]
            if input_string[d].isalpha():
                #convert to ordinate if it is
                output_list.append(str(ord(input_string[d])))
            else:
                output_list.append((str(input_string[d])))
    return output_list
#@input = inputList - the desired list for ordinate shifting
#@return = output_list - the returned shifted ordinate list
def ordShifter (inputList):
    #z is a counter variable for accessing the shift_list sequentially.
    z = 0
    #the same familiar shift math, but z increments for every non-"\n" character
    #uses modulus to allow for simple counter use instead of nested loops.
    for e in range(0, len(inputList)):
        if str(inputList[e]).isnumeric():
            if 97 <= int(inputList[e]) <= 122:
                inputList[e] = str(int(inputList[e]) + int(shift_list[int(z % 5)]))
                if int(inputList[e]) > 122:
                    inputList[e] = str(((int(inputList[e]) % 97) - 26) + 97)
                output_list.append(int(inputList[e]))
                z += 1
            elif 65 <= int(inputList[e]) <= 90:
                inputList[e] = str(int(inputList[e]) + int(shift_list[int(z % 5)]))
                if int(inputList[e]) > 90:
                    inputList[e] = str(((int(inputList[e]) % 65) - 26) + 65)
                output_list.append(int(inputList[e]))
                z += 1
        elif str(inputList[e]) == '\n':
            #if it sees "\n", restart counter
            output_list.append(str(inputList[e]))
            z = 0
        else:
            output_list.append(str(inputList[e]))
            z += 1
    return output_list
#@input = inputList - the desired list for de-scrambling
#@return = inputList - the returned de-scrambled (modified) list
def deScramble (inputList):
    #basically the reverse of the initScramble function
    for q in range(0, len(inputList)):
        inputList[q] = inputList[q][5:(len(inputList[q]) - 5)]
        list_middle = len(inputList[q]) // 2
        mid_hokie = inputList[q].find('hokie', list_middle - 3, list_middle + 3)
        inputList[q] = (inputList[q])[:mid_hokie] + inputList[q][(mid_hokie+5):]
        inputList[q] = (inputList[q]).replace('ZW', 'E')
        inputList[q] = (inputList[q]).replace('zw', 'e')
    return inputList
#@input = inputList - this kind of does the same thing as ordConverter...
#@return = output_list - the returned converted list
def deConverter (inputList):
    #i'll be honest i didn't know this would be redundant until after i'd written it.
    #technically it does the same thing as ordConverter but this is already late and
    #while this is bad form it's not breaking the code, and we're not being graded
    #on how pythonic or even how streamlined our code is.
    output_list = []

    for ac in range(0, 2*len(inputList)):
        if ac % 2 == 1:
            inputList.insert(ac, '\n')

    for ad in range (0, len(inputList)):
        for ae in range(0, len(inputList[ad])):
            input_string = inputList[ad]
            if input_string[ae].isalpha():
                output_list.append(str(ord(int(input_string[ae]))))
            else:
                output_list.append((str(input_string[ae])))
    return output_list
#@input = inputList - the desired list for reverse-shifting
#@return = output_list - the returned reverse-shifted ordinate list
def deShifter (inputList):
    #same z counter as in ordShifter
    z = 0
    output_list = []
    #the same old backwards conversion math, still using mod math to implement simple
    #incrementing counters to access shift_list rotating values.
    for ab in range(0, len(inputList)):
        if str(inputList[ab]).isnumeric():
            if 97 <= int(inputList[ab]) <= 122:
                inputList[ab] = str(int(inputList[ab]) - int(shift_list[int(z % 5)]))
                if int(inputList[ab]) < 97:
                    inputList[ab] = str(122 - (97 - int(inputList[ab])) + 1)
                output_list.append(inputList[ab])
                z += 1
            elif int(inputList[ab]) >= 65 and int(inputList[ab]) <= 90:
                inputList[ab] = str(int(inputList[ab]) - int(shift_list[int(z % 5)]))
                if int(inputList[ab]) < 65:
                    inputList[ab] = str(90 - (65 - int(inputList[ab])) + 1)
                output_list.append(inputList[ab])
                z += 1
        elif str(inputList[ab]) == '\n':
            output_list.append(str(inputList[ab]))
            z = 0
        else:
            output_list.append(inputList[ab])
            z += 1
    return output_list

###########################################################################
while char_continue == 'Y':
    #repeat until user enters something other than 'Y' when prompted
    if input('Encode (E) or Decode(D)? ') == 'E':
        encrypt = True
    else:
       encrypt = False

    if encrypt:
        #1) scramble plaintext
        #2) convert to ordinates
        #3) shift ordinates
        content = initScramble(content)
        content = ordConverter(content)
        content = ordShifter(content)
        #4) convert ordinates to characters and print
        for t in range(0, len(content)):
            if str(content[t]).isnumeric():
                text_scrambled.append(str(chr(int(content[t]))))
            else:
                text_scrambled.append(str(content[t]))

        print(''.join(text_scrambled))
    
    else:
        #convert ciphertext to ordinates
        #reverse shift ordinate ciphertext
        content = ordConverter(content)
        content = deShifter(content)
        #convert ordinates to characters and store in list
        for ag in range(0, len(content)):
            if str(content[ag]).isnumeric():
                text_cleaned.append(str(chr(int(content[ag]))))
            else:
                text_cleaned.append(str(content[ag]))
        #put everything back together, then de-scramble it and print
        text_cleaned = ''.join(text_cleaned)
        text_cleaned = text_cleaned.split('\n')
        content = deScramble(text_cleaned)
        print('\n'.join(content))
###########################################################################
    #clearing vars for repeat
    text_cleaned = []
    text_scrambled = []
    content = []
    #requerying...
    var_continue = str(input('Go again? (Y/N): '))
    if var_continue == 'Y':
        file_name = input('Enter file name: ')

        with open(file_name) as f:
            content = f.readlines()
        content = [q.rstrip() for q in content]

        shift_input = input('Enter shift amounts: ')
        shift_list = shift_input.split()