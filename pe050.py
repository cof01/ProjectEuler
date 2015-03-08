from mytime import exe
import mymath

def main():
  MAX = 10**6
  pri = mymath.get_primes(MAX)
  pri_length = len(pri['list'])
  i = 0
  c_max = 0
  ans = 0
  while i < pri_length:
    s = pri['list'][i]
    j = i + 1
    c = 1
    while j < pri_length and s + pri['list'][j]< MAX:
      s += pri['list'][j]
      c += 1
      if pri['bool'][s] and c_max < c:
        ans = s
        c_max = c
      j += 1
    i += 1
  print ans

exe('main()')