from mytools import debug, get_time, main_start

def make_figuraters(gene):
  ret = {}
  for i in gene:
    if str(i)[:2] == '82':
      print 82,str(i)[2:]
    if str(i)[:2] in ret:
      ret[str(i)[:2]].append(str(i)[2:])
    else:
      ret[str(i)[:2]] = [str(i)[2:]]
  return ret
  
def make_generator(func, start, stop):
  return (func(i) for i in range(stop) if start <= func(i) < stop)

def exist_cyclical(highest_digits,upper_digits, angulars):
  ret = []
  if len(angulars) == 1:
    if upper_digits in angulars[0]:
      for under_digits  in angulars[0][upper_digits]:
        if under_digits == highest_digits:
          return [highest_digits, upper_digits, under_digits]
    return ret

  for i in range(len(angulars)):
    if not(upper_digits in angulars[i]):
      continue
    for under_digits in angulars[i][upper_digits]:
      if i == len(angulars)-1:
        ret = exist_cyclical(highest_digits, under_digits, angulars[:i])
      else:
        ret = exist_cyclical(highest_digits, under_digits, angulars[:i]+angulars[i+1:])
      if ret:
        ret.insert(1,upper_digits)
    if ret:
      break
  return ret

def tri(n): return n*(n+1)/2
def squ(n): return n**2
def pen(n): return n*(3*n-1)/2
def hex(n): return n*(2*n-1)
def hep(n): return n*(5*n-3)/2
def oct(n): return n*(3*n-2)

@get_time
def main():
  start, stop = 1000, 10000
  func_list = [tri, squ, pen, hex, hep, oct]
  angulars = []
  for func in func_list:
    angulars.append(make_figuraters(make_generator(func,start,stop)))
  ans = []
  for upper_digits in angulars[0]:
    for under_digits in angulars[0][upper_digits]:
      ans =  exist_cyclical(upper_digits,under_digits,angulars[1:])
      if ans:
        break
    if ans:
      break

  upper_digits = ans.pop(0)
  ret = []
  while ans:
    under_digits = ans.pop(0)
    ret.append(int(upper_digits + under_digits))
    upper_digits = under_digits
  
  return sum(ret)


print main()