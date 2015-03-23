import mymath
from mytools import get_time

@get_time
def cof():
  pri = mymath.get_primes(10**4)
  n = 1
  num_fac = 1
  lim = 500
  n1_fac =  mymath.get_number_of_factor(n,pri)
  while num_fac < lim:
    n += 1
    if (n+1)%2:
      n2_fac =  mymath.get_number_of_factor(n+1,pri)
    else:
      n2_fac =  mymath.get_number_of_factor((n+1)/2,pri)
    num_fac = n1_fac * n2_fac
    n1_fac = n2_fac
  print n * (n+1) / 2

def factor_seq(max):
  ret = [[0]]
  for i in range(max):
    ret += [[1]]
  seq = range(max+1)
  for i in seq[2:max//2+1]:
    for j in seq[i*2::i]:
      ret[j] += [i]
  return ret

@get_time
def cof2():
  fq = factor_seq(10**5)
  n = 1
  num_fac = 1
  lim = 500
  n1_fac = len(fq[n])
  while num_fac < lim:
    n += 1
    if (n+1)%2:
      n2_fac =  len(fq[n+1])
    else:
      n2_fac =  len(fq[(n+1)/2])
    num_fac = n1_fac * n2_fac
    n1_fac = n2_fac
  print n * (n+1) / 2



cof()
cof2()
