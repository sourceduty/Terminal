# -----------------------------------------------------------------------------
# Underwater Hotel Management Terminal
# 
# Description:
# This Python script is a text-based terminal application designed to manage 
# an underwater hotel's operations. The application includes functionalities 
# for room booking, customer check-in/out, staff management, inventory 
# control, and additional services like restaurant and spa bookings. 
# It provides an interactive menu for seamless operation.
#
# Features:
# - Display available rooms with pricing and status.
# - Book rooms for guests and calculate total costs.
# - Handle guest checkout and update room availability.
# - Manage hotel staff, including adding, removing, and viewing staff members.
# - Manage inventory items with options to add, remove, and view stock.
# - Book additional services like restaurant reservations and spa treatments.
#
# Usage:
# Run the script and follow the menu prompts to perform desired tasks.
#
# -----------------------------------------------------------------------------

import datetime
import os

class UnderwaterHotelManagement:
    def __init__(self):
        self.rooms = {
            101: {'type': 'Single', 'price': 200, 'occupied': False, 'guest': None},
            102: {'type': 'Double', 'price': 300, 'occupied': False, 'guest': None},
            201: {'type': 'Suite', 'price': 500, 'occupied': False, 'guest': None}
        }
        self.staff = {}
        self.inventory = {'Towels': 50, 'Bedsheets': 30, 'Toiletries': 100}
        self.bookings = []
        self.services = {'Restaurant': 50, 'Spa': 100}

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_ascii_art(self):
        print("""
        ████████ ███████ ██████  ███    ███ ██ ███    ██  █████  ██      
           ██    ██      ██   ██ ████  ████ ██ ████   ██ ██   ██ ██      
           ██    █████   ██████  ██ ████ ██ ██ ██ ██  ██ ███████ ██      
           ██    ██      ██   ██ ██  ██  ██ ██ ██  ██ ██ ██   ██ ██      
           ██    ███████ ██   ██ ██      ██ ██ ██   ████ ██   ██ ███████ 
        """)
        print("""
════════════════════════════════════════════════════════════════════════════════
Underwater Hotel Management System!

Manage all operations the underwater hotel resort.
════════════════════════════════════════════════════════════════════════════════
        """)

    def display_menu(self, menu_title, options):
        self.clear_screen()
        self.display_ascii_art()
        print(f"\n{'=' * 80}")
        print(f"{menu_title.center(80)}")
        print(f"{'=' * 80}\n")
        for idx, option in enumerate(options, 1):
            print(f" {idx}. {option}")
        print(f"\n{'=' * 80}")

    def display_rooms(self):
        self.display_menu("Available Rooms", [])
        for room, details in self.rooms.items():
            status = 'Occupied' if details['occupied'] else 'Available'
            print(f"Room {room}: {details['type']} - ${details['price']} - {status}")
        input("\nPress Enter to return to the main menu...")

    def book_room(self):
        self.display_menu("Room Booking", [])
        self.display_rooms()
        room_number = int(input("Enter the room number to book: "))
        if room_number in self.rooms and not self.rooms[room_number]['occupied']:
            guest_name = input("Enter the guest's name: ")
            stay_duration = int(input("Enter the stay duration (days): "))
            self.rooms[room_number]['occupied'] = True
            self.rooms[room_number]['guest'] = guest_name
            booking = {
                'room': room_number,
                'guest': guest_name,
                'duration': stay_duration,
                'checkin_date': datetime.date.today(),
                'checkout_date': datetime.date.today() + datetime.timedelta(days=stay_duration),
                'total_cost': self.rooms[room_number]['price'] * stay_duration
            }
            self.bookings.append(booking)
            print(f"\nRoom {room_number} booked for {guest_name}. Total cost: ${booking['total_cost']}")
        else:
            print("\nInvalid room selection or room already occupied.")
        input("\nPress Enter to return to the main menu...")

    def check_out(self):
        self.display_menu("Guest Check-Out", [])
        room_number = int(input("Enter the room number for checkout: "))
        if room_number in self.rooms and self.rooms[room_number]['occupied']:
            self.rooms[room_number]['occupied'] = False
            guest = self.rooms[room_number]['guest']
            self.rooms[room_number]['guest'] = None
            print(f"\nCheckout successful. Room {room_number} is now available.")
        else:
            print("\nInvalid room or room is not occupied.")
        input("\nPress Enter to return to the main menu...")

    def manage_staff(self):
        self.display_menu("Staff Management", ["Add Staff", "Remove Staff", "View Staff", "Return to Main Menu"])
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter staff name: ")
            role = input("Enter staff role: ")
            self.staff[name] = role
            print(f"\nStaff {name} added as {role}.")
        elif choice == 2:
            name = input("Enter staff name to remove: ")
            if name in self.staff:
                del self.staff[name]
                print(f"\nStaff {name} removed.")
            else:
                print("\nStaff not found.")
        elif choice == 3:
            print("\nCurrent Staff:")
            for name, role in self.staff.items():
                print(f"{name} - {role}")
        else:
            return
        input("\nPress Enter to return to the main menu...")

    def manage_inventory(self):
        self.display_menu("Inventory Management", ["Add Items", "Remove Items", "View Inventory", "Return to Main Menu"])
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"\n{quantity} {item}(s) added.")
        elif choice == 2:
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            if item in self.inventory and self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                print(f"\n{quantity} {item}(s) removed.")
            else:
                print("\nInvalid item or insufficient quantity.")
        elif choice == 3:
            print("\nInventory Details:")
            for item, quantity in self.inventory.items():
                print(f"{item}: {quantity}")
        else:
            return
        input("\nPress Enter to return to the main menu...")

    def book_service(self):
        self.display_menu("Book Additional Services", ["Restaurant", "Spa", "Return to Main Menu"])
        choice = int(input("Enter your choice: "))
        if choice == 1:
            service = 'Restaurant'
        elif choice == 2:
            service = 'Spa'
        else:
            return
        guest_name = input(f"Enter guest's name for {service} booking: ")
        print(f"\n{service} booked for {guest_name} at a cost of ${self.services[service]}.")
        input("\nPress Enter to return to the main menu...")

    def main_menu(self):
        while True:
            self.display_menu("Underwater Hotel Management System", 
                              ["Display Rooms", "Book Room", "Check Out", 
                               "Manage Staff", "Manage Inventory", "Book Services", "Exit"])
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.display_rooms()
            elif choice == 2:
                self.book_room()
            elif choice == 3:
                self.check_out()
            elif choice == 4:
                self.manage_staff()
            elif choice == 5:
                self.manage_inventory()
            elif choice == 6:
                self.book_service()
            elif choice == 7:
                print("\nExiting system. Goodbye!")
                break
            else:
                print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    hotel_management = UnderwaterHotelManagement()
    hotel_management.main_menu()