from pathlib import Path

class Library:
    def __init__(self, name):
        self.name = name
        self.data_dir = Path(__file__).parent.parent / "data"
        self.book_file = self.data_dir / "books.txt"
        
        self.data_dir.mkdir(exist_ok= True) # Create directory if it doesn't exist
        self.book_file.touch(exist_ok=True) # Create file if it doesn't exist
    
    
    # ------------------------ READ BOOKS ------------------------
    
    def read_books(self):
        with open(self.book_file, "r") as f:
            return f.readlines()
    
    
    # ------------------------ CHECK BOOK ------------------------
    
    def book_exists(self, book):
        books = self.read_books()
        
        for line in books:
            data = line.strip().split("|")
            
            if data[0] == book:
                return True
        
        return False
    
    
    # ------------------------- ADD BOOK -------------------------
    
    def add_book(self, book):
        if self.book_exists(book):
            print("Book already exists.")
            return

        with open(self.book_file, "a") as f:
            f.write(book + "\n")

        print(f"Book Added : {book}")
    
    
    # ----------------------- REMOVE BOOK -----------------------
    
    def remove_book(self, book):
        if self.book_exists(book):
            books = self.read_books()
            
            with open(self.book_file, "w") as f:
                for line in books:
                    if line.strip() != book:
                        f.write(line)
            print(f"Book Removed : {book}")
        
        else:
            print("Book doesn't exist.")
    
    
    # ----------------------- SHOW BOOK -----------------------
    
    def show_books(self):
        print("\n", self.name)
        
        books = self.read_books()
        
        if not books:
            print("Nothing to show.")
            
        else:
            for book in self.read_books():
                print(f"-> {book.strip()}")
    
    
    # ----------------------- SEARCH BOOK -----------------------
    
    def search_book(self, book):
        if self.book_exists(book):
            print(f"Yes, '{book}' exists.")
            
        else:
            print("Book doesn't exist.")


# b = BookLibrary("BookLibrary")

# b.add_book("Harry Potter")
# b.add_book("The Great Gatsby")
# b.remove_book("Harry Potter")
# b.search_book("The Great Gatsby")
# b.show_books()
# print(b.read_books())
# b.add_author("Awais")