def vowel_count(sentence):
    dic = {'vowels': 0, 'consonants': 0, 'other': 0}
    s = list(sentence)
    for i in s:
        if i in 'aeiou':
            dic['vowels'] += 1
        elif i in 'bcdfghjklmnpqrstvwxyz':
            dic['consonants'] += 1
        else:
            dic['other'] += 1
    return dic


data = 'i love python and it so easy to learn'
print(vowel_count(data))