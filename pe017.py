from mytools import get_time

def get_x(num):
  x=num%10
  L1 = ['', 'one','two','three','four','five','six','seven','eight','nine']
  return L1[x]

def get_xx(num):
  L2 = ['']*10+['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
  L3 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

  xx = num % 100
  if xx < 10:
    return get_x(xx)
  elif xx < 20:
    return L2[xx]
  else:
    return L3[xx//10] + get_x(xx)

def get_xxx(num):
  xxx = num//100
  xx = num%100

  if xxx:
    if xx:
      return get_x(xxx)+'hundredand'+get_xx(xx)
    else:
      return get_x(xxx)+'hundred'
  else:
    return get_xx(xx)

def get_xxxx(num):
  if num == 1000:
    return 'onethousand'
  else:
    return get_xxx(num)

@get_time
def main():
  s = ''
  for i in range(1,1001):
    s += get_xxxx(i)
  print len(s)

main()