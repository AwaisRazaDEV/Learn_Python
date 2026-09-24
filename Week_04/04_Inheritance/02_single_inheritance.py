
# <-------------------------------- Introduction -------------------------------->
# A child class inherits from exactly one parent class.

#                                     Parent Class
#                                           |
#                                           |
#                                     Child Class



# <-------------------------------- (Challenge 1) -------------------------------->
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        if book in self.books:
            print("Book already exists.")
        else:
            self.books.append(book)
            print(f"Book Added : {book}")
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book Removed : {book}")
        else:
            print("Book doesn't exist.")
    
    def show_books(self):
        print(self.name)
        if not self.books:
            print("Nothing to show.")
        else:
            for book in self.books:
                print(f"-> {book}")
    
    def search_book(self, book):
        if book in self.books:
            print(f"Yes, '{book}' exists.")
        else:
            print("Book doesn't exists.")


class DigitalLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
    
    def download_book(self, book):
        if book in self.books:
            print(f"'{book}', Downloading...")
        else:
            print("Downloading Failed: Book not exists.")


b = DigitalLibrary("Digital Library")

b.add_book("Harry Potter")
b.add_book("Harry Potter")
b.add_book("The Alchemist")
b.add_book("The Great Gatsby")
b.add_book("Book 404")

b.remove_book("Book 404")

b.show_books()

b.search_book("Harry Potter")

b.download_book("The Great Gatsby")
b.download_book("Book 404")



# <-------------------------------- (Challenge 2) -------------------------------->
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        if book in self.books:
            print("Book already exist.")
        else:
            self.books.append(book)
            print(f"Book Added : {book}")
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book Removed : {book}")
        else:
            print("Book doesn't exist.")
    
    def show_books(self):
        print(self.name)
        if not self.books:
            print("Nothing to show.")
        else:
            for book in self.books:
                print(f"-> {book}")
    
    def search_book(self, book):
        if book in self.books:
            print(f"Yes, '{book}' exist.")
        else:
            print("Book doesn't exist.")


class SchoolLibrary(Library):
    def __init__(self,name, school_name, student_count):
        super().__init__(name)
        self.school_name = school_name
        self.student_count = student_count
    
    
    def show_school_info(self):
        print(f"My school name is '{self.school_name}'. There are {self.student_count}+ students in my school and also, there is a library in my school '{self.name}'")


s = SchoolLibrary("School Library", "The Coding School", 250)

s.show_school_info()

# s.add_book("Harry Potter")
# s.add_book("Harry Potter")
# s.add_book("The Alchemist")
# s.add_book("The Great Gatsby")
# s.add_book("Book 404")

# s.remove_book("Book 404")

# s.show_books()

# s.search_book("Harry Potter")
