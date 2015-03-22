from mytools import *

class LychrelNumber(Exception):
  pass

@debug
def is_kaibun(s):
  return str(s) == str(s)[::-1]

operation_number = {}
#@debug
def how_many_operations(n, o):
  n, s = int(n), int(n) + int(str(n)[::-1])
  if is_kaibun(s):
    operation_number[n] = 1
  elif o + 1 > 50:
    operation_number[n] = -1
    raise LychrelNumber
  else:
    if s in operation_number:
      if operation_number[s] == -1:
        operation_number[n] = -1
        raise LychrelNumber
      else:
        operation_number[n] = operation_number[s] + 1
    else:
      operation_number[n] = 1 + how_many_operations(s, o+1)
  return operation_number[n]

#@main_start
@get_time
def main():
  SEARCH_MAX = 10**4
  ans = 0
  for i in range(SEARCH_MAX):
    try:
      how_many_operations(i, 1)
    except LychrelNumber:
      ans += 1
  return ans


print main()