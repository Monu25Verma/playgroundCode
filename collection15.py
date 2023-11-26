#
def translate(b_dict, english_word):
    result = ''
    for x in english_word:
        if x in b_dict:
            result += b_dict[x] + ' '
    return result


b_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
list_words = input("Enter the string to convert english into swedish language: ")
english_word = list(list_words.split(" "))
print(translate(b_dict, english_word))

