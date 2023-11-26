def vowcons(input):
    val = list(input)
    vow = ''
    cons = ''
    for i in val:
        if i in 'aeiou':
            vow += i
        else:
            cons += i
    return cons + vow


def encrypt_sentence(msg):
    result = ''
    data = msg.split(' ')
    for i in range(0, len(data)):
        if (i + 1) % 2 == 0:
            result += vowcons(data[i]) + ' '
        else:
            result += data[i][::-1] + ' '
    print(result)


msg_sentence = 'the sun rises in the east'
encrypt_sentence(msg_sentence)
