import random
import types
import re
import functools


def evenoddlist(n):
	evenlist = []
	oddlist = []

	for i in n:
		if i % 2 == 0:
			evenlist.append(i)
		else:
			oddlist.append(i)
	print(evenlist, " has total", len(evenlist), " elements")
	print(oddlist, " has total", len(oddlist), " elements")


def generaterandomlist(seed):
	return random.sample(range(1, int(seed)), int(seed / 2))


def count():
	string = "i99            8u"
	print(len(string))


def temp():
	f = 140
	c = 5 * (f - 32 / 9)
	print(c)


def fibo(n):
	f = 0
	l = 1
	#print(f)
	while (n > l):
		fib = f + l
		f = l
		l = fib
		print(l)


def countfor(s):
	inputlist = [ord(a) for a in s]
	print(inputlist)
	countlttr = []
	for i in inputlist:

		if i in range(65, 91) or i in range(97, 123):
			countlttr.append(inputlist)
	print(len(countlttr))


def type1(n):
	if (isinstance(n, list) or isinstance(n, tuple)):
		print(n, type(n))
		for i in n:
			print(i, type(i))
			type1(i)
		else:
			print(type(n), end=',')


def zodiac(year):
	if (year % 2 == 0):
		sign = "a"
	elif (year % 2 == 1):
		sign = "b"
	elif (year % 2 == 2):
		sign = "x"
	else:
		sign = "h"
	print(sign)


def agecalculation(n):
	if n in range(1, 3):
		print(10.5)
	else:
		print(n * 4)


def vowelorconsonant(n):
	if n in ("a" or "e" or "i" or "o" or "u"):
		print("vowel")
	else:
		print("consonant")


def howmanydaysinthemonth(n):
	if n in ("september" or "april" or "june" or "november"):
		print(30)
	elif n in ("january" or "december" or "march"):
		print(31)
	else:
		print(28)


def median(a, b, c):
	if (b > a) and (b < c):
		print(b)
	elif (a > c) and (b > a):
		print(a)
	else:
		print(c)


def typeoftriangle(a, b, c):
	if (a == b == c):
		print("equlilaterl")
	elif (a == b != c):
		print("isosceles")
	else:
		print("scaine triangle")


def table(n):
	for f in range(1, 11):
		print(n, 'x', f, '=', n * f)


def counting(N):
	input = [ord(a) for a in N]
	print(input)
	countltt = []
	for i in input:
		if i in range(65, 91) or i in range(97, 133):
			countltt.append(input)
	print(len(countltt))


def alldigiteven():
	out = []
	for i in range(200, 210):
		temporary = [int(a) for a in str(i)]
		#inputlist.append([l for item in l if item%2==0])
		if (all(item % 2 == 0 for item in temporary)):
			out.append(temporary)
	print(out)


def printfizzbizz(n):
	if (n % 3 == 0 and n % 5 == 0):
		print("fizzbuzz")
	elif (n % 3 == 0):
		print("fizz")
	elif (n % 5 == 0):
		print("bizz")


def binarytodecimal(n):
	binarylist = n.split(',')
	for item in binarylist:
		y = int(item, base=2)
		if (y % 5 == 0):
			print(bin(y))


def upper(s):
	coun = 0
	for i in s:
		if i.isupper():
			coun = coun + 1
	print(coun)


def changedate(date, month, year):
	if month in (1, 3, 5, 7, 8, 10, 12):
		monthlength = 31
	elif month == 2:
		if (year % 4 == 0):
			monthlength = 29
		else:
			monthlength = 28
	if (date < monthlength):
		date = date + 1
	else:
		date = 1
		if month == 12:
			month = 1
			year = year + 1
		else:
			month = month + 1
	print(date, month, year)


def getWordsWithCapitalLetters(sentence):
	wordList = sentence.split(" ")
	for word in wordList:
		if (any(letter.isupper() for letter in word)):
			print(word)


def guessNumber():
	num = random.randint(1, 10)
	result = False
	while (result != True):
		guess = input("guess a number between 1 and 10")
		result = int(guess) == num
		if (result == True):
			break
	print("correct guess")


def guessno():
	target_num, guess_num = random.randint(1, 10), 0
	while target_num != guess_num:
		guess_num = int(
		    input('Guess a number between 1 and 10 until you get it right : '))
	print('Well guessed!')


def password(p):
	if len(p) > 6 and len(p) < 17:
		if re.search("[a-z]", p) and re.search("[0-9]", p) and re.search(
		    "[A-Z]", p) and re.search("[$#@]", p):
			print("valid")
	else:
		print("invalid")


def mnmatrix(m, n):
	for i in range(m):
		templist = []
		for j in range(n):
			templist.append(i * j)
		print(templist)

def number():
  a=[1,25,2]
  y=sorted(a)
  print(y[1])

def cal():
	f = lambda x, y : x + y
	print(f(1,1))
	g= lambda a,b:a-b
	print(g(1,1))
	i=lambda c,d : c * d
	print(i(1,1))

def gcd_lcm():
	a=48
	b=12
	k=a*b
	while(a!=b):	
		if(a>b):
			a=a-b
		elif(b>a):
			b=b-a
		print(a)		
		gcd=a
		print(gcd)
	lcm=k//gcd
	print(lcm)	

def gcd(a,b):
	while(a!=b):
		if(a>b):
			a=a-b
		elif(b>a):
			b=b-a
	print(a)
	return a	

def lcm(a,b):
	l=int((a*b)/gcd(a,b))
	print(l)
	return l

def recudegcd(k):
	# gc=functools.reduce(lambda a,b: gcd(a,b),k )	
	gc=functools.reduce(gcd,k )	
	print(gc)

def reducelcm(k):
	lc=functools.reduce(lambda a,b:lcm(a,b),k)
	print(lc)

def bubble_sort():
	sort_list=[1,2,10,4,7]
	n=len(sort_list)
	for j in range(n):
		for k in range(0, n -j - 1):
			if sort_list[k] > sort_list[k + 1]:
				sort_list[k], sort_list[k + 1] = sort_list[k + 1], sort_list[k]
	print(sort_list)

# def swap(arr):
# 	return functools.reduce(lambda a,b : [b]+a, arr,[])

# def dobubble(a,b):
# 	if b>a:
# 		return swap([a,b])
# 	else:
# 		return [a,b]

# def bubblesort(arr):
	# l = functools.reduce(lambda a,b: dobubble, arr,[])
	# print(l)
	
 
