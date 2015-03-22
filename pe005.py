# coding: utf-8
from mymath import lcm
import mymath
from mytime import exe

def main():
  max = 20
  i = 6
  for j in range(5,max+1):
    i = lcm(i,j)
  print i


def main2():
  max = 20
  pri = mymath.get_primes(max)
  num1 = mymath.factor_dict(2,pri)
  for i in range(3,max+1):
    num2 = mymath.factor_dict(i,pri)
    num1 = mymath.lcm_dict(num1,num2)
  ans = mymath.dict2num(num1)
  #print ans
  
def main3():
  max = 20
  #20‚Ü‚Å‚Ì‘f”—ñ‚ğ¶¬
  pri = mymath.get_primes(max)
  ans = 1
  j=1
  i=-1
  while i!=0:
    i=0
    #‘f”‚»‚ê‚¼‚ê‚ğA‚»‚Ì—İæ”‚ªmax‚ğ’´‚¦‚È‚¢”ÍˆÍ‚Å“š‚¦‚ÉŠ|‚¯‡‚í‚¹‚é
    while i < len(pri['list']) and pri['list'][i]**j <= max:
      ans *= pri['list'][i]
      i+=1
    j+=1

  #print ans 
  
if __name__ == '__main__':
  num = 10000
  main()