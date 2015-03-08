import mymath
from mytime import exe

def main():
  (s,l,diff) = (1,100,1)
  ans = (mymath.sum_nums(s,l,diff)**2) - mymath.sum_squars(l)
  print ans

if __name__ == '__main__':
  exe('main()')