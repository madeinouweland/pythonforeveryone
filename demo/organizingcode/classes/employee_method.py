class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeReport:
    def __init__(self, printer):
        self.printer = printer

    def print(self, employees):
        for employee in employees:
            self.printer(employee)

vera = Employee("Vera", 35000)
chuck = Employee("Chuck", 29000)

formatter = lambda employee : print(f"{employee.name} earns {employee.salary}")

report = EmployeeReport(formatter)
report.print([vera, chuck])
