from mytools import get_time
import mymath
import math

@get_time
def main():
  target = 600851475143
  i = 1
  while target != 1:
    i += 2
    while not target % i:
      target /= i
  print i

@get_time
def main2():
  target = 600851475143
  pri = mymath.get_primes(int(math.sqrt(target)))
  max_p = 1
  for p in pri['list']:
    while not target % p:
      target /= p
      max_p = p
  if target != 1:
    print target
  else:
    print max_p

if __name__ == '__main__':
  main()
  main2()