def count(str):
	upper=lower=number=0
	space=1
	a=len(str)
	for i in range(a):
		if str[i].isupper():
			upper+=1
		elif str[i].islower():
			lower+=1
		elif str[i].isdigit():
			number+=1
		elif str[i]==" ":
			space += 1
	print('upper',upper)
	print('lower',lower)
	print('number',number)
	print('words',space)
	
str=input()	
count(str)

			