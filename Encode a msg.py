#program to encode a string with inverse alphabets
s=input("enter  a  string: ")
p=chr(90-(ord(s[0])-65))
for i in range(1,len(s)):
	if(s[i]==" "):
		p=p+" "
		continue;
	if(s[i]!=" "):
		p=p+chr(90-(ord(s[i])-65))
print("the encoded msg is :",p)
