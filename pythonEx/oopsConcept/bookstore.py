from book import *

class bookStore:
  count=0
  storeType = 'book store'
  
  def __init__(self, _name, _address):
    self.name = _name
    self.address = _address
    self.books = []
    bookStore.count +=1

  def __str__(self):
    return self.name + ' at ' + self.address

  def addBook(self, _book):
    self.books.append(_book)
