def exe(func,num=1):
  from timeit import timeit
  setup = 'from __main__ import ' + func.split('(')[0]
  print "%s: %s %s times" % (func, timeit(func, setup, number=num), num)

def profile(func):
  import cProfile
  cProfile.run(func)