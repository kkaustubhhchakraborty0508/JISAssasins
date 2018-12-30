#Q22. Write a program to accept book details of n books as book_title, author,publisher,and costs.
# Assign the accession no to the each book in increasing order and dispLay these details as
# books of a specific number.
# Books by a specific publisher
# all books costing rs 500 and above.
# All books
Books=[]
books1=[]
book=int(input("enter the no of books"))
for x in range(book):
    book_title=(input("enter the book title"))
    Books.append(book_title)
    author=input("enter the author of the book")
    Books.append(author)
    publisher=(input("enter the publisher"))
    Books.append(publisher)
    cost=int(input("enter the cost of the book"))
    Books.append(cost)
    accesion_no=int(input("enter the accession no to the book"))
    books1.append(accesion_no)
books1.sort()
print("The sorted books: {}".format(books1))
if cost>500:
    print("the books whose cost more than 500: BOOK TTITLE: {} BOOK AUTHOR:{} BOOK PUBLISHER:{} BOOK COST:{}".format(book_title,author,publisher,cost))
else:
    print("the books cost are less than 500:BOOK TTITLE: {} BOOK AUTHOR:{} BOOK PUBLISHER:{} BOOK COST:{}".format(book_title,author,publisher,cost))

print("BOOK TTITLE: {} BOOK AUTHOR:{} BOOK PUBLISHER:{} BOOK COST:{}".format(book_title,author,publisher,cost))



