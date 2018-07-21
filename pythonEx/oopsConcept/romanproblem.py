from collections import OrderedDict
from indexed import IndexedOrderedDict

class romanNum:
  def __init__(self):
    self.rom_val_dict = {'I': 1, 'IV':4, 'V': 5, 'IX':9, 'X': 10,'XL':40, 'L': 50, 'XC':90, 'C': 100,'CD':400, 'D': 500,'CM':900, 'M': 1000}
  
  def roman_to_int(self, s):
    int_val = 0
    for i in range(len(s)):
      if i > 0 and self.rom_val_dict[s[i]] > self.rom_val_dict[s[i - 1]]:
        int_val += self.rom_val_dict[s[i]] - 2 * self.rom_val_dict[s[i - 1]]
      else:
        int_val += self.rom_val_dict[s[i]]
    return int_val

  def int_to_roman(self, num):
    roman_num = ''
    length = len(self.rom_val_dict)
    while(num > 0 and length>0):
      ix = self.getKey(length-1)
      val = self.rom_val_dict[ix]
      for _ in range(num // val):
        roman_num += str(ix)
        num -= val
      length -= 1
    return roman_num

  def generateOrderedDict(self):
    return OrderedDict(sorted(self.rom_val_dict.items(), key=lambda t: t[0]))

  def generateIndexedOrderedDict(self):
    return IndexedOrderedDict(sorted(self.rom_val_dict.items(), key=lambda t: t[0]))
  
  def getKey(self, index):
    keylist = list(self.rom_val_dict)
    return keylist[index]
  