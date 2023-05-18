a=int(input("enter the initial point:"))
b=int(input("enter the final point:"))
l=[] 
l1=[]
l4=[]
for i in range(a,b):
	l.append(i)
for i in range(a,b):
	for j in range(2,i):
		if(i%j==0):
			l1.append(i)
for x in l:
	if  x not in l1:
		l4.append(x)
print("prime numbers  in the interval "+str((a,b))+":")
print(l4)