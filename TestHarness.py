# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D
    from DataClasses import Employee as Emp
    import ProcessingClasses as P
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test Module
# objPI = D.Person("Andrew", "Jackson")
# objP2 = D.Person("James", "Buchanan")
# lstTable = [objPI, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))

# Test Data Module
objPI = Emp(1, "Andrew", "Jackson")
objP2 = Emp(2, "James", "Buchanan")
list_of_objects = [objPI, objP2]
for row in list_of_objects:
    print(row.to_string(), type(row))

# Test Processing Module
P.FileProcessor.save_data_to_file("EmployeeData.txt", list_of_objects)
fileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
list_of_objects.clear()
for line in fileData:
    list_of_objects.append(Emp(line[0], line[1], line[2].strip()))
for row in list_of_objects:
    print(row.to_string(), type(row))

# Test IO Classes
Eio.print_menu_options()
Eio.print_current_list_employees(list_of_objects)
print(Eio.input_menu_options())
print(Eio.input_employee_data())


