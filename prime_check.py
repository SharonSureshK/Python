number=int(input("enter a number:"))
flag=0
if(number==1):
	print("neither prime nor composite!")
elif(number==2):
	print("prime!")
elif(number>2):
	for i in range(2,number):
		if(number%2==0):
			flag=1
			break
	if flag:
		print("composite!")
	else:
		print("prime!")
else:
	print("invalid input ")
			


                        
