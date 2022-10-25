def is_isogram(word):
    """tohle jsem napsal já"""
    data = set()
    x = 0
    while x < len(word):
        if word[x] in data:
            return True
        else:
            data.add(word[x])
            x += 1
    return False


def is_isogram2(word):
    """tohle jsem upravil dle předlohy, s využitím for cyklu"""
    word = word.lower()

    data = set()
    for character in word:
        if character in data:
            return True
        data.add(character)
    return False

word = str(input("Test an isogram: "))
print (is_isogram(word))
print (is_isogram2(word))


