import mymath
from mytime import exe
import math
def main():
    target = 2 * (10**6)
    pri = mymath.get_primes(target)
    print sum(pri['list'])
 
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

if __name__ == '__main__':
  exe('main()')
  exe('main2()')