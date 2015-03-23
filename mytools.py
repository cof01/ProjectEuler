import logging
import sys
import time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='log\%s.log' % sys.argv[0],
                    filemode='a')


def input2int(func):
  def wrapper(*args, **kwargs):
    new_args, new_kwargs = [],{}
    for i in range(len(args)):
      new_args.append(int(args[i]))
    for k,v in kwargs.items():
      new_kwargs[k] = int(v)
    func(*new_args, **new_kwargs)
  return wrapper

def input2str(func):
  def wrapper(*args, **kwargs):
    new_args, new_kwargs = [],{}
    for i in range(len(args)):
      new_args.append(str(args[i]))
    for k,v in kwargs.items():
      new_kwargs[k] = str(v)
    func(*new_args, **new_kwargs)
  return wrapper

def debug(func):
  def wrapper(*args, **kwargs):
    logging.debug('%s start. args:%s, kwargs:%s' % (func.__name__, args, kwargs))
    result = func(*args, **kwargs)
    logging.debug('%s finish. result:%s' % (func.__name__, result))
    return result
  return wrapper

def info(func):
  def wrapper(*args, **kwargs):
    logging.info('%s start. args:%s, kwargs:%s' % (func.__name__, args, kwargs))
    result = func(*args, **kwargs)
    logging.info('%s finish. result:%s' % (func.__name__, result))
    return result
  return wrapper

def main_start(func):
  def wrapper(*args, **kwargs):
    logging.info('='*10 + '%s start' % func.__name__ + '='*10)
    logging.info('%s start. args:%s, kwargs:%s' % (func.__name__, args, kwargs))
    result = func(*args, **kwargs)
    logging.info('%s finish. result:%s' % (func.__name__, result))
    logging.info('='*10 + '%s finish' % func.__name__ + '='*10)
    return result
  return wrapper

def get_time(func):
  def wrapper(*args, **kwargs):
    s = time.time()
    result = func(*args,**kwargs)
    e = time.time()
    logging.info('%s %s finish. time:%.5f' % (sys.argv[0], func.__name__, e-s))
    print '%s %s finish. time:%.5f' % (sys.argv[0], func.__name__, e-s)
    return result
  return wrapper
  
if __name__ == '__main__':
  @input2int
  def input2int_test(n, m):
    if not isinstance(n, int):
      print 'n is not int'
      raise
    elif not isinstance(m, int):
      print 'm is not int'
      raise
    print n,m
      
  @input2str
  def input2str_test(n, m):
    if not isinstance(n, str):
      print 'n is not str'
      raise
    elif not isinstance(m, str):
      print 'm is not str'
      raise
    print n,m
      
  @debug
  def debug_test(n, m):
    print n,m

  @info
  def info_test(n, m):
    print n,m
  
  @main_start
  def main_start_test(n, m):
    print n,m
 
  @get_time
  def get_time_test(n, m):
    for i in range(int(n)):
      print n,m

  input2int_test('100', m='200')
  input2int_test(100, m=200)
  input2str_test('100', m='200')
  input2str_test(100, m=200)
  debug_test('100', m='200')
  info_test('100', m='200')
  main_start_test('100', m='200')
  get_time_test('100', m='200')