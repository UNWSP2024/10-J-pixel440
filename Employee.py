# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.name=name
        self.ID_number=ID_number
        self.department=department
        self.job_title=job_title

    def employee_data(self):
        print(f"Name: {self.name}")
        print(f"ID_number: {self.ID_number}")
        print(f"department: {self.department}")
        print(f"Job title: {self.job_title}")


employee_1 =Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee_2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee_3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

employee_1.employee_data()
employee_2.employee_data()
employee_3.employee_data()


