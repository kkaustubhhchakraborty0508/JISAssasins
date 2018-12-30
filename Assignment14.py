#Q14Program to accept 'n' numbers from user and store these numbers  into an array and count the number into an array and count the number of occurences of each number

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# Driver Code
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
nums=int(input("enter the no. to be count"))
print(countX(lst, nums))
