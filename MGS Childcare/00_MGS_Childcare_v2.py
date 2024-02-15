"""V2 of base code - 14/02/24
"""


def main():
    choice = 0
    while choice != 5:
        print("---------------------------------------------------------------"
              "--------")
        print("Welcome to MGS Childcare")
        print("What would you like to do? Please choose one of the items "
              "below")
        print("---------------------------------------------------------------"
              "--------")
        print()
        print("1 Drop off a child")
        print("2 Pick up a child")
        print("3 Calculate cost")
        print("4 Print roll")
        print("5 Exit the system")
        print()
        choice = int(input("Enter your choice (number between 1 and 5): "))
        print()
        if choice == 1:
            dropoff()
        elif choice == 2:
            pickup()
        elif choice == 3:
            calc_cost()
        elif choice == 4:
            print_roll()
        else:
            print("Goodbye")
    return choice


# Function to add new child's names to roll
def dropoff():
    name = input("Please enter your child's name: ")
    roll.append(name)
    print(f"{name} was added to the roll")


def pickup():
    check_name = input("Enter the name of the child to pick up: ")
    if check_name not in roll:
        print("Child name not found")
    else:
        roll.remove(check_name)
        print(f"{check_name} has been removed from the roll")


def calc_cost():
    hours = int(input("How many hours: "))
    children = len(roll)
    charge = 12 * hours * children
    print(f"You must pay ${charge}")


def print_roll():
    print(", ".join(roll))


# Main Routine
roll = []
menu = main()
