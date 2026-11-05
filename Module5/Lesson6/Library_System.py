
class Book:
    def __init__(self, Title, Author):
        self.Title = Title
        self.Author = Author
        self.is_borrowed = False
    def borrow(self):
        if self.is_borrowed == True:
            print("This book is already borrowed.")
        else:
            self.is_borrowed = True
            print("Book borrowed successfully.")
    def return_book(self):
        if self.is_borrowed == False:
            print("This book was not borrowed.")
        else:
            self.is_borrowed = False
            print("Book returned successfully.")

    def __str__(self):
        if self.is_borrowed == True:
            return self.Title+" is written by"+self.Author+" Status = Borrowed"
        else:
            return self.Title+" is written by"+self.Author+" Status = Available"

Book1 = Book("Dog Man", "Dav Pilkey")
Book2 = Book("Diary of a Wimpy Kid", "Jeff Kinney")
Book3 = Book("Sudha Murty", "Sudha Murty")

print("=" * 42)
print("         LIBRARY SYSTEM")
print("=" * 42)

print(Book1)
print(Book2)
print(Book3)
Book1.borrow()
Book2.borrow()
Book1.borrow()
Book1.return_book()
Book3.return_book()
print(Book1)
print(Book2)
print(Book3)