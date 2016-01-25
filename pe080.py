import math
from mytools import get_time
def divid_by_two(x,d):
  y = []
  i = 0
  x_int, x_float = int(x), x - int(x)
  while x_int != 0 and i < (d//2):
    y.append(x_int % 100)
    x_int = (x_int / 100)
    i += 1
    y.reverse()
  while i < d:
    x_float *= 100
    y.append(int(x_float) % 100)
    x_float = x_float - int(x_float) 
    i += 1
  for z in y:
    yield z

def get_divid(divided,support):
  divid = 9
  while divided < (support*10 +  divid) *  divid:  divid -= 1
  return divid

def extraction_of_square_root(x,d):
  support = 0
  divided = 0
  ret = ''
  for t in divid_by_two(x,d):
    divided = divided * 100 + t
    divid = get_divid(divided,support)
    support = support * 10 + divid
    ret += str(divid)
    divided -= support*divid
    support += divid

  return ret
@get_time
def main(target=100,d=100):
  return sum(reduce(lambda x,y:int(x)+int(y), extraction_of_square_root(n,d)) for n in range(1,target+1) if int(math.sqrt(n))**2 != n)

print main()
