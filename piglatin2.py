s=input()
b=""//TO STORE OUTPUT STRING
q=s.split()
for i in q:
	b=b+i[1:]+i[0]+"ay "
print(b)