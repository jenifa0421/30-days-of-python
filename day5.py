#1.FUNCTION

def fun (a,b):

    print("addition of two numbers is",+(a+b))
    print("Subtraction of two numbers is",+(a-b))
    print("Multiplication of two numbers is",+( a * b))
    print("Division of two numbers is",+( a / b))

a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :21"))
fun(a,b)

#2.COVID FUNCTION

def covid(patientname,temp=98):
    print("Name of the patient is",patientname)
    print(f"Temperature of the patient {patientname}is ",temp)

covid("jenifa",79)
covid("diya")