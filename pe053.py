from math import factorial

def defineC(max):
  f_list = [factorial(i) for i in range(max+1)]
  def C(n,r):
    return f_list[n] / ( f_list[r] * f_list[n-r] )
  return C

def main():
  SEARCH_START, SEARCH_MAX, THRESHOLD = 1, 100, 10**6
  #C = defineC(SEARCH_MAX)
  C = lambda n, r : factorial(n) / (factorial(r) * factorial(n-r))
  ans = 0
  for n in range(SEARCH_START,SEARCH_MAX+1):
    for r in range(0,n+1):
      if C(n,r) > THRESHOLD:
        ans += 1
  return ans
import time
s = time.time()
print main()
print time.time() -s
  
