# code to generate coefficient of all powers of x in a polynomial when factors are given
from random import randint
def multiply(l,a,b):
	# l is the list containing the coefficients before multiplying (ax+b) to the polynomial
	# the length of l denotes the degree of the polynomial
	# if length = 4, the polynomial is cubic (ax^3+bx^2+cx+d)
	# a is the coefficient of x in (ax+b)
	# b is the constant from (ax+b)
	last=l[-1]*b
	newl=[]
	newl.append(l[0]*a)
	for i in range(len(l)-1):
		newl.append(l[i]*b+l[i+1]*a)
	newl.append(last)
	return newl
#starting with a random ax+b
l=[randint(-10,10),randint(-10,10)]
print("Starting with l= ",l)
for i in range(10):
	a=randint(-10,10)
	b=randint(-10,10)
	print("we multiply ",l,"with (",a,"x + (",b,"))")
	l=multiply(l,a,b)
print(l)