str=input()
gno=str.index('G')
dno=str.index('$')
tno=str.index('T')
if (gno<dno<tno or tno<dno<gno) or ((dno<tno) and tno<gno) or (dno>tno and tno>gno) :
	print("ALARM")
else:
	print("quiet")
