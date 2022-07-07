str=input()
b=str.split()
c=[]
res=""
if b[1]=="am":
	print(b[0])
else:
	k=b[0].split(":")
	k[0]=int(k[0])+12
	k.insert(1,":")
	
	print(*k)