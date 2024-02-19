""" V1 of Taxi trips """


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


# Function to check for valid input of yes or no
def yes_no(question_text):
    while True:

        # Ask user if they want to start new trip
        answer = input(question_text).lower()

        # If yes output 'Program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no output 'Print summary'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise show 'Error'
        else:
            print("Please enter 'yes' or 'no'")


def menu():
    total_income = 0
    total_time = 0
    number_trips = 0
    name = input("What is your name? ")
    while True:
        answer = yes_no("Would you like to start a new trip(Y/N)? ")
        if answer == "Yes":
            time = integer_checker("How long was the trip(minutes): ")
            cost = 10 + (time * 2)
            print(f"Cost of the trip is {cost}")
            total_time += time
            number_trips += 1
            total_income += cost
        else:
            if number_trips == 0:
                average_time = 0
                average_cost = 0
            else:
                average_time = total_time / number_trips
                average_cost = total_income / number_trips
            print()
            print(f"Today's summary")
            print()
            print(f"Name: {name}")
            print(f"Total time: {total_time} minutes")
            print(f"Average time: {average_time}")
            print(f"Total income today: {total_income}")
            print(f"Average trip cost: {average_cost}")
            break


# Main Routine
menu()
