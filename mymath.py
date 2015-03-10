# coding:utf-8
import math
import copy

def pandigital(digit,seq1,seq2=[]):
  iter1 = map(str,seq1)
  if seq2:
    iter2 = map(str,seq2)
  else:
    iter2 = copy.deepcopy(iter1)
  for d in range(digit-1):
    iter1 = (x+y for x in iter1 for y in iter2 if not (y in x))
  return iter1

def get_prime_boolean(max):
    bool = [False,False]+[True]*(max-1)
    # 2‚Ì”{”‚ğFalse‚É
    bool[4::2] = [False] * (len(bool[4::2]))
    p = 3
    p_max = int(math.sqrt(max))+1
    while p<=p_max:
        if bool[p]:
          bool[p**2::p] = [False] * (len(bool[p**2::p]))
        p+=2
    return bool

def get_prime_list(bool):
    length = len(bool)
    return [i for i in range(2,length) if bool[i]]

def prime_generator(max):
    bool = get_prime_boolean(max)
    length = len(bool)
    return (i for i in range(2,length) if bool[i])

def get_primes(max):
    bool = get_prime_boolean(max)
    list = get_prime_list(bool)
    return {'bool':bool,'list':list}
    
def is_prime(num,pri):
  num = int(num)
  if num < len(pri['bool']):
    return pri['bool'][num]

  M = (num**0.5)+1
  #print num
  for p in pri['list']:
    if p > M:
      return True
    if (num % p) == 0:
      return False

  p = pri['list'][-1]+2
  while p<M:
    if (num % p) == 0:
      return False
    p += 2
  return True

def factor(num,pri):
    ret=[]
    max = int(math.sqrt(num))
    if num < len(pri['bool']) and pri['bool'][num]:
        return [num]
    for p in pri['list']:
        while not num % p:
            ret.append(p)
            num //= p
    if num>=2:
        ret.append(num)
    ret.sort()
    return ret

def factor_dict(num,pri):
    fct_list = factor(num,pri)
    fct_dict = {}
    for i in set(fct_list):
        fct_dict[i] = fct_list.count(i)
    return fct_dict

def sum_factors(num,pri):
    if num == 0:
      return 0
    fct_dict = factor_dict(num,pri)
    ans = 1
    for k,v in fct_dict.items():
        ans *= (k ** (v+1) - 1) / (k-1)
    return ans

def get_number_of_factor(num,pri):
    d = factor_dict(num,pri)
    ans = 1
    for v in d.values():
        ans *= v+1
    return ans

def lcm_dict(num1,num2):
    ret = {}
    ret.update(num1)
    for k in num2.keys():
        if k in num1 and num1[k] < num2[k]:
            ret[k] = num2[k]
        elif not k in num1:
            ret[k] = num2[k]
    return ret

def gcd(m,n):
  while n != 0:
    (m,n) = (n,m%n)
  return m

def lcm(m,n):
  return m*n/gcd(m,n)

def circle(num):
  s = str(num)
  for c in range(len(s)):
    s = s[1:]+s[0]
    yield int(s)

def factor_seq(max):
  ret = [[0]]
  for i in range(max):
    ret += [[1]]
  seq = range(max+1)
  for i in seq[2:max//2+1]:
    for j in seq[i*2::i]:
      ret[j] += [i]
  return ret

def factor_sum_seq(max):
  ret = [0]  + [1] * max
  seq = range(max+1)
  for i in seq[2:max//2+1]:
    for j in seq[i*2::i]:
      ret[j] += i
  return ret

def factor_num_seq(max):
  ret = [0]  + [1] * max
  seq = range(max+1)
  for i in seq[2:max//2+1]:
    for j in seq[i*2::i]:
      ret[j] += 1
  return ret

def dict2num(dict):
  r = 1
  for k in dict.keys():
    r *= k**dict[k]
  return r


def sum_nums(s,l,diff):
    n = (l - s + diff)//diff
    return (n*(s+l))/2

def sum_squars(max):
    return (max*(max+1)*(2*max+1))/6

def chk(output,expected,err_msg):
    if output == expected:
        return True
    else:
        print "output: %s" % output
        print "expected: %s" % expected 
        print err_msg
        return False

def test_get_prime_boolean1():
    input = 24
    output = get_prime_boolean(input)
    expected = [
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False #21 to 24
    ]
    return chk(output, expected, "test_get_prime_boolean1() error")

def test_get_prime_boolean2():
    input = 25
    output = get_prime_boolean(input)
    expected = [
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ]
    return chk(output, expected, "test_get_prime_boolean2() error")

def test_is_prime1():
    input1 = 79428312331
    input2 = get_primes(10**6)
    output = is_prime(input1,input2)
    expected = False
    return chk(output, expected, "test_is_prime1() error")
    
def test_is_prime2():
    input1 = 7220755667
    input2 = get_primes(10**6)
    output = is_prime(input1,input2)
    expected = True
    return chk(output, expected, "test_is_prime2() error")
 
def test_is_prime3():
    input1 = 7942831233787435516541
    input2 = get_primes(10**6)
    output = is_prime(input1,input2)
    expected = False
    return chk(output, expected, "test_is_prime3() error")

def test_is_prime4():
    input1 = 14426687446393
    input2 = get_primes(10**6)
    output = is_prime(input1,input2)
    expected = False
    return chk(output, expected, "test_is_prime4() error")

def test_is_prime5():
    input1 = 24639229
    input2 = get_primes(10**6)
    output = is_prime(input1,input2)
    expected = True
    return chk(output, expected, "test_is_prime5() error")


def test_get_prime_list1():
    input = [
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ]
    output = get_prime_list(input)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    return chk(output, expected, "test_get_prime_list1() error")

def test_get_prime_list2():
    # last number is prime
    input = [
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True #21 to 23
    ]
    output = get_prime_list(input)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    return chk(output, expected, "test_get_prime_list2() error")

def test_get_prime_list3():
    # last number is not prime
    input = [
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False #21 to 22
    ]
    output = get_prime_list(input)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    return chk(output, expected, "test_get_prime_list3() error")

def test_get_primes():
    input = 25
    output = get_primes(input)
    expected = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    return chk(output, expected, "test_get_primes() error")

def test_factor1():
    input1 = 23
    input2 = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    output = factor(input1,input2)
    expected = [23]
    return chk(output, expected, "test_factor1() error")

def test_factor2():
    input1 = 625
    input2 = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    output = factor(input1,input2)
    expected = [5,5,5,5]
    return chk(output, expected, "test_factor2() error")

def test_factor3():
    input1 = 619
    input2 = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    output = factor(input1,input2)
    expected = [619]
    return chk(output, expected, "test_factor3() error")

def test_factor4():
    input1 = 100
    input2 = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    output = factor(input1,input2)
    expected = [2,2,5,5]
    return chk(output, expected, "test_factor4() error")

def test_factor_dict1():
    input1 = 100
    input2 = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    output = factor_dict(input1,input2)
    expected = {2:2,5:2}
    return chk(output, expected, "test_factor_dict1() error")

def test_factor_dict2():
    input1 = 97
    input2 = {'bool':[
        False, #0
        False, True, True, False, True, False, True, False, False, False, #1 to 10
        True, False, True, False, False, False, True, False, True, False, #11 to 20
        False, False, True, False, False #21 to 25
    ],
    'list':[2, 3, 5, 7, 11, 13, 17, 19, 23]}
    output = factor_dict(input1,input2)
    expected = {97:1}
    return chk(output, expected, "test_factor_dict2() error")

def test_lcm_dict():
    input1 = {2:2,3:3}
    input2 = {2:4,5:1}
    output = lcm_dict(input1,input2)
    expected = {2:4,3:3,5:1}
    return chk(output, expected, "test_lcm_dict() error")

def test_time(func,input,name,ok_time):
    import time
    start = time.time()
    func(input)
    end = time.time()
    if end-start <= ok_time:
        print "%s finished in time." % name
        print end-start
        return True
    else:
        print "!!!WARING!!! %s dose not finished in time." % name
        print end-start
        return False

def test_time_get_prime_boolean():
    return test_time(get_prime_boolean,10**6,"get_prime_boolean",0.2)

def tests():
    test_list = [ 
        test_get_prime_boolean1,
        test_get_prime_boolean2,
        test_get_prime_list1,
        test_get_prime_list2,
        test_get_prime_list3,
        test_get_primes,
        test_factor1,
        test_factor2,
        test_factor3,
        test_factor4,
        test_factor_dict1,
        test_factor_dict2,
        test_lcm_dict,
        test_time_get_prime_boolean,
        test_is_prime1,
        test_is_prime2,
        test_is_prime3,
        test_is_prime4,
        test_is_prime5
    ]
    fail = 0
    for test in test_list:
        if not test():
            print test
            fail += 1
    if fail == 0:
        print "All test was successful!"
    else:
        print "%d tests failed!" % fail


if __name__=='__main__': 
    tests()