# -*- coding: utf-8 -*-
from mytools import get_time

def getdays(month, year):
  if month in [1,3,5,7,8,10,12]:
    return 31
  elif month in [4,6,9,11]:
    return 30
  elif year%400 == 0:
    return 29
  elif year%100 == 0:
    return 28
  elif year%4 == 0:
    return 29
  else:
    return 28

def nextdate(date, month, year):
   return (date + getdays(month, year)) % 7

def nextmonth(month, year):
   if month == 12:
      #12���ł���Ύ��̔N��
      return (1, year+1)
   else:
      return (month+1, year)

@get_time
def main():
  STARTYEAR = 1901
  LASTYEAR = 2000
  (date, month, year) = (1, 1, 1900)
  ans = 0

  while year <= LASTYEAR:

    #�O����date,month,year���玟����date(�j��)���擾
    date = nextdate(date, month, year)

    #month, year���C���N�������g
    (month,year) = nextmonth(month, year)

    #year���͈͓���date��0(���j��)�Ȃ�ans��1��������B
    if STARTYEAR <= year <= LASTYEAR and date == 0:
      ans += 1

  print ans

main()