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

