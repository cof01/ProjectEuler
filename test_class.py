class Class1:
  def __init__(self, argv1 = []):
    self.argv = argv1
  def add(self,argv):
    self.argv += argv

class Class2:
  def __init__(self):
    self.argv = []
  def add(self,argv):
    self.argv += argv


c1 = Class1()
c1.add(['a1','a2','a3'])
del c1
c1 = Class1()
c1.add(['a4','a5'])
print c1.argv

c2 = Class2()
c2.add(['a1','a2','a3'])
del c2
c2 = Class2()
c2.add(['a4','a5'])
print c2.argv

