import mymath
import re
from mytools import get_time
class Number:
  def __init__(self, number):
    self.number = str(number)
    self.info = {}

  def has_digit_row(self,digit_row):
    self.info[digit_row] ={}
    p = re.compile('(\d*)(%s)(\d+)' % digit_row)
    self.info[digit_row]['match'] = p.match(str(self.number))
    return self.info[digit_row]['match']

  def has_key(self,key):
    p = re.compile(key)
    return p.match(self.number)

  def separate_number(self,digit_row):
    if digit_row in self.info:
      m = self.info[digit_row]['match']
    else:
      m = self.has_digit_row(digit_row)
    if m:
      self.info[digit_row]['group'] = m.group(1,2,3)
      return self.info[digit_row]['group']
    else:
      return None

  def get_separatenumbers(self,digit_row):
    return self.info[digit_row]['group']

  def has_separate_number(self,digit_row, separate_number ,position):
    if self.self.info[digit_row]['group'] and position < len(self.group):
      return self.self.info[digit_row]['group'][position] == separate_number
    else:
      raise

class Group:
  def __init__(self,name=''):
    self.name = name
    self.member = {}

  def add(self,name,member):
    self.member[name] = member

  def get(self,name):
    return self.member[name]

  def __iter__(self):
    return ((k,v) for k,v in self.member.items())

def first_extract(pri):
  gm1 = Group('groupmanager1')
  for i in range(0,3):
    group_name = str(i)+str(i)+str(i)
    gm1.add(group_name,Group(group_name))
     
  for prime in pri['list']:
    prime_object = Number(prime)
    for group_name, group_object in gm1:
      if prime_object.separate_number(group_name):
        group_object.add(prime,prime_object)
  return gm1

def second_extract(gm1):
  gm2 = Group('groupmanager2')
  for groupname1,group1 in gm1:
    if not(groupname1 in set(['11','22','33'])):
      continue
    for membername1, member1 in group1:
      second_key, none, third_key = member1.get_separatenumbers(groupname1) 
      key = '%s\d\d+%s' % (second_key,third_key)
      g = Group(key)
      g.add(membername1,member1)
      for groupname2,group2 in gm1:
        for membername2, member2 in group2:
          if member2.has_key(key):
            g.add(membername2, member2)
      gm2.add(key,g)
  
  return gm2
  
@get_time
def main():
  MAX = 10**6
  pri = mymath.get_primes(MAX)
  gm1 = first_extract(pri)
  
  for k,v in gm1:
    print pri['bool'][v.number.replace(k.name,'333')]
  
  #gm2 = second_extract(gm1)

  
  #for k,v in gm2:
  #  print k,v
def replacable(p,pri,replace_before):
  p = str(p)
  seq = [str(i)*3  for i in range(0,10)]
  c = 0
  for replace_after in seq:
        p_after = p[0]+p[1:].replace(replace_before,replace_after)
        print p, replace_before, p_after, replace_after, pri['bool'][int(p_after)]
        #print p, replace_before, p_after, replace_after
        if p_after != p and pri['bool'][int(p_after)] and len(str(int(p_after)))== len(p):
          print p
          c += 1
          if c == 7:
            return True
  return False


def has_threerowdigits(p,re_list):
  p = str(p)
  for number, pattern in re_list.items():  
    m = pattern.match(p)
    if m :
      return number
  return False

def main2():
  MAX = (10**7)*5
  pri = mymath.get_primes(MAX)
  re_list = {str(i)*3:re.compile("(\d+)(%s)(\d+)" % (str(i)*3)) for i in range(0,2)}
  seq = [str(i)*3  for i in range(0,10)]
  ans = 0
  for p in pri['list']:
    number = has_threerowdigits(p,re_list)
    if not number :
      continue
    if replacable(p,pri,number):
      ans = p
      break
  print ans

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

def replacable2(prime,num,pri):
  prime = str(prime)
  num1 = str(num)
  c = 0
  if prime[:-1].count(num1) < 3:
    return 0
  c += 1
  for num2 in range(num+1,10):
    if is_prime(int(prime[:-1].replace(num1,str(num2))+prime[-1]),pri):
      c += 1
  return c

@get_time
def main3():
  PRIMEMAX = (10**7)*5
  PRI = mymath.get_primes(PRIMEMAX)
  NUM_LIST = range(3)
  ans = 0
  for prime in PRI['list']:
    for num in NUM_LIST:
      c = replacable2(prime,num,PRI)
      if c >= 8:
        ans = prime
        break
    if ans:
      break
  print ans

main3()
          

