# Replace all 0’s with 1 in a given integer

print("Enter a positive no: ")
num=input()
st=""
for i in range(0,len(num)):
	if num[i]=='0':
		st=st+'1'
	else:
		st=st+num[i]
print("OUTPUT: ",st)
		