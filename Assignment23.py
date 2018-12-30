#23 Write a menu driven program
X = input("Enter your string")
l=len(X)
print("The length is", l)
Y = "Nandita"
Z= X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="I like Python"
new=old.replace("like","love")
print(new)
if X == Y:
    print("Equal")
else:
    print("Not Equal")