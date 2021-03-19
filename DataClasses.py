# 
# Title: DataClasses
# Description: Creating a Person Class
# ChangeLog: (Who, When, What)
# RRoot, 1.1.2030, Created started script
# DYenubari, modified, added class EmployeeList to complete Assignment 09
#
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class Employee(object):
    """Stores data about an Employee:
        properties:
        employee_id: (int) with the employee's ID
        first_name: (str) with the employee's first name
        last_name: (str) with the employee's last_name
        methods:
        to_string() returns comma separated product data(alias for __str__()
        changelog: ( Who, When, What)
        RRoot, 1.1.2030, Created Class
        """

    # Constructor
    def __init__(self, employee_id, first_name, last_name):
        #  Attributes
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name

    # Properties
    @property
    def employee_id(self):
        return str(self.__employee_id)

    @employee_id.setter
    def employee_id(self, value):
        if not str(value).isalpha():
            self.__employee_id = value
        else:
            raise Exception("ID cannot be letters")

    @property
    def first_name(self):
        return str(self.__first_name)

    @first_name.setter
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):
        return str(self.__last_name)

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    #  Methods
    def to_string(self):
        """ Explicitly returns a list with this object's data"""
        return self.__str__()

    def __str__(self):
        """Implicitly returns field data"""
        return str(self.employee_id) + "," + self.__first_name + "," + self.__last_name


class EmployeeList(Employee):
    """Stores data about an Employee:
    properties:
    employee_id: (int) with the employee's ID
    first_name: (str) with the employee's first name
    last_name: (str) with the employee's last_name
    methods:
    to_string() returns comma separated product data(alias for __str__()
    changelog: ( Who, When, What)
    RRoot, 1.1.2030, Created Class
    """

    # Constructor
    def __init__(self, list_of_objects=None):
        # Attributes
        self.__list_of_objects = list_of_objects
        self.list_of_objects = [] if list_of_objects is None else list_of_objects

    # Methods
    def add_to_list_of_objects(self):  # Overrides the original method(polymorphic)
        """ Explicitly returns a string with this object's data """
        super().__str__()  # gets data from super(Employee)class
        self.list_of_objects.append(Employee)
        return self.list_of_objects

    def __list__(self):  # Overrides the original method(polymorphic)
        """ Implicitly returns field data """
        super().__str__()  # gets data from super(Employee)class
        self.list_of_objects.append(Employee)
        return self.list_of_objects
