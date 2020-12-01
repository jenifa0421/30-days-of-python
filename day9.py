#1. create a lambda function that multiplies argument x with argument y

def A(x):
  return (lambda y:x*y)
B=A(4)
print(B(21))

OUTPUT:
84

#2.Write a python program to create fibonacci series to n using lambda

from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])
print("\nFibonacci series upto 9:")
print(fib_series(9))

OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py

Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]

Process finished with exit code 0

#3. write a python prpgram to mulitply each number of a given list with given number

mylist=[]
n=int(input("enter no of elemnts"))
for i in range(0,n):
    ele=int(input("enter element"+str(i+1)+":"))
    mylist.append(ele)
print(mylist)
print("enter the number by which you want to multiply the list elements")
k=int(input())
nresult=(map(lambda x:x*k,mylist))
print(list(nresult))

OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
enter no of elemnts3
enter element1:1
enter element2:6
enter element3:8
[1, 6, 8]
enter the number by which you want to multiply the list elements
5
[5, 30, 40]
Process finished with exit code 0

#4.write a python program  to find numbers divisible by 9 from a list of numbers

mylist=[]
n=int(input("enter no of elemnts"))
for i in range(0,n):
    ele=int(input("enter element"+str(i+1)+":"))
    mylist.append(ele)
print("The list elements are:",mylist)
print("The numbers which are divisible by 9 in the list are:")
p=list(filter(lambda x:(x%9==0),mylist))
print(p)

OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
enter no of elemnts6
enter element1:1
enter element2:2
enter element3:9
enter element4:36
enter element5:27
enter element6:5
The list elements are: [1, 2, 9, 36, 27, 5]
The numbers which are divisible by 9 in the list are:
[9, 36, 27]
Process finished with exit code 0


#5.write a python program to count the even numbers in a given list of numbers

mylist=[]
n=int(input("enter no of elemnts"))
for i in range(0,n):
    ele=int(input("enter element"+str(i+1)+":"))
    mylist.append(ele)
print("The list elements are:",mylist)
print("The even numbers in the list are")
p=list(filter(lambda x:(x%2==0),mylist))
print(p)
l= len(p)
print("The count is",l)

OUTPUT:
C:\Users\Home\PycharmProjects\pythonProject2\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/pythonProject2/main.py
enter no of elemnts5
enter element1:1
enter element2:7
enter element3:14
enter element4:21
enter element5:28
The list elements are: [1, 7, 14, 21, 28]
The even numbers in the list are
[14, 28]
The count is 2

Process finished with exit code 0




