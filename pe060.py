from itertools import permutations,combinations
from mytools import get_time, main_start, debug
from mymath import get_primes, make_is_prime, get_prime_boolean

#@debug



@main_start
@get_time
def main():
  MAX, P_MAX = 10**4, 10**8
  pri = get_primes(MAX)
  
  def pair_of_prime(p_max):
    prime_boolean = get_prime_boolean(p_max)
    def is_pair_of_prime(pri_list, r):
      for pair in permutations(pri_list,r ):
        if not prime_boolean[int(''.join(map(str,pair)))]:
          return False
      return True
    return is_pair_of_prime
    
  is_pair_of_prime = pair_of_prime(P_MAX)
  
  ans = 10**10
  comb1 = map(lambda x: [x], [3] + pri['list'][3:])
  for i in range(2,6):
    comb2 = []
    for p in [3] + pri['list'][3:]:
      for comb in comb1:
        if comb[-1] > p:
          break
          
        all_prime = True
        for c in comb:
          if not is_pair_of_prime([c,p],2):
            all_prime = False
            break
            
        if all_prime:
          comb2.append(comb+[p])
          if i == 5:
            s = sum(comb) + p
            if ans > s:
              ans = s
    comb1 = comb2
  return ans

print main()