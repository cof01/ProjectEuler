import itertools

def is_first_smallest(num_list):
  for n in num_list[1:]:
    if n < num_list[0]:
      return False
  return True
    
def has_same_sum(first,second):
  first_len = len(first)
  s1 = first[0] + second[0] + second[1]
  flag = True
  for i in range(1,first_len):
    if i == first_len -1 :
      s2 = first[i] + second[i] + second[0]
    else:
      s2 = first[i] + second[i] + second[i+1]
    if s1 != s2:
      flag = False
      break
  return flag

def get_num(first,second):
  first_len = len(first)
  ret = ''
  for i in range(0,first_len):
    if i == first_len - 1:
      ret += str(first[i]+1) + str(second[i]+1) + str(second[0]+1)
    else:
      ret += str(first[i]+1) + str(second[i]+1) + str(second[i+1]+1)
  return ret

def main(target=10,dg=16):
  target_set = set(range(0,target))
  limit,ans = target / 2, 0
  for p in itertools.permutations(target_set,limit):
    if not is_first_smallest(p):
      continue
    rest_set = target_set - set(p)
    for r in itertools.permutations(rest_set):
      if has_same_sum(p,r):
        n = int(get_num(p,r))
        if n > ans and len(str(n))==dg:
          ans = n
  return ans
  
print main(10,16)
