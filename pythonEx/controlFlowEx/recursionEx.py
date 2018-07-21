# recursion porte hobe
# https://www.programiz.com/python-programming/recursion
def fibonacci(n):
  fibo = [0,1]
  first=fibo[0]
  second=fibo[1]
  while len(fibo)<n:
    third=first + second
    fibo.append(third)
    first=second
    second=third
  return fibo

def fibonaccirec(n):
  if n<=1:
    return n
  else:
    return (fibonaccirec(n-1)+fibonaccirec(n-2))

for item in range(5):
  print(fibonaccirec(item))
