def is_isogram(word):
    if not isinstance(word, str):
        raise TypeError('This should be a string')
    if not word:
        isogram = False
    else:
        isogram = len(word) == len(set(word.lower()))
    return word, isogram

print (is_isogram("abolishment"))
print (is_isogram("suziki"))
print (is_isogram(200))
