""" V1 of Speeding Motorists """


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


def speeding():
    warrants = ["Zachary Conroy", "James Wilson", "Helga Norman"]
    offenders = []
    while True:
        name = input("What is the offenders name('x' to exit): ")
        if name.lower() == "x":
            break
        elif name in warrants:
            print(f"{name.upper()} - WARRANT TO ARREST")
        else:
            speed = integer_checker("How much over the speed limit: ")
            if speed < 10:
                fine = 30
            elif 10 <= speed <= 14:
                fine = 80
            elif 14 < speed <= 19:
                fine = 120
            elif 19 < speed <= 24:
                fine = 170
            elif 24 < speed <= 29:
                fine = 230
            elif 29 < speed <= 34:
                fine = 300
            elif 34 < speed <= 39:
                fine = 400
            elif 39 < speed <= 44:
                fine = 510
            else:
                fine = 630
            print(f"{name} to be fined {fine}")

            offenders.append({"Name": name, "Fine": fine})
    print()
    print("Summary")
    for offender in offenders:
        print(f"Name: {offender['Name']} - Fine: ${offender['Fine']} ")


# Main routine
speeding()
