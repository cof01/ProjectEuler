import mymath

def twenty_eight(i,factors):
  seq = [0] + [1] * (i-1)
  for f in factors:
    if f == 1:
      continue
    seq[f::f] = [0]*(i/f-1)
  #print i, sum(seq)
  return sum(seq)


def main(target=10**6):
  ans, rate_max = 0, 0
  fact_seq = mymath.factor_seq(target)
  for i, factors in enumerate(fact_seq):
    if i < 2: 
      continue
    n = twenty_eight(i,factors)
    if i / float(n) > rate_max:
      #print i, float(n), i / float(n), rate_max
      rate_max = i / float(n)
      ans = i
    if  (i % 10**4) == 0:
      print i
  return ans

def totyent(i):
  ret = 0
  for n in range(1,i):
    if mymath.gcd(i,n) == 1:
      ret += 1
  #print i, ret
  return ret

def main2(target=10**6):
  ans, rate_max = 0, 0
  for i in range(2,target+1):
    i_rate = i / float(totyent(i))
    if i_rate > rate_max:
       rate_max = i_rate
       ans = i
    if  (i % 10**4) == 0:
      print i
  return ans
  
def noncoprime(max):
  ret = [set([0])]
  for i in range(max):
    ret += [set([1])]
  seq = range(max+1)
  for i in seq[2:max+1]:
    print i
    ret[i] |= set([i])
    for p in ret[i]:
      if p == 1:
        continue
      for k in seq[i+p::p]:
        ret[k] |= set([i])
  return ret

def main3(target=10**6):
  ans, rate_max = 0, 0
  noncoprime_list = noncoprime(target)
  for i, cp in enumerate(noncoprime_list):
    if i < 2:
      continue
    i_rate = i / float(i - len(cp) + 1)
    print i, i - len(cp) + 1, i_rate, noncoprime_list[i]
    if i_rate > rate_max:
      ans, rate_max = i, i_rate
  return ans

import itertools

def totyent2(i,factors):
  length = len(factors)
  ans = i 
  for n in range(1,length+1):
    if length == 1:
      ans -= 1
      break
    for s in itertools.combinations(factors[1:],n):
      c = reduce(lambda x,y:x*y, s)

      ans += (i/c)  * ( (-1)**n )
      #print i, c, i/c, ans, (-1)**n
  return ans

def list_up_factors(max):
  ret = [[0]]
  for i in range(max):
    ret += [[1]]
  seq = range(max+1)
  for i in seq[2:max//2+1]:
    if len(ret[i]) > 1:
      continue
    for j in seq[i*2::i]:
      ret[j] += [i]
  return ret

def main4(target=10**6):
  ans, rate_max = 0, 0
  factors = list_up_factors(target)
  for i, fs in enumerate(factors):
    if i < 2:
      continue
    t = totyent2(i,fs)
    i_rate = i / float(t)
    if (i % 10**4) == 0:
      print i, t , i_rate, factors[i]
    if i_rate > rate_max:
      ans, rate_max = i, i_rate
  return ans
print main4()
