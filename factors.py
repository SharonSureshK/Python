number=int(input("enter a number:"))
l1=[]
for i in range(2,number+1):
	if(number%i==0):
		l1.append(i)
print("factors are:")
print(l1)