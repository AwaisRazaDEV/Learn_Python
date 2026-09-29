
# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in the class, while controlling how the data can be accessed from outsice the class.


# <----------------------------- Advantages ----------------------------->
# 1. Protects data from unauthorized access and accidental modification.
# 2. Controls data updates using getter/setter methods with validation.
# 3. Enhances modularity by hiding internal implementation details.
# 4. Reflects real-world scenarios like restricting direct access to a bank account balance.


# <----------------------------- Access Specifiers ----------------------------->
# Access specifiers define how class members (variables and methods) can be accessed from outside the class.
# They help in implementing encapsulation by controlling the visibility of data. There are three types of access specifiers:


# ----- 1. Public Members -----
# Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules.
# By default, all members in Python are public.
# They are defined without any underscore prefix (e.g., self.name).

# ----- Example -----
class Employee:
    def __init__(self, name):
        self.name = name    # Pubilc attribute
    
    def display_name(self): # Pubilc method
        print(self.name)


person = Employee("John")
print(person.name)      # Accessible
person.display_name()   # Accessible


# ----- 2. Protected Members -----
# Protected members are variables or methods that are intended to be accessed only within the class and its subclasses.
# They are not strictly private but should be treated as internal.
# In Python, protected members are defined with a single underscore prefix (e.g., self._name).

# ----- Example -----
class Employee:
    def __init__(self, name, age):
        self.name = name    # Public
        self._age = age     # Protected

class SubEmployee(Employee):    # Accessible in Subclass
    def show_age(self):
        print("Age :", self._age)


person = SubEmployee("Smith", 20)
print(person._age)  # Can access, but shouldn't
person.show_age()   # Protected accessed through subclass

# A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction.


# ----- 3. Private Members -----
# Private members are variables or methods that cannot be accessed directly from outside the class.
# They are used to restrict access and protect internal data.
# In Python, private members are defined with a double underscore prefix (e.g., self.__salary).

# ----- Example -----
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # private
    
    def show_salary(self):
        print("Salary :", self.__salary)


person = Employee("Sara", 50000)
person.show_salary()        # Accessing private correctly
# print(person.__salary)    # Error: Not accessible directly


# ----- Name Mangling -----
# Name mangling is how Python implements private properties and methods.
# When you use double underscores __, Python uses name mangling, where the interpreter internally renames the variable (for eg, __salary becomes _ClassName__salary).

# Although name-mangled variables are meant to be protected, they can still be accessed using the mangled name.
print("Using Name Mangling :", person._Employee__salary)



# <----------------------------- Getter and Setter Methods ----------------------------->
# In Python, getter and setter methods are used to access and modify private attributes safely.

# Instead of accessing private data directly, these methods provide controlled access, allowing you to:
# --> Read data using a getter method.
# --> Update data using a setter method with optional validation or restrictions.

# ----- Example -----
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    
    def get_salary(self):           # Get method
        print("Salary :", self.__salary)
    
    def set_salalry(self, amount):  # Set method
        if amount > 0:
            self.__salary = amount
            return self.__salary
        else:
            print("Invalid salary amount!")


person = Employee(60000)

person.get_salary()
print(person.set_salalry(70000))