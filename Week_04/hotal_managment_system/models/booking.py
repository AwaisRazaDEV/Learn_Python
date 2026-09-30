
# from guest import Guest
# from room import Room

class Booking:
    def __init__(self, guest, room, nights):
        self.guest  = guest
        self.room   = room
        self.nights = nights
    
    
    def calculate_bill(self):
        return self.room.price * self.nights
    
    
    def display_info(self):
        total = self.calculate_bill()
        
        print(
            f"Guest           : {self.guest.name}\n"
            f"Room            : {self.room.room_number}\n"
            f"Room Type       : {self.room.room_type}\n"
            f"Nights          : {self.nights}\n"
            f"Price per Night : ${self.room.price}\n"
            f"Total Bill      : ${total}"
        )

# guest = Guest("Awais", "", "")
# room = Room(101, "Single", 20)
# booking = Booking(guest, room, 2)

# booking.display_info()