from mytime import exe
from mytools import get_time
import mymath

@get_time
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


def p(n):
    L = [0,0]+[1]*(n-1)
    i = 2
    while i*i<=n:
        while not L[i]: i += 1
        for j in xrange(i+i, n+1, i): L[j] = 0
        i += 1
    return [i for i in xrange(n+1) if L[i]]
 
def f(n):
    P = p(n)
    i, s, t = 0, 0, 0
    while s<n: i, s = i+1, s+P[i]
    for j in xrange(i):
        if i-j<t: break
        for k in xrange(i-1, j, -1):
            if k-j<t: break
            L = P[j:k+1]
            if sum(L) in P: M, t = L, len(L)
    return M

  
main()