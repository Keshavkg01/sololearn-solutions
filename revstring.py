s=input()
b=s
b=s[-1]
for i in range(2,len(s)+1):
	b=b+s[-i]
print(b)