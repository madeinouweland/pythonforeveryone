class Company():
    def calculate_average_salary(self, employees):
        return sum([e.salary for e in employees]) / len(employees)
