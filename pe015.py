from mytools import get_time
def f(L,a,b):
  if not L[a][b]:
    if a == len(L)-1 or b == len(L)-1:
      L[a][b] = 1
    else:
      L[a][b] = f(L,a+1,b) + f(L,a,b+1)
  return L[a][b]
  
@get_time
def main():
  #(x,y) = (2,2)
  (x,y) = (20,20)
  L = [[0 for i in range(0,y+1)] for j in range(0,x+1)]
  ans = f(L,0,0)
  print ans

def g(L,a,b):
  if a == 0:
    return 1
  elif a == b:
    return L[a-1][b]*2
  else:
    return L[a-1][b]+L[a][b-1]

@get_time
def main2():
  seq = range(21)
  L = [[0 for i in seq] for j in seq]

  for a in seq:
    for b in seq[a:]:
      L[a][b] = g(L,a,b)
  print L[20][20]
  
main()
main2()