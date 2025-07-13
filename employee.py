class Employee:
    def __init__(self, emp_id, name, emp_type, salary_data):
        self.emp_id = emp_id
        self.name = name
        self.emp_type = emp_type
        self.salary_data = salary_data  # Monthly salary or [hours, rate]

    def calculate_salary(self):
        if self.emp_type == "full-time":
            return self.salary_data
        elif self.emp_type == "part-time":
            hours, rate = self.salary_data
            return hours * rate

    def show_info(self):
        salary = self.calculate_salary()
        print(f"{self.emp_id} - {self.name} ({self.emp_type}) : Rs. {salary}")
        
# Create employees
ali = Employee(101, "ethan", "full-time", 60000)
sara = Employee(102, "Alice", "part-time", [90, 500])
ahmed = Employee(103, "Fatima", "full-time", 55000)
zara = Employee(104, "Sarah", "part-time", [80, 600])

