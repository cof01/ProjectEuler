from mytools import debug, get_time, main_start

def make_figuraters(gene):
  ret = {}
  for i in gene:
    if str(i)[:2] in ret:
      ret[str(i)[:2]].append(str(i)[2:])
    else:
      ret[str(i)[:2]] = [str(i)[2:]]
    print i, str(i)[:2], ret[str(i)[:2]]
  return ret
  
def make_generator(func, start, stop):
  return (func(i) for i in range(stop) if start < func(i) < stop)

def exist_cyclical(number1, dict_list,k):
  if number1 in dict_list[0]:
    for number2 in dict_list[0][number1]:
      #print number1, number2, 
      if len(dict_list) == 1 and number2 == k:
        print number1+number2, 
        return int(number1+number2)
      elif len(dict_list) == 1:
        continue
      else:
        s = exist_cyclical(number2, dict_list[1:],k)
        if s:
          print number1+number2, 
          return int(number1+number2) + s
  return 0

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
  numbers = []
  for func in func_list:
    numbers.append(make_figuraters(make_generator(func,start,stop)))
  ans = 0
  for k,v_list in numbers[0].items():
    for v in v_list:
      #print k,v, 
      s = exist_cyclical(v,numbers[1:],k)
      #print 
      if s:
        ans = s + int(k+v)
        print k+v
        break
    if ans:
      break
  return ans
print main()