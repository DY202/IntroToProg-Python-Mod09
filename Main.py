# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Your Name>,<Today's Date>,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
#
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    import ProcessingClasses as P
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
#
# Load data from file into a list of employee objects when script starts
objPI = Emp(1, "Andrew", "Jackson")
objP2 = Emp(2, "James", "Buchanan")
list_of_objects = [objPI, objP2]
for row in list_of_objects:
    print(row.to_string(), type(row))

# Show user a menu of options
# Get user's menu option choice
while True:
    Eio.print_menu_options()
    strChoice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice == "1":
        Eio.print_current_list_employees(list_of_objects)
        Eio.input_press_to_continue()
        continue

    # Let user add data to the list of employee objects
    elif strChoice == "2":
        print(Eio.input_employee_data(list_of_objects))
        Eio.input_press_to_continue()
        continue

    # let user save current data to file
    elif strChoice == "3":
        P.FileProcessor.save_data_to_file("EmployeeData.txt", list_of_objects)
        Eio.input_press_to_continue()
        continue

    # let user read current data from file
    elif strChoice == "4":
        fileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
        list_of_objects.clear()
        for line in fileData:
            list_of_objects.append(Emp(line[0], line[1], line[2].strip()))
        for row in list_of_objects:
            print(row.to_string(), type(row))
        Eio.input_press_to_continue()
        continue

    # Let user exit program
    else:
        print("Goodbye!")
        break

