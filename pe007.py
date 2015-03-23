import mymath
from mytools import get_time

@get_time
def main():
  max = 10**6
  target = 10001
  pri = mymath.get_primes(max)
  print pri['list'][target-1]

if __name__ == '__main__':
  main()