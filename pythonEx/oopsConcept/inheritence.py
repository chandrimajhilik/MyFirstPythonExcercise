class Person:
  def __init__(self, _firstName, _lastName):
    self.firstName = _firstName
    self.lastName = _lastName

  def __str__(self):
    return self.firstName + ' ' + self.lastName

  def abbreviation(self):
    return self.firstName[:1].upper() + self.lastName[:1].upper()

class Student(Person):
  def __init__(self, _firstName,_lastName,_rollNumber):
    super().__init__(_firstName,_lastName)
    self.rollNumber = _rollNumber

  def __str__(self):
    return super().__str__()+ ' ' + self.rollNumber

  def abbreviation(self):
    return super().abbreviation() + ' ' 

class highscl(Student):
  def __init__(self,_firstName,_lastName,_rollNumber,_subject):
    super().__init__(_firstName,_lastName,_rollNumber)
    self.subject=_subject
  def __str__(self):
    return super().__str__()+" "+self.subject

class Celsius:
  def __init__(self, temperature = 0):
    self.temperature = temperature

  def to_fahrenheit(self):
    return (self.temperature * 1.8) + 32

  def __str__(self):
    return str(self.temperature)

  # new update
  @property
  def temperature(self):
      print('getting value...')
      return self._temperature

  @temperature.setter
  def temperature(self, value):
    print('...setting value')
    if value < -273:
      raise ValueError("Temperature below -273 is not possible")
    self._temperature = value

  # temperature = property(get_temperature,set_temperature)