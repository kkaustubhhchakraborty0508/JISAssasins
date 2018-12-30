#7.Write a program to calculate the sum of digits of a given no.
n=int(input("enter a number"))
sum=0
while(n>0):
    dig=n%10
    sum=sum+dig
    n=n/10
print("the total sum of the digits:",sum)

