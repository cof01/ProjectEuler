class Card:
  Values = {'A':14,'T':10,'J':11,'Q':12,'K':13}

  def __init__(self, value, suit):
    if value in self.Values:
      self.value = self.Values[value]
    else:
      self.value = int(value)
    self.suit = suit

  def __cmp__(self,other):
    return self.value - other.value

class Hand:
  Ranks = {
           'High Card'      : 1,  #Highest value card.
           'One Pair'       : 2,  #Two cards of the same value.
           'Two Pairs'      : 3,  #Two different pairs.
           'Three of a Kind': 4,  #Three cards of the same value.
           'Straight'       : 5,  #All cards are consecutive values.
           'Flush'          : 6,  #All cards of the same suit.
           'Full House'     : 7,  #Three of a kind and a pair.
           'Four of a Kind' : 8,  #Four cards of the same value.
           'Straight Flush' : 9,  #All cards are consecutive values of same suit.
           'Royal Flush'    : 10  #Ten, Jack, Queen, King, Ace, in same suit.
           }

  def __init__(self):
    self.cards = []
    self.rank = 0
    self.card4 = []
    self.card3 = []
    self.card2 = []
    self.card1 = []
    self.straight = True
    self.flush = True
  
  def add_card(self, card):
    self.cards.append(card)

  def _of_a_kind(self,value, a_kind):
    if a_kind == 4:
      self.card4.append(value)
    elif a_kind == 3:
      self.card3.append(value)
    elif a_kind == 2:
      self.card2.append(value)
    else:
      self.card1.append(value)

  def analyze(self):
    cards = sorted(self.cards)
    first_suit, first_value = cards[0].suit, cards[0].value
    current_value = first_value
    a_kind = 1

    for i in range(1, len(cards)):
      if first_suit != cards[i].suit:
        self.flush = False

      if first_value + i != cards[i].value:
        self.straight = False

      if current_value == cards[i].value:
        a_kind += 1

      else:
        self._of_a_kind(current_value, a_kind)
        current_value = cards[i].value
        a_kind = 1
    else:
      self._of_a_kind(current_value, a_kind)

  def cal(self):
    self.analyze()
    if self.flush:
      if self.straight:
        if sorted(self.cards)[-1].value == 14:
          self.rank = self.Ranks['Royal Flush']
        else:
          self.rank = self.Ranks['Straight Flush']
      else:
        self.rank = self.Ranks['Flush']

    elif self.straight:
      self.rank = self.Ranks['Straight']

    elif self.card4:
      self.rank = self.Ranks['Four of a Kind']

    elif self.card3:
      if self.card2:
        self.rank = self.Ranks['Full House']
      else:
        self.rank = self.Ranks['Three of a Kind']

    elif len(self.card2) == 2:
      self.rank = self.Ranks['Two Pairs']
      
    elif len(self.card2) == 1:
      self.rank = self.Ranks['One Pair']

    else:
      self.rank = self.Ranks['High Card']

  def __cmp__(self,other):
    if self.rank > other.rank:
      return 1
    elif self.rank < other.rank:
      return -1
    else:
      s_analyze = [self.card4, self.card3,self.card2,self.card1]
      o_analyze = [other.card4, other.card3,other.card2,other.card1]
      for s_card,o_card in zip(s_analyze,o_analyze):
        for s_value, o_value in zip(sorted(s_card, reverse=True), sorted(o_card, reverse=True)):
          if s_value > o_value:
            return 1
          elif s_value < o_value:
            return -1
      return 0

  def rank_name(self):
    for k,v in self.Ranks.items():
      if v == self.rank:
        return k


def read_cards(cards):
  hand = Hand()
  for card in cards:
    hand.add_card(Card(card[0],card[1]))
  return hand

def test():
  test_case = {
               '5H 5C 6S 7S KD 2C 3S 8S 8D TD':False,
               '5D 8C 9S JS AC 2C 5C 7D 8S QH':True,
               '2D 9C AS AH AC 3D 6D 7D TD QD':False,
               '4D 6S 9H QH QC 3D 6D 7H QD QS':True,
               '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D':True
              }
  for k,v in test_case.items():
    cards = k.split(' ')
    hand1 = read_cards(cards[:5])
    hand2 = read_cards(cards[5:])

    hand1.cal()
    hand2.cal()
    print hand1 > hand2, v

#test()
def main():
  f = open('p054_poker.txt')
  hands_list = map(lambda x: x.replace('\n',''), f.readlines())
  f.close()
  win = 0
  for fight in hands_list:
    cards = fight.split(' ')
    hand1 = read_cards(cards[:5])
    hand2 = read_cards(cards[5:])

    hand1.cal()
    hand2.cal()
    if hand1 > hand2:
      win += 1
  print win

main()
      
