"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
https://codingbat.com/prob/p158497

:::::::::::::::TO MAKE IT A BETTER CODE::::::::::::::::::::
def in1to10(n, outside_mode):
  if  outside_mode:  
    if (1 < n < 10):
      return False
    else:
      return True
  else:
    if (1 <= n <= 10):
      return True
    else:
      return False

in1to10(9, False)

"""
#here we go..

def in1to10(n, outside_mode):
    range_in, range_out = (1 <= n <= 10), not(1 < n < 10)
    if outside_mode:
        return range_out
    return range_in


  
print(in1to10(9, False))