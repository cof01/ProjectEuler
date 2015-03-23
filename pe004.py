# coding: utf-8
from mytools import get_time

def main():
  (i,j)=(999,999)
  max=1
  
  while i>0:
    while j>0:
      k = i*j
      if k <= max: break
      if str(k)==str(k)[::-1]: max=k
      j -= 1
    (i,j)=(i-1,999)
  print max
  
def while1():
    (i,j)=(999,999)
    max=1

    while i>0:
        while j>0:
            k = i*j
            if k <= max: break
            if str(k)==str(k)[::-1]: max=k
            j -= 1
        (i,j)=(i-1,999)
    #print max
    
def while2():
    (i,j)=(999,999)
    max=1

    while i>0:
        while j>0:
            k = i*j
            if k <= max: break
            if str(k)==str(k)[::-1]: max=k
            j -= 1
        (i,j)=(i-1,i-1) #‚±‚±‚¾‚¯‚ªˆÙ‚È‚éB
    #print max
    
def for1():
    start=999
    max=1
    for i in range(start,0,-1):
        for j in range(i,0,-1):
            k = i*j
            if k <= max: break
            if str(k)==str(k)[::-1]: max=k
    #print max

def for2():
    start=999
    max=1
    L = range(start,0,-1)
    for i in L:
        for j in L[start-i:]:
            k = i*j
            if k <= max: break
            if str(k)==str(k)[::-1]: max=k
    #print max
    
def for3():
    L=range(999,0,-1)
    ans = max([i*j for i in L for j in L[999-i:] if str(i*j) == str(i*j)[::-1]])
    #print ans
    
@get_time
def from999999():
    seed = 999
    max = 999
    min = 99
    ans = 0
    while 1:
        target = seed * 1000 + int(str(seed)[::-1])
        i = max
        while i > min:
            (q, r) =  (target // i, target % i)
            if q > max:
                break
            elif r == 0:
                ans = target
                break
            else:
                i -= 1
        if ans:
            break
        else:
            seed -= 1
    print ans

def erat_approach():
  tl = [False]*(10**6)
  for i in range(800,1000):
    tl[i*800:i*1000:i] = [True]*200
  t = 999
  while 1:
    n = t*1000+int(str(t)[::-1])
    if tl[n]:
      break
    t-=1
  print n
  
if __name__ == '__main__':
  from999999()
  