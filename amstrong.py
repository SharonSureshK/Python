number=int(input("enter a number:"))
num=number
n=len(str(number))
amstrong=0
while(number!=0):
	remainder=number%10
	amstrong=amstrong+(remainder**n)
	number=number//10
if(num==amstrong):
		print("it's an amstrong number")
else:
		print("it's not an amstrong number")
	
	