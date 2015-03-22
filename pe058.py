from mymath import make_is_prime
from mytools import get_time, main_start

@main_start
@get_time
def main():
  UNIT = 10**7
  is_prime = make_is_prime(UNIT)
  ans = 0
  primes, numbers = 0, 1
  i = 1
  length = i*2 + 1
  while ans == 0:
    numbers += 4
    primes += is_prime(length**2 - i*2) + is_prime(length**2 - i*4) + is_prime(length**2 - i*6)
    #print length**2 , (float(primes) / numbers), length**2 - i*2, length**2 - i*4, length**2 - i*6
    if (float(primes) / numbers) < 0.1:
      ans = length
      break
    i+=1
    length = i*2 + 1
  return ans

print main()
      
       