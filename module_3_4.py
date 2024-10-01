import re
def single_root_words( root_word, *other_words):
    same_words = []
    for i in other_words:
        root_word = root_word.lower()
        i = i.lower()
        if root_word in i :
            same_words.append(i)
        elif i in root_word:
            same_words.append(re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), i, 1))
# без этого медота возвращалось значение в нижнем регистре
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
