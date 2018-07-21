import os
from functools import reduce

class Util:
  def __init__(self):
    self.cls = lambda :os.system('cls')

sum = reduce(lambda a,b: a+b,[1,2,3,4,5])
print(sum)
fact = lambda n: reduce(lambda a,b: a*b, range(1,n+1))
print(fact(5))