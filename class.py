# Assignment 1: My Own Class Example
# I chose to make a Book class

class Book:
    # constructor
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # method
    def read(self):
        print("You are reading:", self.title, "by", self.author)

# Inheritance example
class EBook(Book):
    def __init__(self, title, author, pages, filesize):
        # use parent class constructor
        super().__init__(title, author, pages)
        self.filesize = filesize
    
    # overriding method (polymorphism)
    def read(self):
        print("You are reading the E-Book:", self.title, "on a device.")

# make objects
b1 = Book("Harry Potter", "J.K. Rowling", 400)
b2 = EBook("Python Basics", "Student", 250, "5MB")

# call methods
b1.read()
b2.read()
