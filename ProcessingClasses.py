# Title: Processing Classes
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


class FileProcessor:
    """Processes data to and from a file and list of objects:
    methods:
    save_data_to_file(file_name,list_of_objects):
    read_data_from_file(file_name): -> (a list of objects)
    changelog:( Who, When, What)
    RRoot, 1.1 2030, Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects):
        """Writes data to a file from a list of object rows
        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
            print("Data has been saved to file!")
            print()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep="\n")
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """Reads data from a file into a list of object rows
        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
            print("***** Current Data from file *****")
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep="\n")
        return list_of_rows


class DatabaseProcessor:
    pass
