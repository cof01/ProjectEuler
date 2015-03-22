from mytools import get_time,main_start,debug

def encrypt(target,key):
  return ord(target) ^ ord(key)

def decrypt(target,key):
  d = target ^ key
  #if d != 32 and d != 44 and d != 46 and ( d < 65 or 90 < d < 97 or d >122):
  #  return 0
  black_list = [34,37,38,42,92,96]
  if d in black_list :
    return 0
  return d

def try_decrypt(target_list,k):
   ans = 0
   ret = []
   for i in range(len(target_list)):
      d = decrypt(target_list[i], k[i%len(k)])
      #print target_list[i], d , k
      if d:
        ans += d
        ret.append(chr(d))
      else:
        ans, ret = 0, []
        break
   return ans, ret

@get_time
def main():
  start, finish = 97, 122
  keys = [ [i, j, k] for i in range(start, finish) for j in range(start, finish) for k in range(start, finish)]

  f = open('p059_cipher.txt')
  target_list = map(int, f.read().split(','))
  f.close()
  for k in keys:
    ans, ret = try_decrypt(target_list,k)
    
    if ans :
      break
  return ans,''.join(ret)
  
print main()
