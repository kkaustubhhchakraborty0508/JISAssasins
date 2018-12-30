#19. program to accept three sides of a triangle as an input. and print whether triangle is valid or not
a=int(input("enter the first side of a triangle"))
b=int(input("enter the second side of the triangle"))
c=int(input("enter the third side of the triangle"))
if (a+b>c):
    print("triangle is valid")
elif (b+c>a):
    print("triangle is valid")
elif (c+a>b):
    print("triangle is valid")
else:
    print("triangle is not valid")