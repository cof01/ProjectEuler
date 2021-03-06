from mytools import get_time

@get_time
def main():
  (v1, v2) = (1, 2)
  max = 4 * (10**6)
  s = 0
  while v2<=max:
    if not v2 % 2: s += v2
    (v1, v2) = (v2, v1+v2)
  print s

@get_time
def main2():
  (v1, v2) = (1, 2)
  max = 4 * (10**6)
  s = 0
  while v2 <= max:
    s += v2
    (v1, v2) = (v1+2*v2, 2*v1+3*v2)
  print s

if __name__ == '__main__':
  main()
  main2()