from mytools import get_time

@get_time
def main():
  t = 2**1000
  ans = sum(map(lambda x : int(x), str(t)))
  print ans
  
@get_time
def main2():
  t = 2**1000
  N = 10
  ans = 0
  while t:
    (t, r) = (t//N, t%N)
    ans += r
  print ans

main()
main2()