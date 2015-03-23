from mytools import get_time
def next(n):
  if n % 2:
    return n*3 + 1
  else:
    return n / 2

def add(dict,n1):
  n2 = next(n1)
  if not n2 in dict:
    dict = add(dict,n2)
  dict[n1] = dict[n2]+1
  return dict

@get_time
def main():
  dict = {1:1}
  (max_i,max) = (1,1)
  for i in range(2,10**6):
    if not i in dict:
      dict = add(dict,i)
    if dict[i] > max:
      (max_i,max) = (i,dict[i])
  print  (max_i,max)

main()