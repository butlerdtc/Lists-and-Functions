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
booked = {}
name = ""

while True:
    number_needed = integer_checker("How many seats are needed(-1 to exit): ")
    if number_needed <= -1:
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
        chosen = int(input("Choose a vehicle number to book: "))
        if chosen in booked and name in booked[name]:
            print("This vehicle is already booked, please choose another")
        elif chosen not in [v[0] for v in vehicles]:
            print("Invalid vehicle number, please choose another")
        else:
            if name not in booked:
                booked[name] = []
            booked[name].append(chosen)
            print(f"{vehicles[chosen-1][1]} booked by {name}")

print()
print("VEHICLES BOOKED TODAY")
for booker, vehicles_booked in booked.items():
    for vehicle_booked in sorted(vehicles_booked):
        print(f"No. {vehicle_booked} - {vehicles[vehicle_booked-1][1]} - "
              f"booked by {booker.title()}")
