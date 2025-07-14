from abc import ABC, abstractmethod

# -------------------------------
# Abstract Base Class
# -------------------------------
class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def show_info(self):
        salary = self.calculate_salary()
        print(f"{self.emp_id} - {self.name} ({self.__class__.__name__}) : Rs. {salary}")


# -------------------------------
# Full-Time Employee Subclass
# -------------------------------
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# -------------------------------
# Part-Time Employee Subclass
# -------------------------------
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, rate_per_hour):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour


# -------------------------------
# Creating Employee Objects
# -------------------------------
ali = FullTimeEmployee(101, "Ali", 60000)
sara = PartTimeEmployee(102, "Sara", 90, 500)
ahmed = FullTimeEmployee(103, "Ahmed", 55000)
zara = PartTimeEmployee(104, "Zara", 80, 600)

# -------------------------------
# READ Operation
# -------------------------------
print(" Employee Payroll Report:\n")
ali.show_info()
sara.show_info()
ahmed.show_info()
zara.show_info()

# -------------------------------
# UPDATE Operation (Zara)
# -------------------------------
zara.name = "Zara Khan"
zara.rate_per_hour = 650

print("\n Updated Zara's Info:\n")
zara.show_info()

# -------------------------------
# DELETE Operation (Remove Ahmed)
# -------------------------------
print("\n Removed Ahmed from report\n")
print(" Final Payroll Report:\n")
ali.show_info()
sara.show_info()
zara.show_info()
