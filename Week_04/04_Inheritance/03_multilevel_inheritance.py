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
            print("Book doesn't exist.")


class DigitalLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
    
    def download_book(self, book):
        if book in self.books:
            print(f"'{book}', Downloading...")
        else:
            print("Downloading Failed: Book doesn't exist.")


class OnlineLibrary(DigitalLibrary):
    def __init__(self, name):
        super().__init__(name)
    
    def generate_link(self, book):
        self.search_book(book)
        while True:
            self.text = input(f"Do you want to download '{book}' (yes/no) : ")
            if self.text.lower() == "yes":
                self.download_book(book)
                break
            elif self.text.lower() == "no":
                print("You Cancel Downloading.")
                break
            else:
                print("Please Enter yes or no")





b = OnlineLibrary("Digital Library")

b.add_book("Harry Potter")
# b.generate_link("Harry Potter")
b.generate_link("The Alchemist")
# b.add_book("Harry Potter")
# b.add_book("The Alchemist")
# b.add_book("The Great Gatsby")
# b.add_book("Book 404")

# b.remove_book("Book 404")

# b.show_books()

# b.search_book("Harry Potter")

# b.download_book("The Great Gatsby")
# b.download_book("Book 404")