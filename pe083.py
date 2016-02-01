from mytools import get_time
class Cell:
  def __init__(self, value):
    self.value = value
    self.cost = 10**6
  def __call__(self,value):
    self.__init__(value)
  def get_value(self):
    return self.value
  def set_cost(self,cost):
    self.cost = cost
  def get_cost(self):
    return self.cost


def readlinefromfile(file):
  f = open(file)
  lines = map(lambda x: x.replace('\n',''), f.readlines())
  f.close()
  i = 0
  for line in lines:
    yield i, line
    i += 1


class Matrix:
  def __init__(self, start_position, end_position):
    self.start_position = start_position
    self.end_position = end_position
    self.matrix = []
    self.search_range = [(+1,0),(0,+1),(-1,0),(0,-1)] 
    
  def read(self,file):
    for i, line in readlinefromfile(file):
      self.matrix.append([Cell(int(num)) for num in line.split(',')])

  def set_cost(self,i,j):
    cell = self.matrix[i][j]
    previous_cost = cell.get_cost()
    if [i,j] == self.start_position:
      cell.set_cost(cell.get_value()) 
      return False
    cost_list = []
    for k,l in self.search_range:
      try:
        if i+k >= 0 and j+l >= 0:
          cost_list.append(self.matrix[i+k][j+l].get_cost())
      except IndexError:
        pass
    cell.set_cost(cell.get_value()+min(cost_list))
    corrent_cost = cell.get_cost()
    return previous_cost != corrent_cost

  def update_cost(self):
    update_flag = False
    for j in range(len(self.matrix[0])):
      for i in range(len(self.matrix[0])):
        if self.set_cost(i,j):
          update_flag = True
    return update_flag
  def get_end_cost(self):
    return self.matrix[self.end_position[0]][self.end_position[1]].get_cost()


@get_time
def main(start_position=[0,0],end_position=[80-1,80-1],file='p083_matrix.txt'):
  matrix = Matrix(start_position,end_position)
  matrix.read(file)
  while matrix.update_cost():
    pass
  return matrix.get_end_cost()
  
#print main([0,0],[4,4],'p083_matrix_test.txt')
print main()
