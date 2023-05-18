a=int(input("starting point of the interval:"))
b=int(input("end point of the interval:"))
l=[]
l1=[]
for i in range(a,b):
    for j in range(2,b):
        if(i==j*j):
            l.append(i)
for k in l:
    if(k%2==0):
        l1.append(k)
print("even perfect squares in the given interval are:")
print(l1)
            
        
