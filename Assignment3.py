#Q3. Write a menu driven program in that shows the working of a library .The menu opt on should be
# add book information
# display book information
# list all the books of given author
# list the counts in the books in the library using python
#exit.
class Book:
    def id1(self):
        self.id_num=int(input("Please enter id\n"))
    def cost(self):
        self.book_cost=int(input("Please enter cost\n"))
    def author(self):
        self.auth_name=input("Please enter author\n")
    def bookdb(self):
             print("BOOK ID: {} BOOK COST:{} BOOK AUTHOR:{} ".format(self.id_num,self.book_cost,self.auth_name))
b=Book()
b.id1()
b.cost()
b.author()
b.bookdb()





