import math
import mymath

def continued_fraction(x):
  i = int(math.sqrt(x))
  n, m = 1, i
  try:
    while True:
      yield i, n, m
      tm = x - m**2
      if tm == 0:
        raise StopIteration
      tn = int(n / mymath.gcd(n,tm))
      tm = int((x -m**2) / mymath.gcd(n,tm))
      i = int(tn * (math.sqrt(x)+m) / tm)
      m = -(tn * m - i * tm)
      n = tm
  finally:
    pass

def get_period(x):
  comb_list = []
  fraction_gen = continued_fraction(x)
  for i,n,m in fraction_gen:
    comb = {'i':i,'n':n,'m':m}
    if comb in comb_list:
      fraction_gen.close()
    else:
      comb_list.append(comb)

  return len(comb_list) - 1

def main(target=10000):
  ans = 0
  for p in range(1,target+1):
    if get_period(p) % 2:
      ans += 1
  return ans 

print main()
