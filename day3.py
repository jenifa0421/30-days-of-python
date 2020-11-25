#1.MERGING TWO DICTIONARIES

fruits={
    "apple" : 2,
    "mango" : 5,
    "orange" : 10
}
print(fruits)
dry_fruits={
    "almond" : 5,
    "dates" : 3,
    "pista": 5
}
print(dry_fruits)
fruits.update(dry_fruits)
print(fruits)

#2.REMOVING KEY

fruits={
    "apple" : 2,
    "mango" : 5,
    "orange" : 10
}
del fruits['apple']
print(fruits)

#3.MAPPING TWO LISTS INTO DICTIONARY

keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys")
for i in range(0,n):
    ele=int(input("Enter element" +str(i+1)+":"))
    keys.append(ele)
print("For values")
for i in range(0,n):
    ele = int(input("Enter element" + str(i + 1) + ":"))
    values.append(ele)
d=dict(zip(keys,values))
print("Dictionary is ")
print(d)


#4.LENGTH OF SET

set={1,2,3,4}
length=len(set)
print("length of set is")
print(length)

#5.REMOVE INTERSECTION OF SETS

S1={1,2,3,4}
S2={3,4,5,6}
print(S1-S2)
print(S2-S1)

