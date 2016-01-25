class Num:
  def __init__(self,num):
    self.num = num
    self.former = []
    self.later = []
    
  def set_former(self,former):
    if former in self.former:
      pass
    else:
      self.former.append(former)
      
  def set_later(self,later):
    if later in self.later:
      pass
    else:
      self.later.append(later)
      
  def get_former(self):
    for f in self.former:
      yield f
      
  def get_later(self):
    for l in self.later:
      yield l
      
  def has_former(self):
    return len(self.former)
    
  def has_later(self):
    return len(self.later)

class Nums:
  def __init__(self):
    self.nums = {}
    
  def set(self,num):
    if num in self.nums:
      pass
    else:
      self.nums[num] = Num(num)
    return self.get(num)
    
  def get(self,num):
    return self.nums[num]
    
  def read_numstring(self,numstring):
    former = None
    for ns in map(lambda x:int(x), numstring):
      corrent = self.set(ns)
      if former:
        corrent.set_former(former)
        former.set_later(corrent)
      former = corrent
      
  def who_is_fastest(self):
    for num in self.nums.values():
      if not num.has_former():
        return num
      

def readlinefromfile(file):
  f = open(file)
  lines = map(lambda x: x.replace('\n',''), f.readlines())
  f.close()
  for line in lines:
    yield line


def get_longest(num):
  ret = []
  for later in num.get_later():
    later_list = get_longest(later)
    if len(later_list) > len(ret):
      ret = later_list
  return [num] + ret


def main():
  File = 'p079_keylog.txt'
  nums = Nums()
  for line in readlinefromfile(File):
    nums.read_numstring(line)
  longest_list = get_longest(nums.who_is_fastest())
  ans = ''
  for num in longest_list:
    ans += str(num.num)
  return ans


print main()
