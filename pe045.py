from mytools import *


def t(n):
  return n*(n+1)/2

def p(n):
  return n*(3*n-1)/2

def h(n):
  return n*(2*n-1)

@get_time
@main_start
def main():
  #(TRI_START,PEN_START,HEX_START) = (2, 2, 2) 
  (TRI_START,PEN_START,HEX_START) = (286, 166, 144) 
  MAX = 10**8

  tri_gene = ( t(n) for n in xrange(TRI_START, MAX))
  pen_gene = ( p(n) for n in xrange(PEN_START, MAX))
  hex_gene = ( h(n) for n in xrange(HEX_START, MAX))
  ang_list = [
              {'value': tri_gene.next(), 'gene': tri_gene},
              {'value': pen_gene.next(), 'gene': pen_gene},
              {'value': hex_gene.next(), 'gene': hex_gene}
             ]

  ang_max = max(ang_list[0]['value'], ang_list[1]['value'], ang_list[2]['value']) 
  flag = False  
  while not flag:
    flag = True
    for ang in ang_list:
      if ang['value'] < ang_max:
         ang['value'] = ang['gene'].next()
         flag = False
         if ang['value'] > ang_max:
           ang_max = ang['value']
  print ang_max

main()
