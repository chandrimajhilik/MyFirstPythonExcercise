class complex:
  def __init__(self, _real, _imag):
    self.real = _real
    self.imag = _imag

  def __str__(self):
    return str(self.real) + ' + ' + str(self.imag) + 'i'

  def add(self, complex2):
    newcomplex = complex(self.real + complex2.real, self.imag + complex2.imag)
    return newcomplex

  def sub(self,complex2):
    newcomplex1=complex(self.real-complex2.real,self.imag-complex2.imag)
    return newcomplex1
  def multi(self,complex2):
    newcomplex2=complex(self.real*complex2.real,self.imag-complex2.imag)
    return newcomplex2
  def division(self,complex2):
    newcomplex4=complex(self.real/complex2.real,self.imag/complex2.imag)
    return newcomplex4
  def mod(self,complex2):
    newcomplex5=complex(self.real%self.imag,complex2.real/complex.imag)
    return newcomplex5 

