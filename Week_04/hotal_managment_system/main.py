from models.room import Room
from models.guest import Guest
from services.hotel import Hotel

def create_hotel():
    hotel = Hotel("The Baratie")
    
    hotel.add_room(Room(101, "Single", 5))
    hotel.add_room(Room(102, "Single", 10))
    hotel.add_room(Room(103, "Double", 15))
    hotel.add_room(Room(201, "Double", 20))
    hotel.add_room(Room(202, "Single", 25))
    hotel.add_room(Room(301, "Delux", 30))
    
    return hotel


def main():
    hotel = create_hotel()
    
    while True:
        print("\n============ HOTEL MANAGMENT SYSTEM ============")
        print("1. Show Rooms")
        print("2. Add Guest")
        print("3. Show Guests")
        print("4. Book Room")
        print("5. Show Bookings")
        print("6. Checkout")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            hotel.show_rooms()
        
        elif choice == "2":
            name  =  input("Enter guest name : ")
            phone =  input("Enter phone number : ")
            email =  input("Enter email address : ")
            
            guest = Guest(name, phone, email)
            hotel.add_guest(guest)
            print("Guest added Successfully!")
        
        elif choice == "3":
            hotel.show_guests()
        
        elif choice == "4":
            if not hotel.guests:
                print("Please add a guest first.")
                continue
            
            name = input("Enter guest name : ")
            guest = None
            
            for g in hotel.guests:
                if g.name.lower() == name.lower():
                    guest = g
                    break
            
            if guest is None:
                print("Guest not found.")
                continue
            
            try:
                room_number = int(input("Enter room number : "))
                nights      = int(input("Enter number of nights : "))
                
                if nights <= 0:
                    print("Nights must be greater than 0.")
                    continue
                
                hotel.book_room(guest, room_number, nights)
            
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "5":
            hotel.show_bookings()
        
        elif choice == "6":
            try:
                room_number = int(input("Enter room number : "))
                hotel.checkout(room_number)
            except ValueError:
                print("Please enter a valid room number.")
        
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()