def sort_number(n):
  return ''.join(sorted(list(str(n))))

def has_same_multiple(n, multi):
  s_n = sort_number(n)
  for i in range(2,multi+1):
    if s_n != sort_number(n*i):
      return False
  return True

def main():
  START, STOP, CONDITION = 1, 10**6, 6
  ans = 0
  for n in range(START,STOP):
    if has_same_multiple(n,CONDITION):
      ans = n
      break
  print ans
  
import time
s = time.time()
main()
print time.time() -s
