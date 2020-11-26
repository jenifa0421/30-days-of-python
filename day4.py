#1.LIST OPERATIONS

l=[]
n=int(input("enter number of elements "))
for i in range(0,n):
    e=int(input("enter element"+str(i+1)+ ":"))
    l.append(e)
print(l)
a=int(input("enter the element you want to add"))
l.append(a)
print(l)
d=int(input("enter the element you want to remove"))
l.remove(d)
print(l)
min=min(l)
max=max(l)
print("smallest number in the list")
print(min)
print("largest number in the list")
print(max)

#2. REVERSING A TUPLE

x=(5,6,7,8)
y=reversed(x)
print(tuple(y))

#3.TUPLE INTO LIST

t=('Dhoni','Rahul','sam','shreyes')
print(t)
l=list(t)
print(l)

#LIST INTO TUPLE

l=['Dhoni','Rahul','sam','shreyes']
print(l)
t=tuple(l)
print(t)