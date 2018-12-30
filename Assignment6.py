#Q6. Program to accept 5 names from user and store these names into an array sort these array elements in alphabetical order .
names=[]
n=5
for x in range(1,n+1,1):
    names.append(input("Enter the names:"))
names.sort()
print("Names after sorting are",names)