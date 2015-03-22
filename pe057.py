from mytools import *
from fractions import Fraction

@debug
def expantion(n):
  if n == 1:
    return 2 + Fraction(1, 2 + Fraction(1,2))
  else:
    return 2 + Fraction(1, expantion(n-1))
    
  
@main_start
@get_time
def main():
  SEARCH_START, SEARCH_MAX = 1, 10**3 + 1
  #SEARCH_START, SEARCH_MAX = 1, 8
  ans = 0
  f = 2 + Fraction(1, 2 + Fraction(1,2))
  for i in range(SEARCH_START, SEARCH_MAX):
    f = 2 + Fraction(1, f)
    if len(str((f-1).numerator)) > len(str(f.denominator)):
      ans += 1
  return ans
   
print main()
  