import mymath
from mytools import get_time
import math

@get_time
def main():
    target = 2 * (10**6)
    pri = mymath.get_primes(target)
    print sum(pri['list'])

@get_time
def main2():
    target = 2 * (10**6)
    L = [0,0]+range(2,target+1)
    L[4::2] = [0] * (len(L[4::2]))
    p=3
    p_max = int(math.sqrt(target))
    while p<=p_max:
        if L[p]:
            L[p*2::p] = [0] * (len(L[p*2::p]))
        p+=2
    L.remove(0)
    print sum(L)



def generate_primes(n):
  primes = [2]
  append = primes.append
  for i in range(3, n+1, 2):
    j = 1
    while len(primes) > j and primes[j]*primes[j] <= i:
      if i % primes[j] == 0:
        break
      j += 1
    else:
      primes += [i]
    if i % (n // 100) == 1:
      print "%d / %d" % (i, n)
  return primes

@get_time
def h():
  n = 2000000
  primes = generate_primes(n)
  result = sum(primes)
  print result

if __name__ == '__main__':
  main()
  main2()
  h()