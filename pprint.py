import pprint
message='hii how are you'
count={}
for character in message:
	count.setdefault(character,0)
	count[character]=count[character]+1
print(count)
pprint.pprint(count)

 