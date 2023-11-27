
# file = open('Trainees.txt', 'r')
# for i in file:
#     print(i)
# file.close()

# file = open('Trainees.txt', 'r')
# print(file.readline())                    #to read single line from data
# print(file.readlines())               #to readlines
# print(file.tell())                        #to give file open pointer
# file.close()

# file = open('Trainees.txt', 'a')            #append the sring
# empdet = 'T106:John:Web techno:75\n'
# file.write(empdet)
# file.seek(3)                        #give u space of lines
# file.close()



file =  open('Trainees.txt', 'rt')
for i in file:
    s = i.removesuffix('\n')
    data = s.split(":")
    #print(data)
    print(data[1])
file.close()






