number=int(input("enter a number:"))
sum=0
while(number!=0):
	remainder=number%10
	sum=sum+remainder
	number=number//10
print("sum of the digits:"+str(sum))