def simpleArraySum(ar):
  sum=0
  for item in ar:
    sum = sum + item
  return sum

def aVeryBigSum(ar):
  simpleArraySum(ar)

def maxmin():
  # list(map(int, input().rstrip().split()))
  y=[1,8,2,3,5]
  s=list(sorted(y))
  print("minimal",sum(s[:4])) 
  print('maximum',sum(s[-4:]))  

def timeconvert():
  s='12:05:45AM'
  # 12:40:22AM --> 00:40:22
  time=s[:-2].split(':')
  time[0]=str(int(time[0])+12) if s[-2:][0]=='P' else '00' if time[0]=='12' else time[0]
  print(':'.join(time))


def calculate():
  a=[-4,3,-9,0,4,1]
  print(len([i for i in a if i>0])/len(a))
  print(len([i for i in a if i<0])/len(a))
  print(len([i for i in a if i==0])/len(a))
  # p=0
  # m=0
  # z=0
  # for n in a:
  #   if n>0:
  #     p=p+1

  #   elif n==0:
  #     z=z+1
  #   else:
  #     m=m+1 
  # print(p)
  # print(z)
  # print(m)  
  # pp=0
  # np=0
  # zp=0
  # pp=p/y
  # np=m/y
  # zp=z/y
  # print(pp)
  # print(np)
  # print(zp)   

def staircase(nolines):
  for a in range(1,nolines+1):
    print(' '*(nolines-a)+"#"*a)

def birthday(a):
  y=list(sorted(a))[-1:]
  print(a.count(y[0]))  


def diagonaldiff():
  a = [[1, 2, 3], [5, 6, 0], [7, 8, 1]]
  majordiagonal=[]
  minordiagonal=[]
  for i in range(len(a)):
    for j in range(len(a[i])):
      if(i == j):
        majordiagonal.append(a[i][j])
      if i+j==2:
        minordiagonal.append(a[i][j])
  print(majordiagonal)
  print(minordiagonal)
  diff = sum(majordiagonal) - sum(minordiagonal)
  print(diff)

def printrunner(arr):
  print(sorted(filter(lambda i:i!=max(arr),arr))[-1])
  # print(y[-1])


