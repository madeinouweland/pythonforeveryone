class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary = self.salary + self.salary * percent / 100

    def email(self):
        return f"{self.name.lower()}@abc.com"
