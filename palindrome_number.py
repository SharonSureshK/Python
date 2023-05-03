number=int(input("enter a number:"))
n=number
reverse=0
while(number!=0):
	remainder=number%10
	reverse=reverse*10+remainder
	number=number//10
print(reverse)
if(reverse==n):
		print("palindrome number")
else:
		print(" not a palindrome number")
	