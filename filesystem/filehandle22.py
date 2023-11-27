file = open("Trainees.txt", 'r')
data = open('HPF.txt', 'w')
lst = []
for i in file:
    rmv = i.removesuffix('\n')
    s = rmv.split(':')
    if int(s[3]) > 90:
        data.write(i)
print("data has been appended")
file.close()
data.close()