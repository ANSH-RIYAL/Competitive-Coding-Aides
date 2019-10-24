# prefix sum is the sum of all the elements upto that element(including)
# it is useful when we need to find the sum of sub sequences many times

from random import randint
def prefix(l):
	prefix_sum=[l[0]]
	for i in range(1,len(l)):
		prefix_sum.append(l[i]+prefix_sum[i-1])
	return prefix_sum
n=randint(5,40)
print("The number of elements is: ",n)
l=[]
for i in range(n):
	l.append(randint(-100,100))
p=prefix(l)
print("Our array initially is: ",l)
print("The generated prefix sum array is: ",p)