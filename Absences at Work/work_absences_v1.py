""" V1 of Work Absences """


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


names = []
total_absences = 0
highest_absences = 0
most_absent_employee = []
while True:
    employee_name = input("Enter employee name(or $ to terminate program): ")
    if employee_name == "$":
        break
    else:
        days = integer_checker("Enter number of absences: ")
        total_absences += days
        names.append([employee_name, days])

total_employees = len(names)

for employee_name in names:
    if employee_name[1] > highest_absences:
        highest_absences = employee_name[1]
        most_absent_employee = [employee_name]
    elif employee_name[1] == highest_absences:
        most_absent_employee.append(employee_name)

average_absences = round(total_absences/total_employees, 2)
print(f"\nThe average number of absences was {average_absences}")
if len(most_absent_employee) > 1:
    print(f"The employees with the most absences are: ")
    for names in most_absent_employee:
        print(f"\t{names[0]}")
    print(f"\twith {most_absent_employee[0][1]} days absent")
else:
    print(f"{most_absent_employee[0][0]} was the most absent employee with "
          f"{highest_absences} days absent")
