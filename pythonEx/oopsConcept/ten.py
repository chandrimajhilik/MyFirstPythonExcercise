class rectangle:
  def __init__(self,_hight,_width):
    self.hight=_hight
    self.width=_width
  def new(self):
    return self.hight*self.width

class circle:
  def __init__(self,_r):
    self.r=_r
  def area(self):
    return  3.14*self.r**2
  def perimeter(self):
    return self.r*3.14*2

class rev:
  def __init__(self):
    pass
  def work(self, sentence):
    self.input=str(sentence).split(" ")
    self.input=self.input[-1::-1]
    output=" ".join(self.input)  
    return output 

class upper1:
  def __init__(self):
    pass
  def get_string(self,string):
    self._string=string
  def print_string(self):
    y=str(self._string).upper()
    return y

class terget:
  def __init__ (self):
    pass
  def pairSum1(self,_arr):
    self.arr=_arr
    self.arr.sort()
    left, right = (0, len(self.arr)-1)
    while left<right:
        currentSum=self.arr[left]+self.arr[right]
        if currentSum==0:
            print (self.arr[left], self.arr[right])
            left+=1
        elif currentSum<0:
            left+=1
        else:
            right-=1 

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman = ''
        i = 0
        while  num > 0:
            for k in range(num // val[i]):
                roman += syb[i]
                num -= val[i]
            i += 1
        return roman

class power:
  def __init__(self,_x,_n):
    self.x=_x
    self.n=_n
  def pw(self):
    n=1
    for i in range(0,self.n):
      n=n*self.x
    print(n) 
     
      



    

   