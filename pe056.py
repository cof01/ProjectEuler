from mytools import *

@get_time
def main():
  SEARCH_START, SEARCH_MAX =1, 101
  ans = 0
  for a in range(SEARCH_START, SEARCH_MAX):
    for b in range(SEARCH_START, SEARCH_MAX):
      ans = max(sum(map(int, str(a**b))), ans)
  return ans

print main()