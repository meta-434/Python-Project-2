file_name = input('Enter file name: ')
file_obj = open(file_name, 'r')
grabbed_doc = []
pTextHolder = []


for x in file_obj:
    grabbed_doc = x.split()
    grabbed_doc = " ".join(grabbed_doc)
    grabbed_doc = grabbed_doc.replace('\n', '')
    pTextHolder.append(grabbed_doc)
    grabbed_doc = []

for row in pTextHolder:
    print("".join(map(str,row)))

