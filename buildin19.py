def words_count(sentence):

    dic = {}
    s = sentence.split()
    for i in s:
        if len(i) in dic:
            dic[len(i)] += 1

        else:
            dic[len(i)] = 1
    print(dic)






data = 'I love python and it so easy to learn'
words_count(data)