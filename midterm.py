class Star_Cinema:
    _hall_list = []  

    @classmethod
    def get_hall_list(cls):
        return cls._hall_list

    def entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}  
        self.__show_list = []  
        self.__rows = rows  
        self.__cols = cols  
        self.__hall_no = hall_no  
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = {'id': id, 'movie_name': movie_name, 'time': time}
        self.__show_list.append(show_info)
        self.__seats[id] = [["0" for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, id, seats_to_book):
        try:
            if id not in self.__seats:
                raise ValueError("Invalid show ID.")
            for row, col in seats_to_book:
                if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                    raise IndexError("Seat does not exist.")
                if self.__seats[id][row][col] == "1":
                    raise ValueError("The seat is already booked.")
                self.__seats[id][row][col] = "1"
            return True  
        except (ValueError, IndexError) as e:
            print(e)
            return False  

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return []
        return self.__seats[id]

    def display_seats_matrix(self, id):
        if id not in self.__seats:
            print("Invalid show ID.")
            return
        seats_matrix = self.__seats[id]
        for row in seats_matrix:
            print(" ".join(row))
        print()  

def main_menu():
    star_cinema = Star_Cinema()
    hall_1 = Hall(5, 5, 1)
    hall_1.entry_show("1", "Lover Boy Sakib Khan", "6:00")
    hall_1.entry_show("2", "Aynabaji", "10:00")
    hall_2 = Hall(5, 5, 2)
    hall_2.entry_show("3", "Toofan", "18:00")
    hall_2.entry_show("4", "Pathaan", "21:00")

    while True:
        print("1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. EXIT")
        option = input("ENTER OPTION: ")

        if option == "1":
            for hall in star_cinema.get_hall_list():
                print(f"Hall {hall._Hall__hall_no}:")
                for show in hall.view_show_list():
                    print(f"Show ID: {show['id']}, Movie Name: {show['movie_name']}, Time: {show['time']}")
                print()  
        elif option == "2":
            hall_no = input("Enter the hall number: ")
            show_id = input("Enter the show ID: ")
            hall_found = False
            for hall in star_cinema.get_hall_list():
                if hall._Hall__hall_no == int(hall_no):
                    hall_found = True
                    show_exists = any(show['id'] == show_id for show in hall.view_show_list())
                    if show_exists:
                        print(f"Available seats for Show ID {show_id}:")
                        hall.display_seats_matrix(show_id)
                    else:
                        print(f"Show ID {show_id} does not exist in Hall {hall_no}.")
            if not hall_found:
                print(f"Hall {hall_no} does not exist.")

        elif option == "3":
            hall_no = input("Enter the hall number: ")
            show_id = input("Enter the show ID: ")
            num_seats = int(input("Enter the number of seats to book: "))
            seats_to_book = []
            for _ in range(num_seats):
                try:
                    row = int(input("Enter the row number: ")) - 1  
                    col = int(input("Enter the column number: ")) - 1  
                    seats_to_book.append((row, col))
                except ValueError:
                    print("Invalid seat coordinates. Please enter numeric values.")
                    continue  
            booking_successful = False
            for hall in Star_Cinema.get_hall_list():  
                if hall._Hall__hall_no == int(hall_no):
                    booking_successful = hall.book_seats(show_id, seats_to_book)
                    break
            else:
                print(f"Hall {hall_no} does not exist.")
                continue  

            if booking_successful:
                print("Seats booked successfully.")

        elif option == "4":
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
