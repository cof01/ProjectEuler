from mytools import get_time, debug, main_start

@get_time
def main():
  n, ans = 1, 0
  while len(str(9**n)) >= n:
    for b in range(1,10):
      if len(str(b**n)) == n:
        ans += 1
    n += 1
  return ans

print main()
       