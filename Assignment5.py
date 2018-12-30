#Q5. WRITE A PROGRAM TO ACCEPT CUSTOMER DETAILS SICH AS :
# ACCOUNT_NO,NAME , BALANCE, AND ACCOUNT.
# ASSUME MAXIMUM CUSTOMERS IN 20 IN THE BANK.
# WRITE A FUNCTION TO PRINT THE ACCOUNT NO AND NAME OF EACH CUSTOMER WITH BALANCE BELOW RS 100.
class Customers:
    Bank=[]
    customers=int(input("enter no of customers(max 20) in the bank"))
    for x in range(customers):
        account_no=int(input("enter the account no of the customers in the bank"))
        Bank.append(account_no)
        name=input("enter the names of the customers in the bank")
        Bank.append(name)
        balance=int(input("enter the balance of the customer"))
        Bank.append(balance)
        account=(input("enter the account of the customer"))
        Bank.append(account)
        def Account(self,balance):
            if balance<100:
                print("the account no : {} the name of customer: {} the balance of customer: {}".format(self.account_no,self.name,balance))
            else:
                print("the balance of customer is greater than 100")
C=Customers()
C.Account(balance=68)