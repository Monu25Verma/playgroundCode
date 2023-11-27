file = open("Trainees.txt", 'r')
lst = []
print(file)
count = 0
dic = {}
for i in file:
    rmv = i.removesuffix('\n')
    data = rmv.split(":")
    if data[0] in dic:
        dic[data[0]] = data[3]
    else:
        dic[data[0]] = data[3]

print(dic)
file.close()
