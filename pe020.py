from mytools import get_time

@get_time
def main():
  n = 1
  for i in range(1,101): n*=i   
  ans = sum(map(int, str(n)))
  print ans

main()