n=int(input("enter  the number of terms needed:"))
fib_series=[]

f1=0
f2=1
f=f1+f2
fib_series.append(f1)
fib_series.append(f2)
fib_series.append(f)
for i in range(3,n):
	f1=f2
	f2=f
	f=f1+f2
	fib_series.append(f)
print("fibonacci series upto"+" "+str(n)+" "+"terms:")
print(fib_series)
