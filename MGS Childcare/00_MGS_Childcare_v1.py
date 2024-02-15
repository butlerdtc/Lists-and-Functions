"""V1 of base code, supplied by Mr Baker, made into a function by Robson
Butler - 14/02/24
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
            dropOff()
        elif choice == 2:
            pickUp()
        elif choice == 3:
            calcCost()
        elif choice == 4:
            printRoll()
        else:
            print("Goodbye")


# Main Routine
