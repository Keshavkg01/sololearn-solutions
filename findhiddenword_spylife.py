str=input()
p=""
for i in range(1,len(str)+1):
    if str[-i].isalpha():
        p=p+str[-i]
    if str[-i]==" ":
        p=p+str[-i]
print(p)
        