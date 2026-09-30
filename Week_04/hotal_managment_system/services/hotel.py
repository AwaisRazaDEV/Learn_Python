
# if not __package__:
#     import sys
#     from pathlib import Path

#     sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from models.room import Room
from models.guest import Guest
from models.booking import Booking

class Hotel:
    def __init__(self, name):
        self.name = name
        
        self.guests   = []
        self.rooms    = []
        self.bookings = []
    
    
    # ---------- ROOM METHODS ----------
    
    # --- ADD ROOM ---
    def add_room(self, room):
        self.rooms.append(room)
    
    
    # --- SHOW ROOMS ---
    def show_rooms(self):
        print("\n========= ROOMS =========")
        
        if not self.rooms:
            print("No rooms available.")
            return
        
        for room in self.rooms:
            room.display_info()
            print("\t---------\t")
    
    
    # --- FIND ROOM ---
    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        
        return None
    
    
    # ---------- GUEST METHODS ----------
    
    # --- ADD GUEST ---
    def add_guest(self, guest):
        self.guests.append(guest)
    
    
    # --- SHOW GUESTS ---
    def show_guests(self):
        print("\n======= GUESTS =======")
        
        if not self.guests:
            print("No guests found.")
            return
        
        for guest in self.guests:
            guest.display_info()
            print("\t-------\t")
    
    
    # ---------- BOOKING METHOD  ----------
    
    # --- BOOK ROOM ---
    def book_room(self, guest, room_number, nights):
        room = self.find_room(room_number)
        
        if room is None:
            print("Room not found.")
            return
        
        if not room.is_available:
            print("Soory, this room is already booked.")
            return
        
        booking = Booking(guest, room, nights)
        self.bookings.append(booking)
        room.is_available = False
        
        print("Room Booked Successfully!\n")
        print(f"Total : ${booking.calculate_bill()}")
    
    
    # --- SHOW BOOKINGS ---
    def show_bookings(self):
        print("\n======= BOOKINGS =======")
        
        if not self.bookings:
            print("No bookings found.")
            return
        
        for booking in self.bookings:
            booking.display_info()
            print("\t-------\t")
    
    
    # ---------- CHECKOUT ----------
    def checkout(self, room_number):
        booking_found = None
        
        for booking in self.bookings:
            if booking.room.room_number == room_number:
                booking_found = booking
                break
        
        if booking_found is None:
            print("No booking found for this room.")
            return
        
        booking_found.display_info()
        booking_found.room.is_available = True
        self.bookings.remove(booking_found)
        
        print("Checkout Successfull")
        print(f"Room {room_number} is now available.")



# room1 = Room(102, "Double", 5)
# room2 = Room(202, "Single", 10)
# guest = Guest("Awais Raza", "03247112235", "awais@gmail.com")


# hotel = Hotel("Awais ka hotel")
# hotel.add_room(room1)
# hotel.add_room(room2)
# hotel.add_guest(guest)
# hotel.show_rooms()
# hotel.show_guests()
# hotel.book_room(guest, room2, 1)
# hotel.checkout(202)