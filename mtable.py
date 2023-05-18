number=int(input("enter a number of which the multiplication table is needed :"))
limit=int(input("enter the limit:"))
for i in range(1,limit+1):
	print(str(i)+"*"+str(number)+"="+str(i*number))
