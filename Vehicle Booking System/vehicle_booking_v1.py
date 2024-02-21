""" V1 of Vehicle Booking """


# Integer Checking Function
def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


vehicles = [[1, "Suzuki Van", 2], [2, "Toyota Corolla", 4], [3, "Honda CRV",
            4], [4, "Suzuki Swift", 4], [5, "Mitsubishi Air-trek", 4], [6,
            "Nissan DC Ute", 4], [7, "Toyota Pre-via", 7], [8, "Toyota Hi Ace",
            12], [9, "Toyota Hi Ace", 12]]

while True:
    number_needed = integer_checker("How many seats are needed: ")
    if number_needed == -1:
        print("Program Finished")
        break
    else:
        print("VEHICLE NUMBER - TYPE - NO. SEATS")
        for vehicle in vehicles:
            if number_needed > vehicle[2]:
                print(f"No. {vehicle[0]} - {vehicle[1]} - {vehicle[2]} seats -"
                      f" NOTE: Not enough space")
            else:
                print(f"No. {vehicle[0]} - {vehicle[1]} - {vehicle[2]} seats ")
        print()
        name = input("Enter your name: ")
        print(f"{} booked by {name}")
        