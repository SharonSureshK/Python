n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
l1=[]
l2=[]
l3=[]
for i in range(2,n1+1):
    if(n1%i==0):
        l1.append(i)
for j in range(2,n2+1):
    if(n2%j==0):
        l2.append(j)
for k in l1:
    for x in l2:
        if(k==x):
            l3.append(k)
m=l3[0]
for i in range(1,len(l3)):
    if l3[i] > m:
        m=l3[i]

print("THE GCD OF"+" "+str(n1)+" "+"and"+" "+str(n2)+" "+"is"+" "+str(m))





            
            
