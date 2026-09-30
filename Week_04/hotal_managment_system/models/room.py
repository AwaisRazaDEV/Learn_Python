
class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number  = room_number
        self.room_type    = room_type
        self.price        = price
        self.is_available = True
    
    
    def display_info(self):
        status = "Avaliable" if self.is_available else "Booked"
        
        print(
            f"Room Number : {self.room_number}\n"
            f"Room Type   : {self.room_type}\n"
            f"Price       : ${self.price}\n"
            f"Status      : {status}"
        )


# room = Room(101, "Single", 20)

# room.display_info()