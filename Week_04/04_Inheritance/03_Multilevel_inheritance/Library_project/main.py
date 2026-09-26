



# <-------------------------------- (Challenge 2) -------------------------------->
# 1. Library → manages books
#       |
# 2. BookLibrary → manages book authors/categories
#       |
# 3. EBookLibrary → manages file formats such as PDF/EPUB


from library import EBookLibrary


library = EBookLibrary("My Digital Library")



# library.add_format("The Great Gatsby", "PDF")
library.show_format("Awais")
# library.download_book("Awais")
# Add books
# library.add_book(
#     "The Great Gatsby",
#     "F. Scott Fitzgerald",
#     "Classic"
# )

# library.add_book(
#     "Harry Potter",
#     "J.K. Rowling",
#     "Fantasy"
# )

# library.add_book(
#     "Clean Code",
#     "Robert C. Martin",
#     "Programming"
# )



# library.show_books()


# print("\n--- Search Book ---")
# library.search_book("Clean Code")



# library.show_book_details("Harry Potter")


# print("\n--- Add Ebook Format ---")
# library.add_format("Harry Potter", "PDF")


# print("\n--- Ebook Format ---")
# library.show_format("Harry Potter")


# print("\n--- Download ---")
# library.download_book("Harry Potter")


# print("\n--- Remove Book ---")
# library.remove_book("The Great Gatsby")


# print("\n--- Books After Removal ---")
# library.show_books()