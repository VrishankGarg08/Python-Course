# Library System
# Build a simple library system using a class. Each book is an object. Your system lets users borrow and return books and tracks whether each book is currently available.

# What you need to use
# ------------------------------------------------------------------------
# 1.  Book class      →  __init__ sets title, author, and is_borrowed = False
# 2.  borrow()        →  sets is_borrowed to True and prints a confirmation
# 3.  return_book()   →  sets is_borrowed to False and prints a confirmation
# 4.  3 Book objects  →  demonstrate both borrow() and return_book()
# 5.  self            →  used to access and update attributes inside methods
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  Book class with __init__ setting title, author, is_borrowed   →   5 marks
# 2.  borrow() sets is_borrowed True and prints confirmation         →  10 marks
# 3.  return_book() sets is_borrowed False and prints confirmation   →  10 marks
# 4.  At least 3 Book objects with both methods demonstrated         →  10 marks
# 5.  Program runs without any errors                                →   5 marks
# ========================================================================
# Total  →  40 marks
# ========================================================================
Books = {"Dog Man":10,"Wimpy Kid":19,"Sudha Murty": 9}
print("Books Available :")
print(Books)
Dog_Man = 10
Wimpy_Kid = 19
Sudha_Murty = 9
class Book_class:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        is_borrowed = False
    Book = input("Enter a Name Of Book:").split()
    borrow = input("Do You Want To Issue/borrow This Book:(YES/NO) : ").upper()
    if borrow == "YES":
        Book = {Book} - 1
        print("Your Book Is Issued")
        return_book = input("Do You Want To Return This Book:(YES/NO)").upper()
    if borrow == "NO":
        print("Your Book Is Kept Safe With us.")
    if return_book == "YES":
        Book = Book + 1
        print("Your Book Has Been Returned To Us")
    if return_book == "NO":
        print("Your Book Hasn't Been Returned.")

print("Thank You For Visiting The Library")
    