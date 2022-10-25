"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
https://codingbat.com/prob/p118406
"""

def make_bricks(small, big, goal):
  big_fit = goal // 5
  big_rest = goal % 5
  #small_fit = goal - big_fit
  
  if (big_fit <= big) and (big_rest <= small):
    return True
  elif ((goal - small) <= (5 * big)) and (small >= 4):
    return True
  return False



print(make_bricks(3, 2, 10))

"""
here is the solution from the codingbat page: https://codingbat.com/doc/practice/makebricks-solution-code.html interesting!
"""