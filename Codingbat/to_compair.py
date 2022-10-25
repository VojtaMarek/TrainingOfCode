
""""
https://codingbat.com/prob/p143951

Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
"""

#my first solution
def lone_sum1(a, b, c):
  if a == b == c: return 0
  elif a == b:return c
  elif a == c:return b
  elif b == c:return a
  else:return a + b + c


#my second solution
def lone_sum2(a, b, c):
  if a == b == c: return 0
  if a == b:return c
  if a == c:return b
  if b == c:return a
  return a + b + c


#NOT my solution
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum