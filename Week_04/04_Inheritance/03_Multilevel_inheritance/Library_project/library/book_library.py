
from library import Library

class BookLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
    
    
    def add_book(self, book, author, category):
        if self.book_exists(book):
            print("Book already exists.")
            return
        
        print("\n---------------- BOOK ADDED ----------------")
        with open(self.book_file, "a") as f:
            f.write(f"{book}|{author}|{category}\n")
        
        print(f"Book Name  : {book}" )
        print(f"Author     : {author}" )
        print(f"Category   : {category}" )
    
    
    def get_book_details(self, book):
        books = self.read_books()
            
        for line in books:
            data = line.strip().split("|")
                
            if data[0] == book:
                return {
                    "book" : data[0],
                    "author" : data[1],
                    "category" : data[2]
                }
        return None
    
    
    def show_book_details(self, book):
        details = self.get_book_details(book)
        
        if details is None:
            print("Book doesn't exist.")
            return
        
        print("\n---------------- BOOK DETAILS ----------------")
        print(f"\nBook    : {details['book']}")
        print(f"Author    : {details['author']}")
        print(f"Category  : {details['category']}")
    
    
    def show_books(self):
        books = self.read_books()
        
        if not books:
            print("Nothing to show.")
            return
        
        print("\n----------------  ALL BOOKS ----------------")
        print(f"\n========= {self.name} ========= \n")
        
        for line in books:
            data = line.strip().split("|")
            
            book = data[0]
            author = data[1]
            category = data[2]
            
            print(f"-> {book}")
            print(f"    Author   : {author}")
            print(f"    Category : {category}\n")


# b = BookLibrary("Book library")

# b.add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
# b.add_book("Harry Potter", "J.K. Rowling", "Fantasy")
# b.add_book("The Alchemist", "Paulo Coelho", "Fiction")
# b.show_books()