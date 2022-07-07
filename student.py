name=[]
perc=[]
usn=[]
dept=[]
n=int(input("enter the number of students"))
for i in range(0,n):
	name.append[i]=input("enter the name of student"+str(i+1))
	usn.append[i]=input("enter the usn of student "+str(i+1))
	dept.append[input("enter the dept of student"+str(i+1))]
	sub1=int(input('enter the marks of subject 1'))
	sub2=int(input('enter the marks of subject 2'))
	sub3=int(input('enter the marks of subject 3'))
	sub4=int(input('enter the marks of subject 4'))
	sub5=int(input('enter the marks of subject 5'))
	sub6=int(input('enter the marks of subject 6'))
	perc.append[(sub1+sub2+sub3+sub4+sub5+sub6)*100/600]


for i in range(0,n):
	if(perc[i]>75.0):
		print(name[i],usn[i])