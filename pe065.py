from fractions import Fraction

def seeds(s):
  for n in range(s,0,-1):
    if (n % 3) == 2:
      yield ( ( n / 3 ) + 1 ) * 2
    else:
      yield 1
  raise StopIteration
  
def get_continued_fraction(base,seeds):
  ret = next(seeds)
  for s in seeds:
    ret = s + Fraction(1,ret)
    #print "%s: %s" % (s, ret)
  return base + Fraction(1,ret)

def add_func(a,b):
  return int(a)+int(b)
  
def main(target=100-1):
  return reduce(add_func, str(get_continued_fraction(2,seeds(target)).numerator))
  
#for i in range(1,10):
#  print "%d: %s" % (i, main(i))

print main()
  
