list=[]
ecount=ocount=0
n=int(input("enter the count of numbers you will enter:"))
print("enter the "+str(n)+"numbers")
list.append(n)
for i in range(n):
	list.append(int(input()))
for i in range(1,len(list)):
	if list[i]%2==0:
		ecount=ecount+list[i]
	else:
		ocount=ocount+list[i]
		
print("the sum of numbers in the list is:")
print("sum of evens:",ecount)
print("sum of odds:",ocount)