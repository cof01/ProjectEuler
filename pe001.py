from mytools import get_time
@get_time
def main():
  print sum([i for i in range(1,1000) if i%3*i%5==0])

@get_time
def main2():
  print sum(set(range(3,1000,3)+range(5,1000,5)))
  
main()
main2()
