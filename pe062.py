from mytools import get_time,main_start,debug

@get_time
def main():
  #SEARCH_NUMBER = 3
  SEARCH_NUMBER = 5
  seed, ans = 1, 0
  digits_dict = {}
  while True:
    cubic = seed ** 3
    sorted_number = ''.join(sorted(list(str(cubic))))
    if sorted_number in digits_dict:
      digits_dict[sorted_number].append(cubic)
      if len(digits_dict[sorted_number]) == SEARCH_NUMBER:
        ans = digits_dict[sorted_number][0]
        break
    else:
      digits_dict[sorted_number] = [cubic]
    seed += 1
  
  return ans


print main()