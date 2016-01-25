from mytools import get_time
import mymath
@get_time
def main(target=5000):
  sum_comb = {}
  pri = mymath.get_primes(10**6)

  def count_sum_comb(x,imax):
    if x == 0 or x == 2 or (x == 3 and imax==3):
      return 1
    if x <= 3:
      return 0
    key_x = "%d-%d" % (x,imax)
    if key_x in sum_comb:
      return sum_comb[key_x]
    c = 0
    for i in (i for i in range(2,imax+1) if pri['bool'][i]):
      c += count_sum_comb(x-i,min(x-i,i))
      #print x,imax,i,c
    sum_comb[key_x] = c
    return c

  x = 1
  while count_sum_comb(x,x) < target: x+=1
  print x, count_sum_comb(x,x), x-1, count_sum_comb(x-1,x-1)
  return x
print main()
