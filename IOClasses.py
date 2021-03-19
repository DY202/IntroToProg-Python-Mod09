# ---------------------------------------------------------- #
# Title: IO Classes
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else:
    import DataClasses as DC


class EmployeeIO:
    """a class for performing Employee Input and Output actions
    methods:
    print_menu_options():
    print_current_list-items(list_of_objects):
    input_employee_data():
    changelog: (Who,When,What)
    RRoot, 1.1.2030, Created class:
    """

    @staticmethod
    def print_menu_options():
        """Print a menu of choices to the user"""
        print("""
        ***** Menu of Options ********
        1. Show Current Employee Data
        2. Add New Employee Data
        3. Save Employee Data to File
        4. Read Employee Data from File
        5. Exit Program
        ******************************
        """)

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user
        return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4]- ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message: An optional message you want to display
        :return:nothing
        """
        print(optional_message)
        input("Press the [Enter] key to continue.")

    @staticmethod
    def print_current_list_employees(list_of_objects: list):
        """Print the current items in the list of Employee rows
        :param list_of_objects: (list) of rows you want to display
        """
        print("***** Current Employees *****")
        for row in list_of_objects:
            print(str(row.employee_id)
                  + ","
                  + row.first_name
                  + ","
                  + row.last_name)
        print("*****************************")
        print()

    @staticmethod
    def input_employee_data(list_of_objects):
        """ Gets data for an employee object
        :return: (employee) object with input data
        """
        try:
            employee_id = (input("Employee's ID?- ").strip())
            first_name = str(input("Employee's First Name?- ").strip())
            last_name = str(input("Employee's Last Name?- ").strip())
            print()
            Emp = DC.Employee(employee_id, first_name, last_name)
            list_of_objects.append(Emp)
        except Exception as e:
            print(e)
        return Emp



