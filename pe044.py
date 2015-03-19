from mytools import *

@main_start
@get_time
def pe44():
  start, stop = 1, 10**8
  pen = ((n * ( 3*n - 1))//2 for n in xrange(start, stop))
  p_list, p_set = [], set([])
  ans = 10**10
  i = 0
  append = p_list.append
  add = p_set.add
  while 1:
    append(pen.next())
    append(pen.next())
    add(p_list[2*i])
    add(p_list[2*i+1])
    
    d = search(p_list[i],p_list[:i+1],p_set)
    if d:
      min_d = min(d)
      if min_d < ans:
        found_answer(min_d)
        ans = min_d
    if ans < p_list[i+1] - p_list[i]:
      break
    i+=1
  return ans

def found_answer(n):
  print n

#@debug
def search(p1,p_list,p_set):
  d = []
  for p2 in p_list:
    if (p1+p2 in p_set) and (p1-p2 in p_set):
    #if (p1+p2 in p_list) and (p1-p2 in p_list):
      d.append(p1-p2)
  return d

pe44()