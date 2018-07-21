# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
# pattern printing examples

def problemFour(item, depth):
  for i in range(1,depth+1):
    printPattern((item+ ' '), i)
  counter = 0
  while counter<depth-1:
    printPattern((item+' '), (depth-1-counter))
    counter = counter+1

def printPattern(item, counter):
  print(item*counter)

def problemFourtyFour(depth):
  for i in range(1,depth+1):
    printPattern((str(i)+ ' '), i)  

def problemPrintAStar():
  # problem seventeen
  strStandingLine = '*   *'
  row=0
  while row<=6:
    if row==0:
      print('','*'*3)
    elif row==3:
      print('*'*5)
    else:
      print(strStandingLine)
    row=row+1

def problemprintlstar():
    strline='*    '
    row=0
    while row<=6:
      if row==6:
        print("* "*4)
      else:
        print(strline)
      row=row+1

def problemprintustar():
  str='*   *'
  row=0
  while row<=6:
    if row==6:
      print(" *** ")
    else:
      print(str)
    row=row+1    

def problemprintt():
  row=0
  while row<=6:
    if row==0:
      print("*"*5)
    else:
      print("  *  ")
    row=row+1    

def prpblemprinte():
  row=0
  while(row<=6):
    if row==0 or row==6:
      print("*"*5)
    elif row==3:
      print("*"*5)
    else:
      print("*     ")
    row=row+1 

def problemprintm():
  row=0
  while(row<=6):
    if row==2:
      print("** **")
    elif row==3:
      print("* * *")
    else:
      print("*   *")   
    row=row+1 

def problemprintp():
  row=0
  while(row<=6):
    if row==0 or row==3:
      print("*"*4)
    elif row==1 or row==2:
      print("*   *")
    else:
      print('*    ')
    row=row+1

def problemprintx():
  row=0
  while(row<=6):
    if row==0 or row==1 or row==5 or row==6:
      print("*   *")
    elif row==2 or row==4:
      print(" * * ")
    else:
      print("  *")
    row=row+1

def problemprinto():
  row=0
  while(row<=6):
    if row==0 or row==6:
      print(" *** ")
    else:
      print("*   *")
    row=row+1       

def problemprintd():
  row=0
  while(row<=6):
    if row==0 or row==6:
      print("*** ")
    else:
        print("*   *")
    row=row+1  

def problemprintz():
  for i in range(0,8):
    for j in range(0,8):
      if i==0 or i==7:
        print("* "*6)
        break
      elif i+j==8:
        print("* ")
        break
      else:
        print('.', end='')

def problemZ2(m):
  for i in range(1,m+1):
    if i==1 or i==m:
      print('*'*m)
    else:
      print('.'*(m-i),'*')
  
def problemprintN():
  for i in range(8):
    for j in range(8):
      if j==0 or j==7 or i==j:
        print("*",end='')
      else:
        print(' ',end='')
    print()   

# def staircase(item,depth):
#   for i in (1,depth+1):
#     print((item+" ")*i) 
