def encode(message):
    empty_list = []
    empty_str = ''
    for i in message:
        if set(empty_list) == set(message):
            break
        if i not in empty_list:
            empty_list.append(i)
            count = message.count(i)
            empty_str += str(count)
            if count > 1:
                empty_str += i
    return empty_str
print(encode('AAABBVVCC'))
