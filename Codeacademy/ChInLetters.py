letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
    """my own code"""
    sum = set()
    for ch in word:
    #if character in letters:
        if ch in letters:
            sum.add(ch)
    return len(sum)

def unique_english_letters2(word):
    """copied form codeacademy"""
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters2("Apple"))
# should print 4 