
# < ========================  Class Properties  ======================== >

# Properties are variables that belong to a class. They store data for each object created from the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age      # These "self.name" and "self.age" are the properties of the class.


p1 = Person("Awais", 20)
p2 = Person("Sara", 38)

print("Before : " + p1.name)  # Now I'm accessing the class properties unsing dot notation.

p1.name = "John"     # Now I modify the value of properties on object
print("After : " + p1.name)

del p1.age      # I delete the property from object using "del" keyword.
# print(p1.age)     # It raise an error!


# You can add new properties to existing objects:
p1.city = "Lahore"
print(p1.city)


# Adding/Deleting properties only adds/deletes them to that specific object, not to all objects of the class
# Such as:
print(p2.age)       # We only del age property for p1
# print(p2.city)      # It raise an error!



# <-------------------- Class Properties vs Object Properties -------------------->

# Properties defined inside __init__() belong to each object are "Instance Properties".

# Properties defined outside methods belong to the class itself are "Class Properties" and they are shared by all objects.

class Person:
    lname = "Gondal"    # Class Property
    
    def __init__(self, name):
        self.name = name    # Instance Property


p1 = Person("Awais")
p2 = Person("Qais")

print(p1.name, p1.lname)

Person.lname = "Raza" 
# I modify the Class Property and it changes for all the objets.
print("After :", p2.name, p2.lname)
print("After :", p1.name, p1.lname)



# < ========================  Class Methods  ======================== >
# Methods are functions that belong to a class. They define the behavior of objects created from the class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def greet(self):    # This is method of the class. All methods must have self as the first parameter.
        self.age += 1
        return f"Hello, My name is {self.name} and I'm {self.age} years old"


p1 = Person("Awais Raza", 20)

print(p1.greet())
print(p1.greet())   # I'm accessing and modifing the object properties through method define in class.

# We can also delete the method from class using "del" keyword.


print()

# <----------------- Multiple Methods(with small program) ----------------->
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book Added : {book}")
    
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book Removed : {book}")
    
    
    def show_books(self):
        print(f"\nLibrary '{self.name}'")
        if not self.books:
            print("Nothing to Show.")
        else:
            for book in self.books:
                print("-> " + book)
    
    
    def search_book(self, book):
        if book in self.books:
            print(f"Yes, '{book}' exists.")
        else:
            print("Book not found.")


mylibrary = Library("City Library")

mylibrary.add_book("Harry Potter")
mylibrary.add_book("The Alchemist")
mylibrary.add_book("The Great Gatsby")
mylibrary.add_book("Book 404")

mylibrary.remove_book("Book 404")
mylibrary.search_book("The Alchemist")
mylibrary.show_books()
