# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  """my own code"""
  count = 0
  start = 0
  j = word[0:len(x)]
  for j in word:
    end = int(start + len(x))
    j = word[start:end]
    start += 1
    if j == x:
      count += 1
  return count


def count_multi_char_x2(word, x):
  """copied code"""
  splits = word.split(x)
  return(len(splits)-1)


# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x2("apple", "pp"))
# should print 1