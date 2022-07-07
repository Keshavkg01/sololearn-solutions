print('----------------------------------------------------------------------')
print('program to find average no of alpbts in word')
print('----------------------------------------------------------------------')
print('\n')
while(True):
	str=input('enter a sentence: ')
	count=0
	for i in range(len(str)):
	    if(str[i].isalpha()):
	        count+=1
	print("count of no of alphabets are:",count)
	w=len(str.split())
	print('no of words is:',w)
	a=count//w
	if (count%w)!=0:
	    a=a+1
	print('average no of alphabets in a word are:')
	print(a)
	