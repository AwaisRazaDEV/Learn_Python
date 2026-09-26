
from pathlib import Path

from .book_library import BookLibrary

class EBookLibrary(BookLibrary):
    def __init__(self, name):
        super().__init__(name)
        self.format_file = self.data_dir / "ebook_format.txt"
        
        self.format_file.touch(exist_ok=True)
    
    
    # ------------------------ READ FORMATS ------------------------
    
    def read_formats(self):
        with open(self.format_file, "r") as file:
            return file.readlines()
    
    
    # ------------------------ FORMAT EXISTS ------------------------
    
    def format_exists(self, book):
        formats = self.read_formats()
        
        for line in formats:
            data = line.strip().split("|")
            
            if data[0] == book:
                return True
        
        return False
    
    
    # ------------------------ ADD FORMAT ------------------------
    
    def add_format(self, book, file_format):
        if self.format_exists(book):
            print("Format for this book already exists.")
            return
        
        with open(self.format_file, "a") as file:
            file.write(f"{book}.{file_format.lower()}\n")
        
        print(f"Format Added : {file_format}")
        print(f"Book         : {book}")
    
    
    # ------------------------ GET FORMAT ------------------------
    
    def get_format(self, book):
        formats = self.read_formats()
        
        for line in formats:
            data = line.strip().split(".")
            
            if data[0] == book:
                return data[1]
        
        return None
    
    
    # ------------------------ SHOW FORMAT ------------------------
    
    def show_format(self, book):
        file_format = self.get_format(book)
        
        if file_format is None:
            print("No ebook format found.")
        
        else:
            print(f"'{book}' Format : {file_format}")
    
    
    # ---------------- DOWNLOAD ----------------

    def download_book(self, book):
        
        if not self.book_exists(book):
            print("Download Failed: Book doesn't exist.")
            return
        
        file_format = self.get_format(book)
        
        if file_format is None:
            print("Download Failed: Ebook format not available.")
            return
        
        print(
            f"Downloading '{book}' "
            f"as {file_format}..."
        )
