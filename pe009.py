def cof2():
  target=1000
  sq = [x**2 for x in range(0,target)] #create 
  (a,b,c) = (1, 1, target - 2)
  ans = 0
  while a < c:
    while b < c:
      if sq[a] + sq[b] == sq[c]:
        ans = a*b*c
        break
      (b,c) = (b + 1, c - 1)
    if ans:
      break
    else:
      (a,b,c) = (a + 1, a + 1, target - a*2 -2)
  print ans
  
cof2()