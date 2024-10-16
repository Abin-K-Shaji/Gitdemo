file =open('test.txt')
#print(file.read(12))

#print(file.readline())
#file.close()

#print line by line
line= file.readline()
while line!="":
    print(line)
    line=file.readline()

#stores in list and displayes
for line in file.readlines():
    print(line)
