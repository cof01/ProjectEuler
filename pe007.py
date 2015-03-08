import mymath
from mytime import exe
def main():
  max = 10**6
  target = 10001
  pri = mymath.get_primes(max)
  print pri['list'][target-1]

if __name__ == '__main__':
  exe('main()')