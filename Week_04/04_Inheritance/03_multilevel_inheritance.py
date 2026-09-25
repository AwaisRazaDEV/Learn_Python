# <-------------------------------- Introduction -------------------------------->
# A Child Class inherits from a Parent, which in turn inherits from another Grandparent Class.

#                                   Grandparent Class
#                                           |
#                                           |
#                                     Parent Class
#                                           |
#                                           |
#                                     Child Class




# <-------------------------------- (Challenge 1) -------------------------------->
# 1. Library -> Add/remove/search/show books
#       |
# 2. DigitalLibrary -> Download books
#       |
# 3. OnlineLibrary -> Generate a download link

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
    
#     def add_book(self, book):
#         if book in self.books:
#             print("Book already exists.")
#         else:
#             self.books.append(book)
#             print(f"Book Added : {book}")
    
#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             print(f"Book Removed : {book}")
#         else:
#             print("Book doesn't exist.")
    
#     def show_books(self):
#         print(self.name)
#         if not self.books:
#             print("Nothing to show.")
#         else:
#             for book in self.books:
#                 print(f"-> {book}")
    
#     def book_exists(self, book):
#         return book in self.books
    
#     def search_book(self, book):
#         if self.book_exists(book):
#             print(f"Yes, '{book}' exists.")
#         else:
#             print("Book doesn't exist.")


# class DigitalLibrary(Library):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def download_book(self, book):
#         if self.book_exists(book):
#             print(f"'{book}', Downloading...")
#         else:
#             print("Downloading Failed: Book doesn't exist.")


# class OnlineLibrary(DigitalLibrary):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def generate_link(self, book):
#         if not self.book_exists(book):
#             print("Failed to generate link: Book doesn't exist.")
#             return

#         link = f"https://library.com/books/{book.lower().replace(' ', '-')}"
#         print(f"Download Link: {link}")
        
#         while True:
#             text = input(f"Do you want to download '{book}' (yes/no) : ")
            
#             if text.lower() == "yes":
#                 self.download_book(book)
#                 break
            
#             elif text.lower() == "no":
#                 print("You Cancel Downloading.")
#                 break
            
#             else:
#                 print("Please Enter yes or no\n")



# b = OnlineLibrary("Digital Library")

# b.add_book("Harry Potter")
# b.add_book("Harry Potter")
# b.add_book("The Alchemist")
# b.add_book("The Great Gatsby")
# b.add_book("Book 404")

# b.remove_book("Book 404")

# b.show_books()

# b.search_book("Harry Potter")

# b.download_book("The Great Gatsby")
# b.download_book("Book 404")
# b.generate_link("Harry Potter")
# b.generate_link("The Alchemist")




# <-------------------------------- (Challenge 2) -------------------------------->
# 1. Library → manages books
#       |
# 2. BookLibrary → manages book authors/categories
#       |
# 3. EBookLibrary → manages file formats such as PDF/EPUB

from pathlib import Path

class Library:
    def __init__(self, name):
        self.name = name
        self.book_file = Path(__file__).parent / "books.txt"
        
        # Create file if it doesn't exist
        self.book_file.touch(exist_ok=True)
    
    
    # ------------------------ READ BOOKS ------------------------
    
    def read_file(self):
        with open(self.book_file, "r") as f:
            return f.readlines()
    
    
    # ------------------------ CHECK BOOK ------------------------
    
    def book_exists(self, book):
        books = self.read_file()
        
        for line in books:
            data = line.strip().split("|")
            
            if data[0] == book:
                return True
        
        return False
    
    
    # ------------------------- ADD BOOK -------------------------
    
    def add_book(self, book):
        if self.book_exists(book):
            print("Book already exists.")
            
        else:
            with open(self.book_file, "a") as f:
                f.write(book + "\n")

            print(f"Book Added : {book}")
    
    
    # ----------------------- REMOVE BOOK -----------------------
    
    def remove_book(self, book):
        if self.book_exists(book):
            books = self.read_file()
            
            with open(self.book_file, "w") as f:
                for line in books:
                    if line.strip() != book:
                        f.write(line)
            print(f"Book Removed : {book}")
        
        else:
            print("Book doesn't exist.")
    
    
    # ----------------------- SHOW BOOK -----------------------
    
    def show_books(self):
        books = self.read_file()
        
        if not books:
            print("Nothing to show.")
            
        else:
            for book in self.read_file():
                print(f"-> {book.strip()}")
    
    
    # ----------------------- SEARCH BOOK -----------------------
    
    def search_book(self, book):
        if self.book_exists(book):
            print(f"Yes, '{book}' exists.")
            
        else:
            print("Book doesn't exist.")



# ==================================================================
#                           BOOK LIBRARY
# ==================================================================

class BookLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
    


b = BookLibrary("BookLibrary")

# b.add_book("Harry Potter")
# b.add_book("The Great Gatsby")
b.book_exists("The Great Gatsby")
# b.show_books()
# print(b.read_file())
# b.add_author("Awais")