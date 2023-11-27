file = open("Trainees.txt", 'r')
data = open('os_stream.txt', 'w')
for i in file:
    rmv = i.removesuffix('\n')
    s = rmv.split(":")
    if s[2] == 'OS':
        data.write(i)
print('data appended successfully')
file.close()
data.close()