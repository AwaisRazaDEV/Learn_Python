

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
    
    def book_exists(self, book):
        return book in self.books
    
    def search_book(self, book):
        if self.book_exists(book):
            print(f"Yes, '{book}' exists.")
        else:
            print("Book doesn't exist.")


class DigitalLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
    
    def download_book(self, book):
        if self.book_exists(book):
            print(f"'{book}', Downloading...")
        else:
            print("Downloading Failed: Book doesn't exist.")


class OnlineLibrary(DigitalLibrary):
    def __init__(self, name):
        super().__init__(name)
    
    def generate_link(self, book):
        if not self.book_exists(book):
            print("Failed to generate link: Book doesn't exist.")
            return

        link = f"https://library.com/books/{book.lower().replace(' ', '-')}"
        print(f"Download Link: {link}")
        
        while True:
            text = input(f"Do you want to download '{book}' (yes/no) : ")
            
            if text.lower() == "yes":
                self.download_book(book)
                break
            
            elif text.lower() == "no":
                print("You Cancel Downloading.")
                break
            
            else:
                print("Please Enter yes or no\n")



b = OnlineLibrary("Digital Library")

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
b.generate_link("Harry Potter")
b.generate_link("The Alchemist")


