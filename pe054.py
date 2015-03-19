class Card:
  Numbers = {'A':14,'T':10,'J':11,'Q':12,'K':13}
  
  def __init__(self, number, mark):
    if number in self.Numbers:
      self.number = self.Numbers[number]
    else:
      self.number = int(number)
    self.mark = mark
    
  def __cmp__(self,other):
    if self.number > other.number:
      return 1
    elif self.number < other.number:
      return -1
    else:
      return 0
      

class Hand:
  def __init__(self, cards):
    self.cards = sorted(cards)
    self.related = []
    self.nonrelated = []
    
  def is_one_pair(self):
    