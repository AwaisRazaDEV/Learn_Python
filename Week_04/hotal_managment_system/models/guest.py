
class Guest:
    def __init__(self, name, phone, email):
        self.name  = name
        self.phone = phone
        self.email = email
    
    
    def display_info(self):
        print(
            f"Name  : {self.name}\n"
            f"Phone : {self.phone}\n"
            f"Email : {self.email}"
        )