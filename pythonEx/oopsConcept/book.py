class book:
  def __init__(self, _name, _author, _price):
    self.name = _name
    self.author = _author
    self.price = _price

  def __str__(self):
    return self.name + ' written by ' + self.author + ' costs ' + str(self.price)